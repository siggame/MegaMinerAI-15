class Player(object):
  game_state_attributes = ['id', 'playerName', 'time', 'scarabs', 'roundsWon']
  def __init__(self, game, id, playerName, time, scarabs, roundsWon):
    self.game = game
    self.id = id
    self.playerName = playerName
    self.time = time
    self.scarabs = scarabs
    self.roundsWon = roundsWon
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.playerName, self.time, self.scarabs, self.roundsWon, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, playerName = self.playerName, time = self.time, scarabs = self.scarabs, roundsWon = self.roundsWon, )
  
  def nextTurn(self):
    pass

  def placeTrap(self, x, y, trapType):
    tile = self.game.getTile(x, y)
    if not tile:
      return "You cannot place a trap outside of the map."
    if tile.type == 1:
      return "You cannot place a trap on a spawn point"
    if tile.type == 2:
      return "You cannot place a trap on a wall"
      
    if len(self.game.grid[x][y]) > 1:
      return "You cannot place a trap on a trap"
    if self.game.turnNumber > 1:
      return "You cannot place traps after the first turn"

    trap = self.game.addObject(Trap)
    self.game.grid[x][y].append(trap)

  def purchaseThief(self, x, y, thiefType):
    realX = self.game.getRealX(self.id, x, 1)
    thiefCount = 0
    if x < 0 or x >= self.game.mapWidth /2 or y < 0 or y >= self.game.mapHeight:
      return 'Turn {}: You cannot place a thief out of bounds. ({}, {})'.format(self.game.turnNumber, x, y)
    tile = self.game.getTile(realX, y)
    if tile.type != 1:
      return 'Turn {}: You can only spawn thieves on spawn tiles. ({}, {})'.format(self.game.turnNumber, x, y)
    if thiefType < 0 or thiefType >= len(self.game.objects.thiefTypes):
      return 'Turn {}: You cannot spawn thieves of this type. ({}, {})'.format(self.game.turnNumber, x, y)
    type = self.game.objects.thiefTypes[thiefType]
    for thief in self.game.thieves:
      if thief.owner == self.id and thief.type == thiefType:
          thiefCount += 1
    if thiefCount >= type.maxInstances:
      return 'Turn {}: You cannot buy any more of this type of thief. ({}, {})'.format(self.game.turnNumber, x, y)
    if self.scarabs < type.cost:
      return 'Turn {}: You do not have enough scarabs to buy this thief. ({}, {})'.format(self.game.turnNumber, x, y)

    self.scarabs -= type.cost
    # 'id', 'x', 'y', 'owner', 'thiefType', 'alive', 'ninjaReflexesLeft', 'maxNinjaReflexes', 'movementLeft', 'maxMovement', 'frozenTurnsLeft'
    newThiefStats = [realX, y, self.id, thiefType, 1, type.maxNinjaReflexes, type.maxNinjaReflexes, type.maxMovement, type.maxMovement, 0]
    newThief = self.game.addObject(Thief, newThiefStats)
    self.game.grid[newThief.x][newThief.y].append(newThief)

    self.game.addAnimation(SpawnAnimation(self.id, realX, y))

    return True
	
  def pharaohTalk(self, message):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Mappable(object):
  game_state_attributes = ['id', 'x', 'y']
  def __init__(self, game, id, x, y):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.x, self.y, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Tile(Mappable):
  game_state_attributes = ['id', 'x', 'y', 'type']
  def __init__(self, game, id, x, y, type):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.type = type
    self.updatedAt = game.turnNumber
    self.unit = None

  def toList(self):
    return [self.id, self.x, self.y, self.type, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, type = self.type, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Trap(Mappable):
  game_state_attributes = ['id', 'x', 'y', 'owner', 'trapType', 'visible', 'active', 'bodyCount']
  def __init__(self, game, id, x, y, owner, trapType, visible, active, bodyCount):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.owner = owner
    self.trapType = trapType
    self.visible = visible
    self.active = active
    self.bodyCount = bodyCount
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.trapType, self.visible, self.active, self.bodyCount, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, trapType = self.trapType, visible = self.visible, active = self.active, bodyCount = self.bodyCount, )
  
  def nextTurn(self):
    pass

  def act(self, x, y):
    pass

  def toggle(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Thief(Mappable):
  game_state_attributes = ['id', 'x', 'y', 'owner', 'thiefType', 'alive', 'ninjaReflexesLeft', 'maxNinjaReflexes', 'movementLeft', 'maxMovement', 'frozenTurnsLeft']
  def __init__(self, game, id, x, y, owner, thiefType, alive, ninjaReflexesLeft, maxNinjaReflexes, movementLeft, maxMovement, frozenTurnsLeft):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.owner = owner
    self.thiefType = thiefType
    self.alive = alive
    self.ninjaReflexesLeft = ninjaReflexesLeft
    self.maxNinjaReflexes = maxNinjaReflexes
    self.movementLeft = movementLeft
    self.maxMovement = maxMovement
    self.frozenTurnsLeft = frozenTurnsLeft
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.thiefType, self.alive, self.ninjaReflexesLeft, self.maxNinjaReflexes, self.movementLeft, self.maxMovement, self.frozenTurnsLeft, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, thiefType = self.thiefType, alive = self.alive, ninjaReflexesLeft = self.ninjaReflexesLeft, maxNinjaReflexes = self.maxNinjaReflexes, movementLeft = self.movementLeft, maxMovement = self.maxMovement, frozenTurnsLeft = self.frozenTurnsLeft, )
  
  def nextTurn(self):
    pass

  def thiefTalk(self, message):
    pass

  def move(self, x, y):
    if self.owner != self.game.playerID:
      return 'Turn {}: You cannot use the other player\'s thief {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    elif self.movementLeft <= 0:
      return 'Turn {}: Your thief {} does not have any movement left. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    elif not ((self.game.mapWidth / 2) * self.game.playerID^1 <= x < (self.game.mapWidth / 2) + (self.game.mapWidth / 2) * self.game.playerID^1) or not (0 <= y < self.game.mapHeight):
      return 'Turn {}: Your thief {} cannot move off its side of the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    elif self.game.getTile(x, y).type == 2:
      return 'Turn {}: Your thief {} is trying to run into a wall. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    elif abs(self.x-x) + abs(self.y-y) != 1:
      return 'Turn {}: Your thief {} can only move one unit away. ({}.{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

    self.game.grid[self.x][self.y].remove(self)

    self.game.addAnimation(MoveAnimation(self.id,self.x,self.y,x,y))
    self.x = x
    self.y = y
    self.movementLeft -= 1
    self.game.grid[self.x][self.y].append(self)
    
    #TODO: Figure out trap activation
    for unit in self.game.grid[x][y]:             
      if isinstance(unit, Trap) and unit.active:
        unit.act(x, y)
    self.actionsLeft = 0
    return True

  def act(self, x, y):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class ThiefType(object):
  game_state_attributes = ['id', 'name', 'type', 'cost', 'maxMovement', 'maxNinjaReflexes', 'maxInstances']
  def __init__(self, game, id, name, type, cost, maxMovement, maxNinjaReflexes, maxInstances):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.maxMovement = maxMovement
    self.maxNinjaReflexes = maxNinjaReflexes
    self.maxInstances = maxInstances
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.maxMovement, self.maxNinjaReflexes, self.maxInstances, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, maxMovement = self.maxMovement, maxNinjaReflexes = self.maxNinjaReflexes, maxInstances = self.maxInstances, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class TrapType(object):
  game_state_attributes = ['id', 'name', 'type', 'cost', 'startsVisible', 'hasAction', 'activatable', 'maxBodyCount', 'maxInstances', 'killsOnWalkThrough', 'turnsToKillOnTile', 'canPlaceInWalls', 'canPlaceInEmptyTiles', 'freezesForTurns']
  def __init__(self, game, id, name, type, cost, startsVisible, hasAction, activatable, maxBodyCount, maxInstances, killsOnWalkThrough, turnsToKillOnTile, canPlaceInWalls, canPlaceInEmptyTiles, freezesForTurns):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.startsVisible = startsVisible
    self.hasAction = hasAction
    self.activatable = activatable
    self.maxBodyCount = maxBodyCount
    self.maxInstances = maxInstances
    self.killsOnWalkThrough = killsOnWalkThrough
    self.turnsToKillOnTile = turnsToKillOnTile
    self.canPlaceInWalls = canPlaceInWalls
    self.canPlaceInEmptyTiles = canPlaceInEmptyTiles
    self.freezesForTurns = freezesForTurns
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.startsVisible, self.hasAction, self.activatable, self.maxBodyCount, self.maxInstances, self.killsOnWalkThrough, self.turnsToKillOnTile, self.canPlaceInWalls, self.canPlaceInEmptyTiles, self.freezesForTurns, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, startsVisible = self.startsVisible, hasAction = self.hasAction, activatable = self.activatable, maxBodyCount = self.maxBodyCount, maxInstances = self.maxInstances, killsOnWalkThrough = self.killsOnWalkThrough, turnsToKillOnTile = self.turnsToKillOnTile, canPlaceInWalls = self.canPlaceInWalls, canPlaceInEmptyTiles = self.canPlaceInEmptyTiles, freezesForTurns = self.freezesForTurns, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)


