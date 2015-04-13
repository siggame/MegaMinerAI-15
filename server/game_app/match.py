from base import *
from matchUtils import *
from objects import *
import networking.config.config
from collections import defaultdict
from networking.sexpr.sexpr import *
import os
import itertools
import scribe
import jsonLogger
import maze

Scribe = scribe.Scribe


def loadClassDefaults(cfgFile = "config/defaults.cfg"):
  cfg = networking.config.config.readConfig(cfgFile)
  for className in cfg.keys():
    for attr in cfg[className]:
      setattr(eval(className), attr, cfg[className][attr])

class Match(DefaultGameWorld):
  def __init__(self, id, controller):
    self.id = int(id)
    self.controller = controller
    DefaultGameWorld.__init__(self)
    self.scribe = Scribe(self.logPath())
    if( self.logJson ):
      self.jsonLogger = jsonLogger.JsonLogger(self.logPath())
      self.jsonAnimations = []
      self.dictLog = dict(gameName = "Pharaoh", turns = [])
    self.addPlayer(self.scribe, "spectator")

    self.grid = []
    self.mapWidth = self.mapWidth
    self.mapHeight = self.mapHeight
    self.turnNumber = 0
    self.roundTurnNumber = 0
    self.maxThieves = self.maxThieves
    self.maxTraps = self.maxTraps
    self.playerID = -1
    self.gameNumber = id
    self.roundNumber = 0
    self.scarabsForTraps = self.scarabsForTraps
    self.scarabsForThieves = self.scarabsForThieves
    self.maxStack = self.maxStack
    self.roundsToWin = self.roundsToWin
    self.roundTurnLimit = self.roundTurnLimit

  #this is here to be wrapped
  def __del__(self):
    pass

  def addPlayer(self, connection, type="player"):
    connection.type = type
    if len(self.players) >= 2 and type == "player":
      return "Game is full"
    if type == "player":
      self.players.append(connection)
      try:
        self.addObject(Player, [connection.screenName, self.startTime, self.scarabsForTraps, 0])
      except TypeError:
        raise TypeError("Someone forgot to add the extra attributes to the Player object initialization")
    elif type == "spectator":
      self.spectators.append(connection)
      #If the game has already started, send them the ident message
      if (self.turn is not None):
        self.sendIdent([connection])
    return True

  def removePlayer(self, connection):
    if connection in self.players:
      if self.turn is not None:
        winner = self.players[1 - self.getPlayerIndex(connection)]
        self.declareWinner(winner, 'Opponent Disconnected')
      self.players.remove(connection)
    else:
      self.spectators.remove(connection)

  def loadTypeConfig(self):
    cfgTrapTypes = networking.config.config.readConfig("config/trapTypes.cfg")
    cfgThiefTypes = networking.config.config.readConfig("config/thiefTypes.cfg")
    trapTypeStatlist = ['name', 'type', 'cost', 'maxInstances', 'startsVisible', 'hasAction', 'deactivatable', 'maxActivations', 'activatesOnWalkedThrough', 'turnsToActivateOnTile', 'canPlaceOnWalls', 'canPlaceOnOpenTiles', 'freezesForTurns', 'killsOnActivate', 'cooldown', 'explosive', 'unpassable']
    thiefTypeStatlist = ['name', 'type', 'cost', 'maxMovement', 'maxSpecials', 'maxInstances']
    trapTypes = cfgTrapTypes.values()
    trapTypes.sort(key=lambda trapType: trapType['type'])
    for trapTypeStats in trapTypes:
      newTrapType = self.addObject(TrapType, [trapTypeStats[key] for key in trapTypeStatlist])
    thiefTypes = cfgThiefTypes.values()
    thiefTypes.sort(key=lambda thiefType: thiefType['type'])
    for thiefTypeStats in thiefTypes:
      self.addObject(ThiefType, [thiefTypeStats[key] for key in thiefTypeStatlist])

  def start(self):
    if len(self.players) < 2:
      return "Game is not full"
    if self.winner is not None or self.turn is not None:
      return "Game has already begun"

    self.loadTypeConfig()

    #TODO: START STUFF
    self.turn = self.players[-1]
    self.turnNumber = -1
    self.roundTurnNumber = -1

    self.grid = [[[ self.addObject(Tile,[x, y, self.empty]) ] for y in range(self.mapHeight)] for x in range(self.mapWidth)]

    self.setupRound()

    self.nextTurn()
    return True

  def setupRound(self):
      generatedMaze = maze.generate(self.mapHeight)
      for y in range(self.mapHeight):
        for x in range(self.mapWidth):
          self.grid[x][y][:] = self.grid[x][y][0:1] # Remove everything except tile
          self.grid[x][y][0].type = generatedMaze[x % (self.mapWidth / 2)][y]
          self.grid[x][y][0].updatedAt = self.turnNumber # updatedAt tells the server to resend tile data

      # Remove any traps and thieves from the previous round
      for trap in list(self.objects.traps):
        #self.grid[trap.x][trap.y].remove(trap)
        self.removeObject(trap)
      for thief in list(self.objects.thiefs):
        #self.grid[thief.x][thief.y].remove(thief)
        self.removeObject(thief)

      # Place a sarcophagus, players can still move it later
      # ['id', 'x', 'y', 'owner', 'trapType', 'visible', 'active', 'bodyCount', 'activationsRemaining', 'turnsTillActive']
      sarcophagus_stats = [self.mapWidth / 4 + 1, self.mapHeight / 2 + 1, 0, self.sarcophagus, 1, 1, 0, 0, 0]
      self.grid[self.mapWidth / 4 + 1][self.mapHeight / 2 + 1].append( self.addObject(Trap, sarcophagus_stats))
      sarcophagus_stats = [self.mapWidth / 4 + 1 + self.mapWidth / 2, self.mapHeight / 2 + 1, 1, self.sarcophagus, 1, 1, 0, 0, 0]
      self.grid[self.mapWidth / 4 + 1 + self.mapWidth / 2][self.mapHeight / 2 + 1].append( self.addObject(Trap, sarcophagus_stats))

      return True

  def getTile(self, x, y):
    if (0 <= x < self.mapWidth) and (0 <= y < self.mapHeight):
      return self.grid[x][y][0]
    else:
      return None

  def getTrap(self, x, y):
    if (0 <= x < self.mapWidth) and (0 <= y < self.mapHeight):
      trap = None
      for unit in self.grid[x][y][1:]:
        if isinstance(unit, Trap):
          trap = unit
      return trap
    else:
      return None

  def nextTurn(self):
    self.turnNumber += 1
    self.roundTurnNumber += 1
    if self.turn == self.players[0]:
      self.turn = self.players[1]
      self.playerID = 1
    elif self.turn == self.players[1]:
      self.turn = self.players[0]
      self.playerID = 0
    else:
      return "Game is over."

    self.checkRoundWinner()

    for obj in self.objects.values():
      obj.nextTurn()

    self.checkWinner()
    if self.winner is None:
      self.sendStatus([self.turn] +  self.spectators)
    else:
      self.sendStatus(self.spectators)
    
    if( self.logJson ):
      self.dictLog['turns'].append(
        dict(
          mapWidth = self.mapWidth,
          mapHeight = self.mapHeight,
          turnNumber = self.turnNumber,
          roundTurnNumber = self.roundTurnNumber,
          maxThieves = self.maxThieves,
          maxTraps = self.maxTraps,
          playerID = self.playerID,
          gameNumber = self.gameNumber,
          roundNumber = self.roundNumber,
          scarabsForTraps = self.scarabsForTraps,
          scarabsForThieves = self.scarabsForThieves,
          maxStack = self.maxStack,
          roundsToWin = self.roundsToWin,
          roundTurnLimit = self.roundTurnLimit,
          Players = [i.toJson() for i in self.objects.values() if i.__class__ is Player],
          Mappables = [i.toJson() for i in self.objects.values() if i.__class__ is Mappable],
          Tiles = [i.toJson() for i in self.objects.values() if i.__class__ is Tile],
          Traps = [i.toJson() for i in self.objects.values() if i.__class__ is Trap],
          Thiefs = [i.toJson() for i in self.objects.values() if i.__class__ is Thief],
          ThiefTypes = [i.toJson() for i in self.objects.values() if i.__class__ is ThiefType],
          TrapTypes = [i.toJson() for i in self.objects.values() if i.__class__ is TrapType],
          animations = self.jsonAnimations
        )
      )
      self.jsonAnimations = []

    self.animations = ["animations"]
    return True

  def checkRoundWinner(self):
    sarcophagi = dict()
    for trap in self.objects.traps:
      if trap.trapType == self.sarcophagus:
        sarcophagi[trap.owner] = trap

    #check if there are any enemy thieves on the sarcophagus
    for playerID in [0, 1]:
      for obj in self.grid[sarcophagi[playerID].x][sarcophagi[playerID].y]:
        if isinstance(obj, Thief):
          self.declareRoundWinner(self.objects.players[obj.owner], "Player {} reached the sarcophagus".format(obj.owner))
          return True

    if self.roundTurnNumber >= self.roundTurnLimit:
      #the winner at this point is the player who is closest to their sarcophagus
      player0Closest = 100
      player1Closest = 100
      for thief in self.objects.thiefs:
        if thief.owner == 0:
          player0Closest = min(player0Closest, abs(thief.x-sarcophagi[1].x) + abs(thief.y-sarcophagi[1].y))
        else:
          player1Closest = min(player1Closest, abs(thief.x-sarcophagi[0].x) + abs(thief.y-sarcophagi[0].y))

      if player0Closest < player1Closest:
        self.declareRoundWinner(self.objects.players[0], "Player 0 was closest to their sarcophagus")
      elif player1Closest < player0Closest:
        self.declareRoundWinner(self.objects.players[1], "Player 1 was closest to their sarcophagus")
      else:
        #TODO: Add more tiebreakers
        self.declareRoundWinner(self.objects.players[0], "Because I said so, this should be removed")
      return True
    return False

  def checkWinner(self):
    for playerObj in self.objects.players:
      if playerObj.roundsWon >= self.roundsToWin:
        self.declareWinner(self.players[playerObj.id], "Player {} ({}) reached {} points".format(playerObj.id, self.players[playerObj.id].user, self.roundsToWin))

  #declare the round winner and reset the match
  def declareRoundWinner(self, winner, reason=''):
    winnerName = self.players[winner.id].user
    winner.roundsWon = winner.roundsWon + 1
    print "Turn {}: Player {} ({}) wins round {} for game {} because {}".format(self.turnNumber, winner.id, winnerName, self.roundNumber, self.id, reason)
    self.roundNumber += 1
    if winner.roundsWon < self.roundsToWin:
      #TODO: Add an animation declaring the round winner
      self.setupRound()
      self.roundTurnNumber = 0

  def declareWinner(self, winner, reason=''):
    self.winner = winner
    print "Player {} ({}) wins game {} because {}".format(self.getPlayerIndex(self.winner), self.winner.user, self.id, reason)

    msg = ["game-winner", self.id, self.winner.user, self.getPlayerIndex(self.winner), reason]
    
    if( self.logJson ):
      self.dictLog["winnerID"] =  self.getPlayerIndex(self.winner)
      self.dictLog["winReason"] = reason
      self.jsonLogger.writeLog( self.dictLog )
    
    self.scribe.writeSExpr(msg)
    self.scribe.finalize()
    self.removePlayer(self.scribe)

    for p in self.players + self.spectators:
      p.writeSExpr(msg)
    
    self.sendStatus([self.turn])
    self.playerID ^= 1
    self.sendStatus([self.players[self.playerID]])
    self.playerID ^= 1
    self.turn = None
    self.objects.clear()

  def logPath(self):
    return "logs/" + str(self.id)

  @derefArgs(Player, None, None, None)
  def placeTrap(self, object, x, y, trapType):
    return object.placeTrap(x, y, trapType, )

  @derefArgs(Player, None, None, None)
  def purchaseThief(self, object, x, y, thiefType):
    return object.purchaseThief(x, y, thiefType, )

  @derefArgs(Player, None)
  def pharaohTalk(self, object, message):
    return object.pharaohTalk(message, )

  @derefArgs(Trap, None, None)
  def act(self, object, x, y):
    return object.act(x, y, )

  @derefArgs(Trap)
  def toggle(self, object):
    return object.toggle()

  @derefArgs(Thief, None)
  def thiefTalk(self, object, message):
    return object.thiefTalk(message, )

  @derefArgs(Thief, None, None)
  def move(self, object, x, y):
    return object.move(x, y, )

  @derefArgs(Thief, None, None)
  def useSpecial(self, object, x, y):
    return object.useSpecial(x, y, )


  def sendIdent(self, players):
    if len(self.players) < 2:
      return False
    list = []
    for i in itertools.chain(self.players, self.spectators):
      list += [[self.getPlayerIndex(i), i.user, i.screenName, i.type]]
    for i in players:
      i.writeSExpr(['ident', list, self.id, self.getPlayerIndex(i)])

  def getPlayerIndex(self, player):
    try:
      playerIndex = self.players.index(player)
    except ValueError:
      playerIndex = -1
    return playerIndex

  def sendStatus(self, players):
    for i in players:
      i.writeSExpr(self.status())
      i.writeSExpr(self.animations)
    return True


  def status(self):
    msg = ["status"]

    msg.append(["game", self.mapWidth, self.mapHeight, self.turnNumber, self.roundTurnNumber, self.maxThieves, self.maxTraps, self.playerID, self.gameNumber, self.roundNumber, self.scarabsForTraps, self.scarabsForThieves, self.maxStack, self.roundsToWin, self.roundTurnLimit])

    typeLists = []
    typeLists.append(["Player"] + [i.toList() for i in self.objects.players])
    typeLists.append(["Mappable"] + [i.toList() for i in self.objects.values() if i.__class__ is Mappable])
    updated = [i for i in self.objects.tiles if i.updatedAt > self.turnNumber-3]
    if updated:
      typeLists.append(["Tile"] + [i.toList() for i in updated])
    typeLists.append(["Trap"] + [i.toList() for i in self.objects.traps])
    typeLists.append(["Thief"] + [i.toList() for i in self.objects.thiefs])
    updated = [i for i in self.objects.thiefTypes if i.updatedAt > self.turnNumber-3]
    if updated:
      typeLists.append(["ThiefType"] + [i.toList() for i in updated])
    updated = [i for i in self.objects.trapTypes if i.updatedAt > self.turnNumber-3]
    if updated:
      typeLists.append(["TrapType"] + [i.toList() for i in updated])

    msg.extend(typeLists)

    return msg

  def addAnimation(self, anim):
    # generate the sexp
    self.animations.append(anim.toList())
    # generate the json
    if( self.logJson ):
      self.jsonAnimations.append(anim.toJson())
  


loadClassDefaults()

