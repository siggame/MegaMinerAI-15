# -*- python -*-

from library import library

from ExistentialError import ExistentialError

class GameObject(object):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration


##
class Player(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.playerGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.players:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  ##Place the specified trap type at the given location.
  def placeTrap(self, x, y, trapType):
    self.validify()
    return library.playerPlaceTrap(self._ptr, x, y, trapType)

  ##Place the specified thief type at the given location.
  def purchaseThief(self, x, y, thiefType):
    self.validify()
    return library.playerPurchaseThief(self._ptr, x, y, thiefType)

  ##Display a message on the screen.
  def pharaohTalk(self, message):
    self.validify()
    return library.playerPharaohTalk(self._ptr, message)

  #\cond
  def getId(self):
    self.validify()
    return library.playerGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getPlayerName(self):
    self.validify()
    return library.playerGetPlayerName(self._ptr)
  #\endcond
  ##Player's Name
  playerName = property(getPlayerName)

  #\cond
  def getTime(self):
    self.validify()
    return library.playerGetTime(self._ptr)
  #\endcond
  ##Time remaining, updated at start of turn
  time = property(getTime)

  #\cond
  def getScarabs(self):
    self.validify()
    return library.playerGetScarabs(self._ptr)
  #\endcond
  ##The number of scarabs this player has to purchase traps or thieves.
  scarabs = property(getScarabs)

  #\cond
  def getRoundsWon(self):
    self.validify()
    return library.playerGetRoundsWon(self._ptr)
  #\endcond
  ##The number of rounds won by this player.
  roundsWon = property(getRoundsWon)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "playerName: %s\n" % self.getPlayerName()
    ret += "time: %s\n" % self.getTime()
    ret += "scarabs: %s\n" % self.getScarabs()
    ret += "roundsWon: %s\n" % self.getRoundsWon()
    return ret

##A mappable object!
class Mappable(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.mappableGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.mappables:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  #\cond
  def getId(self):
    self.validify()
    return library.mappableGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getX(self):
    self.validify()
    return library.mappableGetX(self._ptr)
  #\endcond
  ##X position of the object
  x = property(getX)

  #\cond
  def getY(self):
    self.validify()
    return library.mappableGetY(self._ptr)
  #\endcond
  ##Y position of the object
  y = property(getY)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "x: %s\n" % self.getX()
    ret += "y: %s\n" % self.getY()
    return ret

##Represents a tile.
class Tile(Mappable):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.tileGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.tiles:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  #\cond
  def getId(self):
    self.validify()
    return library.tileGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getX(self):
    self.validify()
    return library.tileGetX(self._ptr)
  #\endcond
  ##X position of the object
  x = property(getX)

  #\cond
  def getY(self):
    self.validify()
    return library.tileGetY(self._ptr)
  #\endcond
  ##Y position of the object
  y = property(getY)

  #\cond
  def getType(self):
    self.validify()
    return library.tileGetType(self._ptr)
  #\endcond
  ##What type of tile this is. 0: empty, 1: spawn: 2: wall.
  type = property(getType)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "x: %s\n" % self.getX()
    ret += "y: %s\n" % self.getY()
    ret += "type: %s\n" % self.getType()
    return ret

##Represents a single trap on the map.
class Trap(Mappable):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.trapGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.traps:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  ##Commands a trap to act on a location.
  def act(self, x, y):
    self.validify()
    return library.trapAct(self._ptr, x, y)

  ##Commands a trap to toggle between being activated or not.
  def toggle(self):
    self.validify()
    return library.trapToggle(self._ptr)

  #\cond
  def getId(self):
    self.validify()
    return library.trapGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getX(self):
    self.validify()
    return library.trapGetX(self._ptr)
  #\endcond
  ##X position of the object
  x = property(getX)

  #\cond
  def getY(self):
    self.validify()
    return library.trapGetY(self._ptr)
  #\endcond
  ##Y position of the object
  y = property(getY)

  #\cond
  def getOwner(self):
    self.validify()
    return library.trapGetOwner(self._ptr)
  #\endcond
  ##The owner of this trap.
  owner = property(getOwner)

  #\cond
  def getTrapType(self):
    self.validify()
    return library.trapGetTrapType(self._ptr)
  #\endcond
  ##The type of this trap. This type refers to list of trapTypes.
  trapType = property(getTrapType)

  #\cond
  def getVisible(self):
    self.validify()
    return library.trapGetVisible(self._ptr)
  #\endcond
  ##Whether the trap is visible to the enemy player.
  visible = property(getVisible)

  #\cond
  def getActive(self):
    self.validify()
    return library.trapGetActive(self._ptr)
  #\endcond
  ##Whether the trap is active.
  active = property(getActive)

  #\cond
  def getBodyCount(self):
    self.validify()
    return library.trapGetBodyCount(self._ptr)
  #\endcond
  ##How many thieves this trap has killed.
  bodyCount = property(getBodyCount)

  #\cond
  def getActivationsRemaining(self):
    self.validify()
    return library.trapGetActivationsRemaining(self._ptr)
  #\endcond
  ##How many more times this trap can activate.
  activationsRemaining = property(getActivationsRemaining)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "x: %s\n" % self.getX()
    ret += "y: %s\n" % self.getY()
    ret += "owner: %s\n" % self.getOwner()
    ret += "trapType: %s\n" % self.getTrapType()
    ret += "visible: %s\n" % self.getVisible()
    ret += "active: %s\n" % self.getActive()
    ret += "bodyCount: %s\n" % self.getBodyCount()
    ret += "activationsRemaining: %s\n" % self.getActivationsRemaining()
    return ret

##Represents a single thief on the map.
class Thief(Mappable):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.thiefGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.thiefs:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  ##Allows a thief to display messages on the screen
  def thiefTalk(self, message):
    self.validify()
    return library.thiefThiefTalk(self._ptr, message)

  ##Commands a thief to move to a new location.
  def move(self, x, y):
    self.validify()
    return library.thiefMove(self._ptr, x, y)

  ##Commands a thief to act on a location.
  def act(self, x, y):
    self.validify()
    return library.thiefAct(self._ptr, x, y)

  #\cond
  def getId(self):
    self.validify()
    return library.thiefGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getX(self):
    self.validify()
    return library.thiefGetX(self._ptr)
  #\endcond
  ##X position of the object
  x = property(getX)

  #\cond
  def getY(self):
    self.validify()
    return library.thiefGetY(self._ptr)
  #\endcond
  ##Y position of the object
  y = property(getY)

  #\cond
  def getOwner(self):
    self.validify()
    return library.thiefGetOwner(self._ptr)
  #\endcond
  ##The owner of this thief.
  owner = property(getOwner)

  #\cond
  def getThiefType(self):
    self.validify()
    return library.thiefGetThiefType(self._ptr)
  #\endcond
  ##The type of this thief. This type refers to list of thiefTypes.
  thiefType = property(getThiefType)

  #\cond
  def getAlive(self):
    self.validify()
    return library.thiefGetAlive(self._ptr)
  #\endcond
  ##Whether the thief is alive or not.
  alive = property(getAlive)

  #\cond
  def getNinjaReflexesLeft(self):
    self.validify()
    return library.thiefGetNinjaReflexesLeft(self._ptr)
  #\endcond
  ##How many more deaths this thief can escape.
  ninjaReflexesLeft = property(getNinjaReflexesLeft)

  #\cond
  def getMaxNinjaReflexes(self):
    self.validify()
    return library.thiefGetMaxNinjaReflexes(self._ptr)
  #\endcond
  ##The maximum number of times this thief can escape death.
  maxNinjaReflexes = property(getMaxNinjaReflexes)

  #\cond
  def getMovementLeft(self):
    self.validify()
    return library.thiefGetMovementLeft(self._ptr)
  #\endcond
  ##The remaining number of times this thief can move.
  movementLeft = property(getMovementLeft)

  #\cond
  def getMaxMovement(self):
    self.validify()
    return library.thiefGetMaxMovement(self._ptr)
  #\endcond
  ##The maximum number of times this thief can move.
  maxMovement = property(getMaxMovement)

  #\cond
  def getFrozenTurnsLeft(self):
    self.validify()
    return library.thiefGetFrozenTurnsLeft(self._ptr)
  #\endcond
  ##How many turns this thief is frozen for.
  frozenTurnsLeft = property(getFrozenTurnsLeft)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "x: %s\n" % self.getX()
    ret += "y: %s\n" % self.getY()
    ret += "owner: %s\n" % self.getOwner()
    ret += "thiefType: %s\n" % self.getThiefType()
    ret += "alive: %s\n" % self.getAlive()
    ret += "ninjaReflexesLeft: %s\n" % self.getNinjaReflexesLeft()
    ret += "maxNinjaReflexes: %s\n" % self.getMaxNinjaReflexes()
    ret += "movementLeft: %s\n" % self.getMovementLeft()
    ret += "maxMovement: %s\n" % self.getMaxMovement()
    ret += "frozenTurnsLeft: %s\n" % self.getFrozenTurnsLeft()
    return ret

##Represents a type of thief.
class ThiefType(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.thiefTypeGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.thiefTypes:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  #\cond
  def getId(self):
    self.validify()
    return library.thiefTypeGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getName(self):
    self.validify()
    return library.thiefTypeGetName(self._ptr)
  #\endcond
  ##The name of this type of thief.
  name = property(getName)

  #\cond
  def getType(self):
    self.validify()
    return library.thiefTypeGetType(self._ptr)
  #\endcond
  ##The type of this thief. This value is unique for all types.
  type = property(getType)

  #\cond
  def getCost(self):
    self.validify()
    return library.thiefTypeGetCost(self._ptr)
  #\endcond
  ##The number of scarabs required to purchase this thief.
  cost = property(getCost)

  #\cond
  def getMaxMovement(self):
    self.validify()
    return library.thiefTypeGetMaxMovement(self._ptr)
  #\endcond
  ##The maximum number of times this thief can move.
  maxMovement = property(getMaxMovement)

  #\cond
  def getMaxNinjaReflexes(self):
    self.validify()
    return library.thiefTypeGetMaxNinjaReflexes(self._ptr)
  #\endcond
  ##The maximum number of times this thief can escape death.
  maxNinjaReflexes = property(getMaxNinjaReflexes)

  #\cond
  def getMaxInstances(self):
    self.validify()
    return library.thiefTypeGetMaxInstances(self._ptr)
  #\endcond
  ##The maximum number of this type thief that can be purchased each round.
  maxInstances = property(getMaxInstances)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "name: %s\n" % self.getName()
    ret += "type: %s\n" % self.getType()
    ret += "cost: %s\n" % self.getCost()
    ret += "maxMovement: %s\n" % self.getMaxMovement()
    ret += "maxNinjaReflexes: %s\n" % self.getMaxNinjaReflexes()
    ret += "maxInstances: %s\n" % self.getMaxInstances()
    return ret

##Represents a type of trap.
class TrapType(GameObject):
  def __init__(self, ptr):
    from BaseAI import BaseAI
    self._ptr = ptr
    self._iteration = BaseAI.iteration
    self._id = library.trapTypeGetId(ptr)

  #\cond
  def validify(self):
    from BaseAI import BaseAI
    #if this class is pointing to an object from before the current turn it's probably
    #somewhere else in memory now
    if self._iteration == BaseAI.iteration:
      return True
    for i in BaseAI.trapTypes:
      if i._id == self._id:
        self._ptr = i._ptr
        self._iteration = BaseAI.iteration
        return True
    raise ExistentialError()
  #\endcond
  #\cond
  def getId(self):
    self.validify()
    return library.trapTypeGetId(self._ptr)
  #\endcond
  ##Unique Identifier
  id = property(getId)

  #\cond
  def getName(self):
    self.validify()
    return library.trapTypeGetName(self._ptr)
  #\endcond
  ##The name of this type of trap.
  name = property(getName)

  #\cond
  def getType(self):
    self.validify()
    return library.trapTypeGetType(self._ptr)
  #\endcond
  ##The type of this trap. This value is unique for all types.
  type = property(getType)

  #\cond
  def getCost(self):
    self.validify()
    return library.trapTypeGetCost(self._ptr)
  #\endcond
  ##The number of scarabs required to purchase this trap.
  cost = property(getCost)

  #\cond
  def getMaxInstances(self):
    self.validify()
    return library.trapTypeGetMaxInstances(self._ptr)
  #\endcond
  ##The maximum number of this type of trap that can be placed in a round by a player.
  maxInstances = property(getMaxInstances)

  #\cond
  def getStartsVisible(self):
    self.validify()
    return library.trapTypeGetStartsVisible(self._ptr)
  #\endcond
  ##Whether the trap starts visible to the enemy player.
  startsVisible = property(getStartsVisible)

  #\cond
  def getHasAction(self):
    self.validify()
    return library.trapTypeGetHasAction(self._ptr)
  #\endcond
  ##Whether the trap is able to act().
  hasAction = property(getHasAction)

  #\cond
  def getDeactivatable(self):
    self.validify()
    return library.trapTypeGetDeactivatable(self._ptr)
  #\endcond
  ##Whether the trap can be deactivated by the player, stopping the trap from automatically activating.
  deactivatable = property(getDeactivatable)

  #\cond
  def getMaxActivations(self):
    self.validify()
    return library.trapTypeGetMaxActivations(self._ptr)
  #\endcond
  ##The maximum number of times this trap can be activated before being disabled.
  maxActivations = property(getMaxActivations)

  #\cond
  def getActivatesOnWalkedThrough(self):
    self.validify()
    return library.trapTypeGetActivatesOnWalkedThrough(self._ptr)
  #\endcond
  ##This trap activates when a thief moves onto and then off of this tile.
  activatesOnWalkedThrough = property(getActivatesOnWalkedThrough)

  #\cond
  def getTurnsToActivateOnTile(self):
    self.validify()
    return library.trapTypeGetTurnsToActivateOnTile(self._ptr)
  #\endcond
  ##The maximum number of turns a thief can stay on this tile before it activates.
  turnsToActivateOnTile = property(getTurnsToActivateOnTile)

  #\cond
  def getCanPlaceOnWalls(self):
    self.validify()
    return library.trapTypeGetCanPlaceOnWalls(self._ptr)
  #\endcond
  ##Whether this trap can be placed inside of walls.
  canPlaceOnWalls = property(getCanPlaceOnWalls)

  #\cond
  def getCanPlaceOnOpenTiles(self):
    self.validify()
    return library.trapTypeGetCanPlaceOnOpenTiles(self._ptr)
  #\endcond
  ##Whether this trap can be placed on empty tiles.
  canPlaceOnOpenTiles = property(getCanPlaceOnOpenTiles)

  #\cond
  def getFreezesForTurns(self):
    self.validify()
    return library.trapTypeGetFreezesForTurns(self._ptr)
  #\endcond
  ##How many turns a thief will be frozen when this trap activates.
  freezesForTurns = property(getFreezesForTurns)

  #\cond
  def getKillsOnActivate(self):
    self.validify()
    return library.trapTypeGetKillsOnActivate(self._ptr)
  #\endcond
  ##Whether this trap kills thieves when activated.
  killsOnActivate = property(getKillsOnActivate)

  #\cond
  def getCooldown(self):
    self.validify()
    return library.trapTypeGetCooldown(self._ptr)
  #\endcond
  ##How many turns this trap has to wait between activations.
  cooldown = property(getCooldown)

  #\cond
  def getExplosive(self):
    self.validify()
    return library.trapTypeGetExplosive(self._ptr)
  #\endcond
  ##When destroyed via dynamite kills adjacent thieves.
  explosive = property(getExplosive)

  #\cond
  def getUnpassable(self):
    self.validify()
    return library.trapTypeGetUnpassable(self._ptr)
  #\endcond
  ##Cannot be passed through, stopping a thief that tries to move onto its tile.
  unpassable = property(getUnpassable)


  def __str__(self):
    self.validify()
    ret = ""
    ret += "id: %s\n" % self.getId()
    ret += "name: %s\n" % self.getName()
    ret += "type: %s\n" % self.getType()
    ret += "cost: %s\n" % self.getCost()
    ret += "maxInstances: %s\n" % self.getMaxInstances()
    ret += "startsVisible: %s\n" % self.getStartsVisible()
    ret += "hasAction: %s\n" % self.getHasAction()
    ret += "deactivatable: %s\n" % self.getDeactivatable()
    ret += "maxActivations: %s\n" % self.getMaxActivations()
    ret += "activatesOnWalkedThrough: %s\n" % self.getActivatesOnWalkedThrough()
    ret += "turnsToActivateOnTile: %s\n" % self.getTurnsToActivateOnTile()
    ret += "canPlaceOnWalls: %s\n" % self.getCanPlaceOnWalls()
    ret += "canPlaceOnOpenTiles: %s\n" % self.getCanPlaceOnOpenTiles()
    ret += "freezesForTurns: %s\n" % self.getFreezesForTurns()
    ret += "killsOnActivate: %s\n" % self.getKillsOnActivate()
    ret += "cooldown: %s\n" % self.getCooldown()
    ret += "explosive: %s\n" % self.getExplosive()
    ret += "unpassable: %s\n" % self.getUnpassable()
    return ret
