import Player, Mappable, Tile, Trap, Thief, ThiefType, TrapType, structures, game;
import std.array, std.stdio;

class BaseAI {
  protected:
    Connection* c;
    Player[] players;
    Mappable[] mappables;
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
      return game.getMapWidth(c);
    }
    
    int getMapHeight() {
      return game.getMapHeight(c);
    }
    
    int getTurnNumber() {
      return game.getTurnNumber(c);
    }
    
    int getRoundTurnNumber() {
      return game.getRoundTurnNumber(c);
    }
    
    int getMaxTheives() {
      return game.getMaxThieves(c);
    }
    
    int getMaxTraps() {
      return game.getMaxTraps(c);
    }
    
    int getPlayerID() {
      return game.getPlayerID(c);
    }
    
    int getGameNumber() {
      return game.getGameNumber(c);
    }
    
    int getRoundNumber() {
      return game.getRoundNumber(c);
    }
    
    int getScarabsForTraps() {
      return game.getScarabsForTraps(c);
    }
    
    int getScarabsForThieves() {
      return game.getScarabsForThieves(c);
    }
    
    int getMaxStack() {
      return game.getMaxStack(c);
    }
    
    int getRoundToWin() {
      return game.getRoundsToWin(c);
    }
    
    int getRoundTurnLimit() {
      return game.getRoundTurnLimit(c);
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
