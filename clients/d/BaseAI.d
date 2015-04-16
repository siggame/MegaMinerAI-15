import Player, Mappable, Tile, Trap, Thief, ThiefType, TrapType, structures, game;
import std.array, std.stdio;

static int iteration = 0;

class BaseAI {
  public:
    Connection* c;
    static Player[] players;
    static Mappable[] mappables;
    static Tile[] tiles;
    static Trap[] traps;
    static Thief[] thieves;
    static ThiefType[] thiefTypes;
    static TrapType[] trapTypes;

    this(Connection* connection) {
      c = connection;
    }
  
    int mapWidth() {
      return game.getMapWidth(c);
    }
    
    int mapHeight() {
      return game.getMapHeight(c);
    }
    
    int turnNumber() {
      return game.getTurnNumber(c);
    }
    
    int roundTurnNumber() {
      return game.getRoundTurnNumber(c);
    }
    
    int maxThieves() {
      return game.getMaxThieves(c);
    }
    
    int maxTraps() {
      return game.getMaxTraps(c);
    }
    
    int playerID() {
      return game.getPlayerID(c);
    }
    
    int gameNumber() {
      return game.getGameNumber(c);
    }
    
    int roundNumber() {
      return game.getRoundNumber(c);
    }
    
    int scarabsForTraps() {
      return game.getScarabsForTraps(c);
    }
    
    int scarabsForThieves() {
      return game.getScarabsForThieves(c);
    }
    
    int roundsToWin() {
      return game.getRoundsToWin(c);
    }
    
    int roundTurnLimit() {
      return game.getRoundTurnLimit(c);
    }
    
    int numberOfSarcophagi() {
      return game.getNumberOfSarcophagi(c);
    }
    
    abstract const string username();
    abstract const string password();
    abstract void init();
    abstract bool run();
    
    bool startTurn() {
      static bool initialized = false;
      iteration++;
      int count = 0;
      count = getPlayerCount(c);
      players.clear();
      players.length = count;
      foreach (i; 0..count) {
        players[i] = new Player(getPlayer(c, i));
      }
      
      count = getMappableCount(c);
      mappables.clear();
      mappables.length = count;
      foreach (i; 0..count) {
        mappables[i] = new Mappable(getMappable(c, i));
      }
      
      count = getTileCount(c);
      tiles.clear();
      tiles.length = count;
      foreach (i; 0..count) {
        tiles[i] = new Tile(getTile(c, i));
      }
      
      count = getTrapCount(c);
      traps.clear();
      traps.length = count;
      foreach (i; 0..count) {
        traps[i] = new Trap(getTrap(c, i));
      }
      
      count = getThiefCount(c);
      thieves.clear();
      thieves.length = count;
      foreach (i; 0..count) {
        thieves[i] = new Thief(getThief(c, i));
      }
      
      count = getThiefTypeCount(c);
      thiefTypes.clear();
      thiefTypes.length = count;
      foreach (i; 0..count) {
        thiefTypes[i] = new ThiefType(getThiefType(c, i));
      }
      
      count = getTrapTypeCount(c);
      trapTypes.clear();
      trapTypes.length = count;
      foreach (i; 0..count) {
        trapTypes[i] = new TrapType(getTrapType(c, i));
      }
      
      if (!initialized) {
        initialized = true;
        init();
      }
      
      return run();
    }
}