# The following are animations and do not need to have any logic added
class SpawnAnimation:
  def __init__(self, actingID, x, y):
    self.actingID = actingID
    self.x = x
    self.y = y

  def toList(self):
    return ["spawn", self.actingID, self.x, self.y, ]

  def toJson(self):
    return dict(type = "spawn", actingID = self.actingID, x = self.x, y = self.y)

class MoveAnimation:
  def __init__(self, actingID, fromX, fromY, toX, toY):
    self.actingID = actingID
    self.fromX = fromX
    self.fromY = fromY
    self.toX = toX
    self.toY = toY

  def toList(self):
    return ["move", self.actingID, self.fromX, self.fromY, self.toX, self.toY, ]

  def toJson(self):
    return dict(type = "move", actingID = self.actingID, fromX = self.fromX, fromY = self.fromY, toX = self.toX, toY = self.toY)

class KillAnimation:
  def __init__(self, actingID, targetID):
    self.actingID = actingID
    self.targetID = targetID

  def toList(self):
    return ["kill", self.actingID, self.targetID, ]

  def toJson(self):
    return dict(type = "kill", actingID = self.actingID, targetID = self.targetID)

class PharaohTalkAnimation:
  def __init__(self, actingID, message):
    self.actingID = actingID
    self.message = message

  def toList(self):
    return ["pharaohTalk", self.actingID, self.message, ]

  def toJson(self):
    return dict(type = "pharaohTalk", actingID = self.actingID, message = self.message)

class ThiefTalkAnimation:
  def __init__(self, actingID, message):
    self.actingID = actingID
    self.message = message

  def toList(self):
    return ["thiefTalk", self.actingID, self.message, ]

  def toJson(self):
    return dict(type = "thiefTalk", actingID = self.actingID, message = self.message)

class ActivateAnimation:
  def __init__(self, actingID):
    self.actingID = actingID

  def toList(self):
    return ["activate", self.actingID, ]

  def toJson(self):
    return dict(type = "activate", actingID = self.actingID)

class BombAnimation:
  def __init__(self, actingID, x, y):
    self.actingID = actingID
    self.x = x
    self.y = y

  def toList(self):
    return ["bomb", self.actingID, self.x, self.y, ]

  def toJson(self):
    return dict(type = "bomb", actingID = self.actingID, x = self.x, y = self.y)

