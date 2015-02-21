class Player(object):
  game_state_attributes = ['id', 'playerName', 'time', 'scarabs']
  def __init__(self, game, id, playerName, time, scarabs):
    self.game = game
    self.id = id
    self.playerName = playerName
    self.time = time
    self.scarabs = scarabs
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.playerName, self.time, self.scarabs, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, playerName = self.playerName, time = self.time, scarabs = self.scarabs, )
  
  def nextTurn(self):
    pass

  def placeTrap(self, x, y, trapType):
    pass

  def purchaseThief(self, x, y, thiefType):
    pass

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

class Tile(object):
  game_state_attributes = ['id', 'isWall']
  def __init__(self, game, id, isWall):
    self.game = game
    self.id = id
    self.isWall = isWall
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.isWall, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, isWall = self.isWall, )
  
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
  game_state_attributes = ['id', 'x', 'y', 'owner', 'thiefType', 'alive', 'actionsLeft', 'maxActions', 'movementLeft', 'maxMovement']
  def __init__(self, game, id, x, y, owner, thiefType, alive, actionsLeft, maxActions, movementLeft, maxMovement):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.owner = owner
    self.thiefType = thiefType
    self.alive = alive
    self.actionsLeft = actionsLeft
    self.maxActions = maxActions
    self.movementLeft = movementLeft
    self.maxMovement = maxMovement
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.thiefType, self.alive, self.actionsLeft, self.maxActions, self.movementLeft, self.maxMovement, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, thiefType = self.thiefType, alive = self.alive, actionsLeft = self.actionsLeft, maxActions = self.maxActions, movementLeft = self.movementLeft, maxMovement = self.maxMovement, )
  
  def nextTurn(self):
    pass

  def thiefTalk(self, message):
    pass

  def move(self, x, y):
    pass

  def act(self, x, y):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class ThiefType(object):
  game_state_attributes = ['id', 'name', 'type', 'cost', 'maxActions', 'maxMovement', 'maxInstances']
  def __init__(self, game, id, name, type, cost, maxActions, maxMovement, maxInstances):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.maxActions = maxActions
    self.maxMovement = maxMovement
    self.maxInstances = maxInstances
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.maxActions, self.maxMovement, self.maxInstances, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, maxActions = self.maxActions, maxMovement = self.maxMovement, maxInstances = self.maxInstances, )
  
  def nextTurn(self):
    pass

  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class TrapType(object):
  game_state_attributes = ['id', 'name', 'type', 'cost', 'startsVisible', 'hasAction']
  def __init__(self, game, id, name, type, cost, startsVisible, hasAction):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.startsVisible = startsVisible
    self.hasAction = hasAction
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.startsVisible, self.hasAction, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, startsVisible = self.startsVisible, hasAction = self.hasAction, )
  
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

