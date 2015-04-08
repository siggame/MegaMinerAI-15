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
    if self.game.roundTurnNumber in [0, 1]:
      self.scarabs = self.game.scarabsForTraps
    if self.game.roundTurnNumber in [2, 3]:
      self.scarabs = self.game.scarabsForThieves

  def placeTrap(self, x, y, trapTypeIndex):
    if self.game.roundTurnNumber > 1:
      return "You cannot place traps after the first turn"
    tile = self.game.getTile(x, y)
    if not tile:
      return "Turn {}: You cannot place a trap outside of the map. ({}, {})".format(self.game.turnNumber, x, y)
    if not (self.id * (self.game.mapWidth / 2) < x < (1 + self.id) * (self.game.mapWidth / 2)):
      return "Turn {}: You cannot place a trap outside of your pyramid. ({}, {})".format(self.game.turnNumber, x, y)
    if tile.type == self.game.spawn:
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

    if trapTypeIndex != self.game.sarcophagus:
      trapCount = sum(1 for trap in self.game.objects.traps if trap.owner == self.id and trap.trapType == trapTypeIndex)
      if trapCount >= trapType.maxInstances:
        return "Turn {}: You cannot buy any more of this type of trap (type: {}, have: {})".format(self.game.turnNumber, trapTypeIndex, trapCount)
    if self.scarabs < trapType.cost:
      return "Turn {}: You do not have enough scarabs to buy this trap (have: {}, cost: {})".format(self.game.turnNumber, self.scarabs, trapType.cost)

    self.scarabs -= trapType.cost

    # Move sarcophagus
    if trapTypeIndex == self.game.sarcophagus:
      sarcophagus = next(trap for trap in self.game.objects.traps if trap.trapType == self.game.sarcophagus and trap.owner == self.id)
      self.game.grid[sarcophagus.x][sarcophagus.y].remove(sarcophagus)
      sarcophagus.x, sarcophagus.y = x, y
      self.game.grid[sarcophagus.x][sarcophagus.y].append(sarcophagus)
    else: # Create new trap
      # ['id', 'x', 'y', 'owner', 'trapType', 'visible', 'active', 'bodyCount', 'activationsRemaining', 'turnsTillActive']
      newTrapStats = [x, y, self.id, trapTypeIndex, trapType.startsVisible, 1, 0, trapType.maxActivations, 0]
      newTrap = self.game.addObject(Trap, newTrapStats)
      self.game.grid[newTrap.x][newTrap.y].append(newTrap)
      self.game.addAnimation(SpawnAnimation(self.id, x, y))

    return True

  def purchaseThief(self, x, y, thiefType):
    if self.game.roundTurnNumber < 2:
      return "You cannot place thieves on the first turn"
    tile = self.game.getTile(x, y)
    if not tile:
      return 'Turn {}: You cannot place a thief outside of the map. ({}, {})'.format(self.game.turnNumber, x, y)
    if not (0 <= x - (self.id ^ 1) * (self.game.mapWidth / 2) < self.game.mapWidth / 2):
      return "Turn {}: You cannot place a thief inside of your own pyramid. ({}, {}) {}".format(self.game.turnNumber, x, y, self.id)
    if tile.type != self.game.spawn:
      return 'Turn {}: You can only spawn thieves on spawn tiles. ({}, {})'.format(self.game.turnNumber, x, y)
    if thiefType < 0 or thiefType >= len(self.game.objects.thiefTypes):
      return 'Turn {}: You cannot spawn thieves of this type. (given: {})'.format(self.game.turnNumber, thiefType)
    type = self.game.objects.thiefTypes[thiefType]

    if self.scarabs < type.cost:
      return 'Turn {}: You do not have enough scarabs to buy this thief. (have: {}, cost: {})'.format(self.game.turnNumber, self.scarabs, type.cost)

    thiefCount = sum(1 for thief in self.game.objects.thiefs if thief.owner == self.id and thief.thiefType == thiefType)
    if thiefCount >= type.maxInstances:
      return 'Turn {}: You cannot buy any more of this type of thief. (type: {}, have: {})'.format(self.game.turnNumber, thiefType, thiefCount)

    self.scarabs -= type.cost
    # ['id', 'x', 'y', 'owner', 'thiefType', 'alive', 'specialsLeft', 'maxSpecials', 'movementLeft', 'maxMovement', 'frozenTurnsLeft']
    newThiefStats = [x, y, self.id, thiefType, 1, type.maxSpecials, type.maxSpecials, type.maxMovement, type.maxMovement, 0]
    newThief = self.game.addObject(Thief, newThiefStats)
    self.game.grid[newThief.x][newThief.y].append(newThief)

    self.game.addAnimation(SpawnAnimation(self.id, x, y))

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
    self.movementLeft = 1

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.trapType, self.visible, self.active, self.bodyCount, self.activationsRemaining, self.turnsTillActive, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, trapType = self.trapType, visible = self.visible, active = self.active, bodyCount = self.bodyCount, activationsRemaining = self.activationsRemaining, turnsTillActive = self.turnsTillActive, )

  def activate(self):
    self.activationsRemaining -= 1
    if self.activationsRemaining == 0:
      self.active = 0
    elif self.game.objects.trapTypes[self.trapType].cooldown:
      self.active = 0
      self.turnsTillActive = self.game.objects.trapTypes[self.trapType].cooldown
    self.visible = 1

  def attack(self, thief):
    if thief.alive and self.active:
      if thief.thiefType != self.game.ninja or thief.specialsLeft <= 0:
        if self.game.objects.trapTypes[self.trapType].killsOnActivate:
          thief.alive = 0
          thief.frozenTurnsLeft = 0
          self.bodyCount += 1
          if not self.visible:
            thief.hidden = True
        if self.game.objects.trapTypes[self.trapType].freezesForTurns:
          thief.frozenTurnsLeft = self.game.objects.trapTypes[self.trapType].freezesForTurns
          if not self.visible:
            thief.hidden = True
      elif thief.thiefType == self.game.ninja:
        thief.specialsLeft -= 1

  def nextTurn(self):
    trapType = self.game.objects.trapTypes[self.trapType]

    if self.game.playerID == self.owner:
      if self.turnsTillActive > 0:
        self.turnsTillActive -= 1
        if self.turnsTillActive == 0:
          self.active = 1

      # swinging blade
      elif self.trapType == self.game.swingingBlade:
        self.active = self.active ^ 1

      if self.trapType == self.game.mummy:
        self.movementLeft = 1

      elif trapType.turnsToActivateOnTile:
        # Find thieves
        thieves = [unit for unit in self.game.grid[self.x][self.y] if isinstance(unit, Thief)]
        # Forget thieves who moved off
        self.standingThieves = {thief: turns for thief, turns in self.standingThieves.iteritems() if thief in thieves}
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
      # Check if desired space is adjacent to mummy's current space
      if abs(x - self.x) + abs(y - self.y) != 1:
        return 'Turn {}: Cannot move mummy {} to non-adjacent space. ({}, {}) -> ({}, {})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      # Check if desired space is within grid
      if not (0 <= x - (self.game.mapWidth/2) * (self.owner) < self.game.mapWidth/2) or not (0 <= y < self.game.mapHeight):
        return 'Turn {}: Cannot move mummy {} outside of grid ({}, {}) -> ({}, {})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      # Check if desired space is not a wall
      if self.game.grid[x][y].type != self.game.empty:
        return 'Turn {}: Cannot move mummy {} into a wall or spawn. ({}, {}) -> ({}, {})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      # Check if the mummy still has moves left
      if self.movementLeft <= 0:
        return 'Turn {}: Mummy {} can only move once per turn. ({}, {}) -> ({}, {})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      
      # Move trap (mummy)
      self.game.grid[self.x][self.y].remove(self)
      self.x, self.y = x, y
      self.game.grid[self.x][self.y].append(self)
      self.movementLeft -= 1
      # Kill thieves
      for unit in self.game.grid[self.x][self.y]:
        if isinstance(unit, Thief):
          self.attack(unit)

    # General trap logic
    self.activate()

    return True

  def toggle(self):
    if not self.game.objects.trapTypes[self.trapType].deactivatable:
      return 'Turn {}: Cannot toggle trap {} that is not deactivatable'.format(self.game.turnNumber, self.id)
    if self.active:
      self.active = 0
    elif self.activationsRemaining and self.turnsTillActive == 0:
      self.active = 1

    return True


  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class Thief(Mappable):
  game_state_attributes = ['id', 'x', 'y', 'owner', 'thiefType', 'alive', 'specialsLeft', 'maxSpecials', 'movementLeft', 'maxMovement', 'frozenTurnsLeft']
  def __init__(self, game, id, x, y, owner, thiefType, alive, specialsLeft, maxSpecials, movementLeft, maxMovement, frozenTurnsLeft):
    self.game = game
    self.id = id
    self.x = x
    self.y = y
    self.owner = owner
    self.thiefType = thiefType
    self.alive = alive
    self.specialsLeft = specialsLeft
    self.maxSpecials = maxSpecials
    self.movementLeft = movementLeft
    self.maxMovement = maxMovement
    self.frozenTurnsLeft = frozenTurnsLeft
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.x, self.y, self.owner, self.thiefType, self.alive, self.specialsLeft, self.maxSpecials, self.movementLeft, self.maxMovement, self.frozenTurnsLeft, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, x = self.x, y = self.y, owner = self.owner, thiefType = self.thiefType, alive = self.alive, specialsLeft = self.specialsLeft, maxSpecials = self.maxSpecials, movementLeft = self.movementLeft, maxMovement = self.maxMovement, frozenTurnsLeft = self.frozenTurnsLeft, )
  
  def nextTurn(self):
    if self.game.playerID == self.owner:
      if self.thiefType == 3:
        xchange = [-1, 1, 0,  0]
        ychange = [ 0, 0, 1, -1]
        for i in range(4):
          if 0 <= self.x + xchange[i] < self.game.mapWidth and 0 <= self.y + ychange[i] < self.game.mapHeight:
            for obj in self.game.grid[self.x + xchange[i]][self.y + ychange[i]]:
              if isinstance(obj, Trap):
                obj.visible = 1
      self.hidden = False
      if self.alive:
        if self.frozenTurnsLeft > 0:
          self.frozenTurnsLeft -= 1
        if self.frozenTurnsLeft == 0:
          self.movementLeft = self.maxMovement

    return True

  def thiefTalk(self, message):
    pass

  def move(self, x, y):
    if self.owner != self.game.playerID:
      return 'Turn {}: You cannot use the other player\'s thief {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    if not self.alive:
      if self.hidden:
        return True
      else:
        return 'Turn {}: You cannot move a dead thief {}. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    if self.frozenTurnsLeft > 0:
      if self.hidden:
        return True
      else:
        return 'Turn {}: You cannot move a thief {} that is frozen for {} turns. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.frozenTurnsLeft, self.x, self.y, x, y)
    if self.movementLeft <= 0:
      return 'Turn {}: Your thief {} does not have any movement left. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    if not (0 <= x - (self.game.mapWidth / 2) * (self.owner ^ 1) < self.game.mapWidth / 2) or not (0 <= y < self.game.mapHeight):
      return 'Turn {}: Your thief {} cannot move off its side of the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    if self.game.getTile(x, y).type == self.game.wall:
      return 'Turn {}: Your thief {} is trying to run into a wall. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
    if abs(self.x - x) + abs(self.y - y) != 1:
      return 'Turn {}: Your thief {} can only move one unit away. ({}.{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

    # Only check for activatesOnWalkedThrough traps when thief moves off of them and not on the thief's first move
    if self.movementLeft < self.maxMovement:
      backstabTrap = next((trap for trap in self.game.grid[self.x][self.y] if isinstance(trap, Trap) and
                           trap.active and self.game.objects.trapTypes[trap.trapType].activatesOnWalkedThrough), None)
      if backstabTrap:
        backstabTrap.attack(self)
        backstabTrap.activate()

    blockingTrap = next((trap for trap in self.game.grid[x][y] if isinstance(trap, Trap) and trap.active and
                         self.game.objects.trapTypes[trap.trapType].unpassable), None)

    if blockingTrap:
      blockingTrap.activate()

    if self.alive and not blockingTrap:
      self.game.grid[self.x][self.y].remove(self)
      self.x, self.y = x, y
      self.game.grid[self.x][self.y].append(self)
      self.movementLeft -= 1
      self.game.addAnimation(MoveAnimation(self.id, self.x, self.y, x, y))

      instaTrap = next((trap for trap in self.game.grid[x][y] if isinstance(trap, Trap) and trap.active and
                        self.game.objects.trapTypes[trap.trapType].activatesOnWalkedThrough and
                        self.game.objects.trapTypes[trap.trapType].turnsToActivateOnTile == 1), None)

      if instaTrap:
        instaTrap.attack(self)
        instaTrap.activate()

    return True

  def act(self, x, y):
    if self.owner != self.game.playerID:
      return 'Turn {}: You cannot use the other player\'s thief {}. ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y)
    if (self.thiefType != self.game.bomber) and (self.thiefType != self.game.digger):
      return 'Turn {}: act() is function of the digger and bomber, not the {} {}. ({},{})'.format(self.game.turnNumber, self.thiefType, self.id, self.x, self.y)
    if self.thiefType == self.game.bomber:
      if self.specialsLeft <= 0:
        return 'Turn {}: No bombs remaining for your bomber {}. ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y)
      elif self.movementLeft != self.maxMovement:
        return 'Turn {}: Your bomber {} cannot move and throw a bomb on the same turn. ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y)
      elif abs(self.x-x) + abs(self.y-y) != 1:
        return 'Turn {}: Your bomber {} must throw onto an adjacent tile. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      elif not (0 <= x < self.game.mapWidth and 0 <= y < self.game.mapHeight):
        return 'Turn {}: Your bomber {} must bomb on the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

      #Blow stuff up
      for unit in self.game.grid[x][y]:
        #Blow up walls
        if isinstance(unit, Tile) and unit.type == 2:
          unit.type = 0
        #Blow up traps
        if isinstance(unit, Trap) and unit.trapType != 0:
          self.game.grid[x][y].remove(unit)
        #Blow up thieves
        if isinstance(unit, Thief):
          unit.alive = 0
          self.game.grid[x][y].remove(unit)
        
      self.game.addAnimation(BombAnimation(self.id, self.game.grid[x][y][0]))
      self.movementLeft = 0
      self.specialsLeft -= 1

    if self.thiefType == self.game.digger:
      if self.specialsLeft <= 0:
        return "Turn {}: Your digger {} has no shovel. ({},{})".format(self.game.turnNumber, self.id, self.x, self.y)
      elif self.movementLeft != self.maxMovement:
        return "Turn {}: Your digger {} cannot move and dig on the same turn. ({},{})".format(self.game.turnNumber, self.id, self.x, self.y)
      elif abs(self.x-x) + abs(self.y-y) != 1:
        return 'Turn {}: Your digger {} must dig on an adjacent tile. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      elif self.game.getTile(x, y).type != 2:
        return 'Turn {}: Your digger {} must dig into a wall. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)
      elif not (0 <= x < self.game.mapWidth and 0 <= y < self.game.mapHeight):
        return 'Turn {}: Your digger {} must dig on the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

      #make sure that there is somewhere to end up on the other side of the wall
      xchange = x - self.x
      ychange = y - self.y
      thisTile = self.game.getTile(x + xchange, y + ychange)
      if thisTile is None or thisTile.type != 0:
        return 'Turn {}: Your digger {} has nowhere to go on the other side of the map. ({},{}) -> ({},{})'.format(self.game.turnNumber, self.id, self.x, self.y, x, y)

      self.game.addAnimation(DigAnimation(self.id, self.game.grid[x][y][0], x + xchange, y + ychange))

      self.game.grid[self.x][self.y].remove(self)
      newX = x + xchange
      newY = y + ychange
      self.x = newX
      self.y = newY
      self.game.grid[self.x][self.y].append(self)

      self.movementLeft = 0
      self.specialsLeft -= 1


  def __setattr__(self, name, value):
      if name in self.game_state_attributes:
        object.__setattr__(self, 'updatedAt', self.game.turnNumber)
      object.__setattr__(self, name, value)

