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

    #TODO: INITIALIZE THESE!
    self.grid = []
    self.mapWidth = None
    self.mapHeight = None
    self.turnNumber = None
    self.roundTurnNumber = None
    self.maxThieves = None
    self.maxTraps = None
    self.playerID = None
    self.gameNumber = id
    self.roundNumber = None
    self.scarabsForTraps = None
    self.scarabsForThieves = None
    self.maxStack = None

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
        self.addObject(Player, [connection.screenName, self.startTime])
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

  def start(self):
    if len(self.players) < 2:
      return "Game is not full"
    if self.winner is not None or self.turn is not None:
      return "Game has already begun"

    #TODO: START STUFF
    self.turn = self.players[-1]
    self.turnNumber = -1
	self.roundTurnNumber = -1
    self.grid = [[[ self.addObject(Tile,[x, y, -1]) ] for y in range(self.mapHeight)] for x in range(self.mapWidth)]

    self.nextTurn()
    return True

  def getTile(self, x, y):
    if (0 <= x < self.mapWidth) and (0 <= y < self.mapHeight):
      return self.grid[x][y][0]
    else:
      return None

  def getRealX(self, player, x, side):
	if player == 0:
		if side == 0:# left player placing traps
			return x
		else:# left player placing thieves
			return x + (self.mapWidth / 2)
	else:
		if side == 1:# right player placing traps
			return x + (self.mapWidth / 2)
		else:# right player placing thieves
			return x

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

  def checkWinner(self):
    #TODO: Make this check if a player won, and call declareWinner with a player if they did
    if self.turnNumber >= self.turnLimit:
       self.declareWinner(self.players[0], "Because I said so, this should be removed")


  def declareWinner(self, winner, reason=''):
    print "Player", self.getPlayerIndex(self.winner), "wins game", self.id
    self.winner = winner

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
  def act(self, object, x, y):
    return object.act(x, y, )


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

    msg.append(["game", self.mapWidth, self.mapHeight, self.turnNumber, self.roundTurnNumber, self.maxThieves, self.maxTraps, self.playerID, self.gameNumber, self.roundNumber, self.scarabsForTraps, self.scarabsForThieves, self.maxStack])

    typeLists = []
    typeLists.append(["Player"] + [i.toList() for i in self.objects.values() if i.__class__ is Player])
    typeLists.append(["Mappable"] + [i.toList() for i in self.objects.values() if i.__class__ is Mappable])
    updated = [i for i in self.objects.values() if i.__class__ is Tile and i.updatedAt > self.turnNumber-3]
    if updated:
      typeLists.append(["Tile"] + [i.toList() for i in updated])
    typeLists.append(["Trap"] + [i.toList() for i in self.objects.values() if i.__class__ is Trap])
    typeLists.append(["Thief"] + [i.toList() for i in self.objects.values() if i.__class__ is Thief])
    updated = [i for i in self.objects.values() if i.__class__ is ThiefType and i.updatedAt > self.turnNumber-3]
    if updated:
      typeLists.append(["ThiefType"] + [i.toList() for i in updated])
    updated = [i for i in self.objects.values() if i.__class__ is TrapType and i.updatedAt > self.turnNumber-3]
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

