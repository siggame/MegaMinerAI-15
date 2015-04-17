import Player, Mappable, Tile, Trap, Thief, ThiefType, TrapType, structures, game;
import std.array;

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
  
    ///The width of the total map.
    int mapWidth() {
      return game.getMapWidth(c);
    }
    
    ///The height of the total map.
    int mapHeight() {
      return game.getMapHeight(c);
    }
    
    ///The current turn number.
    int turnNumber() {
      return game.getTurnNumber(c);
    }
    
    ///The current turn number for this round.
    int roundTurnNumber() {
      return game.getRoundTurnNumber(c);
    }
    
    ///The maximum number of Thieves allowed per player.
    int maxThieves() {
      return game.getMaxThieves(c);
    }
    
    ///The maximum number of Traps allowed per player.
    int maxTraps() {
      return game.getMaxTraps(c);
    }
    
    ///The id of the current player.
    int playerID() {
      return game.getPlayerID(c);
    }
    
    ///What number game this is for the server.
    int gameNumber() {
      return game.getGameNumber(c);
    }
    
    ///What round of the game this is.
    int roundNumber() {
      return game.getRoundNumber(c);
    }
    
    ///The scarabs given to a player to purchase traps per round.
    int scarabsForTraps() {
      return game.getScarabsForTraps(c);
    }
    
    ///The scarabs given to a player to purchase thieves per round.
    int scarabsForThieves() {
      return game.getScarabsForThieves(c);
    }
    
    ///The number of won rounds required to win.
    int roundsToWin() {
      return game.getRoundsToWin(c);
    }
    
    ///The maximum number of round turns before a winner is decided.
    int roundTurnLimit() {
      return game.getRoundTurnLimit(c);
    }
    
    ///The number of sarcophagi each player will start with each round.
    int numberOfSarcophagi() {
      return game.getNumberOfSarcophagi(c);
    }
    
    ///Make this your username, which should be provided.
    abstract const string username();
    
    ///Make this your password, which should be provided.
    abstract const string password();
    
    ///This function is run once, before your first turn.
    abstract void init();
    
    ///This function is called each time it is your turn
    ///Return true to end your turn, return false to ask the server for updated information
    abstract bool run();
    
    bool startTurn() {
      static bool initialized = false;
      iteration++;
      int count = 0;
      count = getPlayerCount(c);
      players = new Player[count];
      foreach (i; 0..count) {
        players[i] = new Player(getPlayer(c, i));
      }
      
      count = getMappableCount(c);
      mappables = new Mappable[count];
      foreach (i; 0..count) {
        mappables[i] = new Mappable(getMappable(c, i));
      }
      
      count = getTileCount(c);
      tiles = new Tile[count];
      foreach (i; 0..count) {
        tiles[i] = new Tile(getTile(c, i));
      }
      
      count = getTrapCount(c);
      traps = new Trap[count];
      foreach (i; 0..count) {
        traps[i] = new Trap(getTrap(c, i));
      }
      
      count = getThiefCount(c);
      thieves = new Thief[count];
      foreach (i; 0..count) {
        thieves[i] = new Thief(getThief(c, i));
      }
      
      count = getThiefTypeCount(c);
      thiefTypes = new ThiefType[count];
      foreach (i; 0..count) {
        thiefTypes[i] = new ThiefType(getThiefType(c, i));
      }
      
      count = getTrapTypeCount(c);
      trapTypes = new TrapType[count];
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