class ThiefType(object):
  game_state_attributes = ['id', 'name', 'type', 'cost', 'maxMovement', 'maxSpecials', 'maxInstances']
  def __init__(self, game, id, name, type, cost, maxMovement, maxSpecials, maxInstances):
    self.game = game
    self.id = id
    self.name = name
    self.type = type
    self.cost = cost
    self.maxMovement = maxMovement
    self.maxSpecials = maxSpecials
    self.maxInstances = maxInstances
    self.updatedAt = game.turnNumber

  def toList(self):
    return [self.id, self.name, self.type, self.cost, self.maxMovement, self.maxSpecials, self.maxInstances, ]
  
  # This will not work if the object has variables other than primitives
  def toJson(self):
    return dict(id = self.id, name = self.name, type = self.type, cost = self.cost, maxMovement = self.maxMovement, maxSpecials = self.maxSpecials, maxInstances = self.maxInstances, )
  
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
  def __init__(self, sourceID, x, y):
    self.sourceID = sourceID
    self.x = x
    self.y = y

  def toList(self):
    return ["spawn", self.sourceID, self.x, self.y, ]

  def toJson(self):
    return dict(type = "spawn", sourceID = self.sourceID, x = self.x, y = self.y)

class ActivateAnimation:
  def __init__(self, sourceID):
    self.sourceID = sourceID

  def toList(self):
    return ["activate", self.sourceID, ]

  def toJson(self):
    return dict(type = "activate", sourceID = self.sourceID)

