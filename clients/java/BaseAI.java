import com.sun.jna.Pointer;

/// \brief A basic AI interface.

///This class implements most the code an AI would need to interface with the lower-level game code.
///AIs should extend this class to get a lot of builer-plate code out of the way
///The provided AI class does just that.
public abstract class BaseAI
{
  static Player[] players;
  static Mappable[] mappables;
  static Tile[] tiles;
  static Trap[] traps;
  static Thief[] thiefs;
  static ThiefType[] thiefTypes;
  static TrapType[] trapTypes;
  Pointer connection;
  static int iteration;
  boolean initialized;

  public BaseAI(Pointer c)
  {
    connection = c;
  }
    
  ///
  ///Make this your username, which should be provided.
  public abstract String username();
  ///
  ///Make this your password, which should be provided.
  public abstract String password();
  ///
  ///This is run on turn 1 before run
  public abstract void init();
  ///
  ///This is run every turn . Return true to end the turn, return false
  ///to request a status update from the server and then immediately rerun this function with the
  ///latest game status.
  public abstract boolean run();

  ///
  ///This is run on after your last turn.
  public abstract void end();


  public boolean startTurn()
  {
    iteration++;
    int count = 0;
    count = Client.INSTANCE.getPlayerCount(connection);
    players = new Player[count];
    for(int i = 0; i < count; i++)
    {
      players[i] = new Player(Client.INSTANCE.getPlayer(connection, i));
    }
    count = Client.INSTANCE.getMappableCount(connection);
    mappables = new Mappable[count];
    for(int i = 0; i < count; i++)
    {
      mappables[i] = new Mappable(Client.INSTANCE.getMappable(connection, i));
    }
    count = Client.INSTANCE.getTileCount(connection);
    tiles = new Tile[count];
    for(int i = 0; i < count; i++)
    {
      tiles[i] = new Tile(Client.INSTANCE.getTile(connection, i));
    }
    count = Client.INSTANCE.getTrapCount(connection);
    traps = new Trap[count];
    for(int i = 0; i < count; i++)
    {
      traps[i] = new Trap(Client.INSTANCE.getTrap(connection, i));
    }
    count = Client.INSTANCE.getThiefCount(connection);
    thiefs = new Thief[count];
    for(int i = 0; i < count; i++)
    {
      thiefs[i] = new Thief(Client.INSTANCE.getThief(connection, i));
    }
    count = Client.INSTANCE.getThiefTypeCount(connection);
    thiefTypes = new ThiefType[count];
    for(int i = 0; i < count; i++)
    {
      thiefTypes[i] = new ThiefType(Client.INSTANCE.getThiefType(connection, i));
    }
    count = Client.INSTANCE.getTrapTypeCount(connection);
    trapTypes = new TrapType[count];
    for(int i = 0; i < count; i++)
    {
      trapTypes[i] = new TrapType(Client.INSTANCE.getTrapType(connection, i));
    }

    if(!initialized)
    {
      initialized = true;
      init();
    }
    return run();
  }


  ///The width of the total map.
  int mapWidth()
  {
    return Client.INSTANCE.getMapWidth(connection);
  }
  ///The height of the total map.
  int mapHeight()
  {
    return Client.INSTANCE.getMapHeight(connection);
  }
  ///The current turn number.
  int turnNumber()
  {
    return Client.INSTANCE.getTurnNumber(connection);
  }
  ///The current turn number for this round.
  int roundTurnNumber()
  {
    return Client.INSTANCE.getRoundTurnNumber(connection);
  }
  ///The maximum number of Thieves allowed per player.
  int maxThieves()
  {
    return Client.INSTANCE.getMaxThieves(connection);
  }
  ///The maximum number of Traps allowed per player.
  int maxTraps()
  {
    return Client.INSTANCE.getMaxTraps(connection);
  }
  ///The id of the current player.
  int playerID()
  {
    return Client.INSTANCE.getPlayerID(connection);
  }
  ///What number game this is for the server.
  int gameNumber()
  {
    return Client.INSTANCE.getGameNumber(connection);
  }
  ///What round of the game this is.
  int roundNumber()
  {
    return Client.INSTANCE.getRoundNumber(connection);
  }
  ///The scarabs given to a player to purchase traps per round.
  int scarabsForTraps()
  {
    return Client.INSTANCE.getScarabsForTraps(connection);
  }
  ///The scarabs given to a player to purchase thieves per round.
  int scarabsForThieves()
  {
    return Client.INSTANCE.getScarabsForThieves(connection);
  }
  ///The number of won rounds required to win.
  int roundsToWin()
  {
    return Client.INSTANCE.getRoundsToWin(connection);
  }
  ///The maximum number of round turns before a winner is decided.
  int roundTurnLimit()
  {
    return Client.INSTANCE.getRoundTurnLimit(connection);
  }
  ///The number of sarcophagi each player will start with each round.
  int numberOfSarcophagi()
  {
    return Client.INSTANCE.getNumberOfSarcophagi(connection);
  }
}
