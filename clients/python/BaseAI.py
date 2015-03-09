# -*- python -*-

from library import library

class BaseAI:
  """@brief A basic AI interface.

  This class implements most the code an AI would need to interface with the lower-level game code.
  AIs should extend this class to get a lot of builer-plate code out of the way
  The provided AI class does just that.
  """
  #\cond
  initialized = False
  iteration = 0
  runGenerator = None
  connection = None
  #\endcond
  players = []
  mappables = []
  tiles = []
  traps = []
  thiefs = []
  thiefTypes = []
  trapTypes = []
  #\cond
  def startTurn(self):
    from GameObject import Player
    from GameObject import Mappable
    from GameObject import Tile
    from GameObject import Trap
    from GameObject import Thief
    from GameObject import ThiefType
    from GameObject import TrapType

    BaseAI.players = [Player(library.getPlayer(self.connection, i)) for i in xrange(library.getPlayerCount(self.connection))]
    BaseAI.mappables = [Mappable(library.getMappable(self.connection, i)) for i in xrange(library.getMappableCount(self.connection))]
    BaseAI.tiles = [Tile(library.getTile(self.connection, i)) for i in xrange(library.getTileCount(self.connection))]
    BaseAI.traps = [Trap(library.getTrap(self.connection, i)) for i in xrange(library.getTrapCount(self.connection))]
    BaseAI.thiefs = [Thief(library.getThief(self.connection, i)) for i in xrange(library.getThiefCount(self.connection))]
    BaseAI.thiefTypes = [ThiefType(library.getThiefType(self.connection, i)) for i in xrange(library.getThiefTypeCount(self.connection))]
    BaseAI.trapTypes = [TrapType(library.getTrapType(self.connection, i)) for i in xrange(library.getTrapTypeCount(self.connection))]

    if not self.initialized:
      self.initialized = True
      self.init()
    BaseAI.iteration += 1;
    if self.runGenerator:
      try:
        return self.runGenerator.next()
      except StopIteration:
        self.runGenerator = None
    r = self.run()
    if hasattr(r, '__iter__'):
      self.runGenerator = r
      return r.next()
    return r
  #\endcond
  #\cond
  def getMapWidth(self):
    return library.getMapWidth(self.connection)
  #\endcond
  mapWidth = property(getMapWidth)
  #\cond
  def getMapHeight(self):
    return library.getMapHeight(self.connection)
  #\endcond
  mapHeight = property(getMapHeight)
  #\cond
  def getTurnNumber(self):
    return library.getTurnNumber(self.connection)
  #\endcond
  turnNumber = property(getTurnNumber)
  #\cond
  def getRoundTurnNumber(self):
    return library.getRoundTurnNumber(self.connection)
  #\endcond
  roundTurnNumber = property(getRoundTurnNumber)
  #\cond
  def getMaxThieves(self):
    return library.getMaxThieves(self.connection)
  #\endcond
  maxThieves = property(getMaxThieves)
  #\cond
  def getMaxTraps(self):
    return library.getMaxTraps(self.connection)
  #\endcond
  maxTraps = property(getMaxTraps)
  #\cond
  def getPlayerID(self):
    return library.getPlayerID(self.connection)
  #\endcond
  playerID = property(getPlayerID)
  #\cond
  def getGameNumber(self):
    return library.getGameNumber(self.connection)
  #\endcond
  gameNumber = property(getGameNumber)
  #\cond
  def getRoundNumber(self):
    return library.getRoundNumber(self.connection)
  #\endcond
  roundNumber = property(getRoundNumber)
  #\cond
  def getScarabsForTraps(self):
    return library.getScarabsForTraps(self.connection)
  #\endcond
  scarabsForTraps = property(getScarabsForTraps)
  #\cond
  def getScarabsForThieves(self):
    return library.getScarabsForThieves(self.connection)
  #\endcond
  scarabsForThieves = property(getScarabsForThieves)
  #\cond
  def getMaxStack(self):
    return library.getMaxStack(self.connection)
  #\endcond
  maxStack = property(getMaxStack)
  #\cond
  def getRoundsToWin(self):
    return library.getRoundsToWin(self.connection)
  #\endcond
  roundsToWin = property(getRoundsToWin)
  def __init__(self, connection):
    self.connection = connection