class BombAnimation:
  def __init__(self, sourceID, targetID):
    self.sourceID = sourceID
    self.targetID = targetID

  def toList(self):
    return ["bomb", self.sourceID, self.targetID, ]

  def toJson(self):
    return dict(type = "bomb", sourceID = self.sourceID, targetID = self.targetID)

class MoveAnimation:
  def __init__(self, sourceID, fromX, fromY, toX, toY):
    self.sourceID = sourceID
    self.fromX = fromX
    self.fromY = fromY
    self.toX = toX
    self.toY = toY

  def toList(self):
    return ["move", self.sourceID, self.fromX, self.fromY, self.toX, self.toY, ]

  def toJson(self):
    return dict(type = "move", sourceID = self.sourceID, fromX = self.fromX, fromY = self.fromY, toX = self.toX, toY = self.toY)

class KillAnimation:
  def __init__(self, sourceID, targetID):
    self.sourceID = sourceID
    self.targetID = targetID

  def toList(self):
    return ["kill", self.sourceID, self.targetID, ]

  def toJson(self):
    return dict(type = "kill", sourceID = self.sourceID, targetID = self.targetID)

class PharaohTalkAnimation:
  def __init__(self, playerID, message):
    self.playerID = playerID
    self.message = message

  def toList(self):
    return ["pharaohTalk", self.playerID, self.message, ]

  def toJson(self):
    return dict(type = "pharaohTalk", playerID = self.playerID, message = self.message)

class ThiefTalkAnimation:
  def __init__(self, sourceID, message):
    self.sourceID = sourceID
    self.message = message

  def toList(self):
    return ["thiefTalk", self.sourceID, self.message, ]

  def toJson(self):
    return dict(type = "thiefTalk", sourceID = self.sourceID, message = self.message)

class DigAnimation:
  def __init__(self, sourceID, targetID, x, y):
    self.sourceID = sourceID
    self.targetID = targetID
    self.x = x
    self.y = y

  def toList(self):
    return ["dig", self.sourceID, self.targetID, self.x, self.y, ]

  def toJson(self):
    return dict(type = "dig", sourceID = self.sourceID, targetID = self.targetID, x = self.x, y = self.y)

class RollAnimation:
  def __init__(self, sourceID, x, y):
    self.sourceID = sourceID
    self.x = x
    self.y = y

  def toList(self):
    return ["roll", self.sourceID, self.x, self.y, ]

  def toJson(self):
    return dict(type = "roll", sourceID = self.sourceID, x = self.x, y = self.y)

