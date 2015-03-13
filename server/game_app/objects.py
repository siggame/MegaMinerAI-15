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

  def placeTrap(self, x, y, trapTypeIndex):
    realX = self.game.getRealX(self.id, x, 0)
    tile = self.game.getTile(realX, y)

    if self.game.roundTurnNumber > 1:
      return "You cannot place traps after the first turn"
    if not tile:
      return "Turn {}: You cannot place a trap outside of the map. ({}, {})".format(self.game.turnNumber, x, y)
    if tile.type == 1:
      return "Turn {}: You cannot place a trap on a spawn point ({}, {})".format(self.game.turnNumber, x, y)
    if len(self.game.grid[x][y]) > 1:
      return "Turn {}: You cannot place a trap on a trap ({}, {})".format(self.game.turnNumber, x, y)
    if trapTypeIndex < 0 or trapTypeIndex >= len(self.game.objects.trapTypes):
      return "Turn {}: You cannot spawn traps of this type. (given: {})".format(self.game.turnNumber, trapTypeIndex)

    trapType = self.game.objects.trapTypes[trapTypeIndex]
    if tile.type == self.game.wall and not trapType.canPlaceOnWalls:
      return "Turn {}: You cannot place this trap on a wall ({}, {})".format(self.game.turnNumber, x, y)
    if tile.type == self.game.empty and not trapType.canPlaceOnOpenTiles:
      return "Turn {}: You cannot place this trap on an empty tile ({}, {})".format(self.game.turnNumber, x, y)

    if trapTypeIndex != self.game.sarcohpagus:
      trapCount = sum(1 for trap in self.game.traps if trap.owner == self.id and trap.type == trapTypeIndex)
      if trapCount >= trapType.maxInstances:
        return "Turn {}: You cannot buy any more of this type of trap (type: {}, have: {})".format(self.game.turnNumber, trapTypeIndex, trapCount)
    if self.scarabs < trapType.cost:
      return "Turn {}: You do not have enough scarabs to buy this trap (have: {}, cost: {})".format(self.game.turnNumber, self.scarabs, trapType.cost)

    self.scarabs -= trapType.cost

    # Move sarcophagus
    if trapTypeIndex == self.game.sarcohpagus:
      sarcophagus = next(trap for trap in self.game.traps if trap.type == self.game.sarcohpagus and trap.owner == self.id)
      self.game.grid[sarcophagus.x][sarcophagus.y].remove(sarcophagus)
      self.game.grid[realX][y].append(sarcophagus)
    else: # Create new trap
      # ['id', 'x', 'y', 'owner', 'trapType', 'visible', 'active', 'bodyCount', 'activationsRemaining', 'turnsTillActive']
      newTrapStats = [realX, y, self.id, trapTypeIndex, trapType.startsVisible, 1, 0, trapType.maxActivations, 0]
      newTrap = self.game.addObject(Trap, newTrapStats)
      self.game.grid[newTrap.x][newTrap.y].append(newTrap)
      self.game.addAnimation(SpawnAnimation(self.id, realX, y))

    return True

  def purchaseThief(self, x, y, thiefType):
    realX = self.game.getRealX(self.id, x, 1)

    if self.game.roundTurnNumber < 2:
      return "You cannot place thieves on the first turn"
    if x < 0 or x >= self.game.mapWidth / 2 or y < 0 or y >= self.game.mapHeight:
      return 'Turn {}: You cannot place a thief out of bounds. ({}, {})'.format(self.game.turnNumber, x, y)
    tile = self.game.getTile(realX, y)
    if tile.type != 1:
      return 'Turn {}: You can only spawn thieves on spawn tiles. ({}, {})'.format(self.game.turnNumber, x, y)
    if thiefType < 0 or thiefType >= len(self.game.objects.thiefTypes):
      return 'Turn {}: You cannot spawn thieves of this type. (given: {})'.format(self.game.turnNumber, thiefType)
    type = self.game.objects.thiefTypes[thiefType]

    if self.scarabs < type.cost:
      return 'Turn {}: You do not have enough scarabs to buy this thief. (have: {}, cost: {})'.format(self.game.turnNumber, self.scarabs, type.cost)

    thiefCount = sum(1 for thief in self.game.thiefs if thief.owner == self.id and thief.type == thiefType)
    if thiefCount >= type.maxInstances:
      return 'Turn {}: You cannot buy any more of this type of thief. (type: {}, have: {})'.format(self.game.turnNumber, thiefType, thiefCount)

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
  game_state_attributes = ['id', 'x', 'y', 'owner', 'trapType', 'visible', 'active', 'bodyCount', 'activationsRemaining', 'turnsTillActive']
  def __init__(self, game, id, x, y, owner, trapType, visible, active, bodyCount, activationsRemaining, turnsTillActive):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.owner = owner
    self.trapType = trapType
    self.visible = visible
    self.active = active
    self.bodyCount = bodyCount
    self.activationsRemaining = activationsRemaining
    self.turnsTillActive = turnsTillActive
    self.updatedAt = game.turnNumber

    self.standingThieves = dict()
    """:type : dict[Thief, int]"""

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.trapType, self.visible, self.active, self.bodyCount, self.activationsRemaining, self.turnsTillActive, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, trapType = self.trapType, visible = self.visible, active = self.active, bodyCount = self.bodyCount, activationsRemaining = self.activationsRemaining, turnsTillActive = self.turnsTillActive, )

  def activate(self):
    self.activationsRemaining -= 1
    if self.activationsRemaining <= 0:
      self.active = 0
    elif self.game.trapTypes[self.trapType].cooldown:
      self.active = 0
      self.turnsTillActive = self.game.trapTypes[self.trapType].cooldown
    self.visible = 1

  def attack(self, thief):
    if thief.alive:
      if thief.ninjaReflexesLeft <= 0:
        if self.game.objects.trapTypes[self.trapType].killsOnActivate:
          thief.alive = 0
          self.bodyCount += 1
        if self.game.objects.trapTypes[self.trapType].freezesForTurns:
          thief.frozenTurnsLeft = self.game.objects.trapTypes[self.trapType].freezesForTurns
      else:
        thief.ninjaReflexesLeft -= 1

  def nextTurn(self):
    if self.turnsTillActive > 0:
      self.turnsTillActive -= 1
      if self.turnsTillActive == 0:
        self.active = True

    if self.active:
      trapType = self.game.objects.trapTypes[self.trapType]
      if trapType.turnsToActivateOnTile:
        # Find thieves
        thieves = [unit for unit in self.game.grid[self.x][self.y] if isinstance(unit, Thief)]
        # Forget thieves who moved off
        self.standingThieves = {thief: turns for thief, turns in self.standingThieves if thief in thieves}
        # Increase counter for thieves
        activated = False
        for thief in thieves:
          if thief not in self.standingThieves:
            self.standingThieves[thief] = 0
          self.standingThieves[thief] += 1
          if self.standingThieves[thief] >= trapType.turnsToActivateOnTile:
            activated = True
            self.attack(thief)
        if activated:
          self.activate()

      return True

  def act(self, x, y):
    if self.owner != self.game.playerID:
      return 'Turn {}: You cannot use the other player\'s trap {}. ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y)
    if not self.game.objects.trapTypes[self.trapType].hasAction:
      return 'Turn {}: Trap type {} does not have an action.'.format(self.game.turnNumber, self.trapType)
    if self.activationsRemaining <= 0:
      return 'Turn {}: Trap ({}) has no activations remaining.'.format(self.game.turnNumber, self.id)
    if self.turnsTillActive > 0:
      return 'Turn {}: Trap ({}) must wait {} turns to act again.'.format(self.game.turnNumber, self.id, self.turnsTillActive)
    if not self.active:
      return 'Turn {}: You cannot use this trap ({}) because it is not active.'.format(self.game.turnNumber, self.id)

    if self.trapType == self.game.boulder:
      if abs(x) + abs(y) != 1:
        return 'Turn {}: Invalid rolling direction for boulder {}. ({}, {})'.format(self.game.turnNumber, self.id, x, y)

      # Kill thieves as boulder rolls over them, until boulder runs into a wall
      boulderX, boulderY = self.x, self.y
      while self.game.grid[boulderX][boulderY][0].type == self.game.empty:
        for unit in self.game.grid[boulderX][boulderY]:
          if isinstance(unit, Thief):
            self.attack(unit)
        boulderX += x
        boulderY += y
    # Move mummy and kill thieves
    elif self.trapType == self.game.mummy:
      realX = self.game.getRealX(self.owner, x, 0)
      # Check if desired space is adjacent to mummy's current space
      if abs(realX - self.x) + abs(y - self.y) != 1:
        return 'Turn {}: Cannot move mummy {} to non-adjacent space. ({}, {}) -> ({}, [})'.format(self.game.turnNumber, self.id, self.game.getUserX(self.owner, self.x, 0), self.y, x, y)
      # Move trap (mummy)
      self.game.grid[self.x][self.y].remove(self)
      self.x, self.y = realX, y
      self.game.grid[self.x][self.y].append(self)
      # Kill thieves
      for unit in self.game.grid[self.x][self.y]:
        if isinstance(unit, Thief):
          self.attack(unit)

    # General trap logic
    self.activate()

    return True

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
    userX = self.game.getUserX(self.owner, self.x, 1)
    realX = self.game.getRealX(self.owner, x, 1)
    if self.owner != self.game.playerID:
      return 'Turn {}: You cannot use the other player\'s thief {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)
    if not self.alive:
      return 'Turn {}: You cannot move a dead thief {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)
    if self.frozenTurnsLeft > 0:
      return 'Turn {}: You cannot move a thief {} that is frozen for {} turns. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.frozenTurnsLeft, userX, self.y, x, y)
    if self.movementLeft <= 0:
      return 'Turn {}: Your thief {} does not have any movement left. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)
    if not (0 <= x < self.game.mapWidth / 2) or not (0 <= y < self.game.mapHeight):
      return 'Turn {}: Your thief {} cannot move off its side of the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)
    if self.game.getTile(x, y).type == self.game.wall:
      return 'Turn {}: Your thief {} is trying to run into a wall. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)
    if abs(self.x - realX) + abs(self.y - y) != 1:
      return 'Turn {}: Your thief {} can only move one unit away. ({}.{}) -> ({},{})'.format(self.game.turnNumber, self.id, userX, self.y, x, y)

    trap = next((trap for trap in self.game.grid[self.x][self.y] if isinstance(trap, Trap) and trap.active and self.game.objects.trapTypes[trap.trapType].activatesOnWalkThrough), None)

    if trap and self.movementLeft < self.maxMovement:
      trap.attack(self)
      trap.activate()

    blockingTrap = next((trap for trap in self.game.grid[realX][y] if isinstance(trap, Trap) and trap.active and self.game.objects.trapTypes[trap.trapType].unpassable), None)

    if blockingTrap:
      blockingTrap.activate()

    if self.alive and not blockingTrap:
      self.game.grid[self.x][self.y].remove(self)
      self.x, self.y = realX, y
      self.game.grid[self.x][self.y].append(self)
      self.movementLeft -= 1
      self.game.addAnimation(MoveAnimation(self.id, self.x, self.y, realX, y))

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
  game_state_attributes = ['id', 'name', 'type', 'cost', 'maxInstances', 'startsVisible', 'hasAction', 'deactivatable', 'maxActivations', 'activatesOnWalkedThrough', 'turnsToActivateOnTile', 'canPlaceOnWalls', 'canPlaceOnOpenTiles', 'freezesForTurns', 'killsOnActivate', 'cooldown', 'explosive', 'unpassable']
  def __init__(self, game, id, name, type, cost, maxInstances, startsVisible, hasAction, deactivatable, maxActivations, activatesOnWalkedThrough, turnsToActivateOnTile, canPlaceOnWalls, canPlaceOnOpenTiles, freezesForTurns, killsOnActivate, cooldown, explosive, unpassable):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.maxInstances = maxInstances
    self.startsVisible = startsVisible
    self.hasAction = hasAction
    self.deactivatable = deactivatable
    self.maxActivations = maxActivations
    self.activatesOnWalkedThrough = activatesOnWalkedThrough
    self.turnsToActivateOnTile = turnsToActivateOnTile
    self.canPlaceOnWalls = canPlaceOnWalls
    self.canPlaceOnOpenTiles = canPlaceOnOpenTiles
    self.freezesForTurns = freezesForTurns
    self.killsOnActivate = killsOnActivate
    self.cooldown = cooldown
    self.explosive = explosive
    self.unpassable = unpassable
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.maxInstances, self.startsVisible, self.hasAction, self.deactivatable, self.maxActivations, self.activatesOnWalkedThrough, self.turnsToActivateOnTile, self.canPlaceOnWalls, self.canPlaceOnOpenTiles, self.freezesForTurns, self.killsOnActivate, self.cooldown, self.explosive, self.unpassable, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, maxInstances = self.maxInstances, startsVisible = self.startsVisible, hasAction = self.hasAction, deactivatable = self.deactivatable, maxActivations = self.maxActivations, activatesOnWalkedThrough = self.activatesOnWalkedThrough, turnsToActivateOnTile = self.turnsToActivateOnTile, canPlaceOnWalls = self.canPlaceOnWalls, canPlaceOnOpenTiles = self.canPlaceOnOpenTiles, freezesForTurns = self.freezesForTurns, killsOnActivate = self.killsOnActivate, cooldown = self.cooldown, explosive = self.explosive, unpassable = self.unpassable, )
  
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

