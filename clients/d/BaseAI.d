import Player, Mappable, Tile, Trap, Thief, ThiefType, TrapType, structures, game;
import std.array;

class BaseAI {
  protected:
    Connection* c;
    Player[] players;
    Mappable[] mappable;
    Tile[] tiles;
    Trap[] traps;
    Thief[] thieves;
    ThiefType[] thiefTypes;
    TrapType[] trapTypes;
  
  public:
    this(Connection* connection) {
      c = connection;
    }
  
    int getMapWidth() {
      getMapWidth(c);
    }
    
    int getMapHeight() {
      getMapHeight(c);
    }
    
    int getTurnNumber() {
      getTurnNumber(c);
    }
    
    int getRoundTurnNumber() {
      getRoundTurnNumber(c);
    }
    
    int getMaxTheives() {
      getMaxTheives(c);
    }
    
    int getMaxTraps() {
      getMaxTraps(c);
    }
    
    int getPlayerID() {
      getPlayerID(c);
    }
    
    int getGameNumber() {
      getGameNumber(c);
    }
    
    int getRoundNumber() {
      getRoundNumber(c);
    }
    
    int getScarabsForTraps() {
      getScarabsForTraps(c);
    }
    
    int getScarabsForTheieves() {
      getScarabsForTheieves(c);
    }
    
    int getMaxStack() {
      getMaxStack(c);
    }
    
    int getRoundToWin() {
      getRoundToWin(c);
    }
    
    int getRoundTurnLimit() {
      getRoundTurnLimit(c);
    }
    
    abstract const string getUsername();
    abstract const string getPassword();
    abstract void init();
    abstract bool run();
    
    bool startTurn() {
      static bool initialized = false;
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
