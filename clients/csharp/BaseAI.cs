using System;
using System.Runtime.InteropServices;

/// <summary>
/// This class implements most the code an AI would need to interface with the lower-level game code.
/// AIs should extend this class to get a lot of builer-plate code out of the way. The provided AI class does just that.
/// </summary>
public abstract class BaseAI
{
  public static Player[] players;
  public static Mappable[] mappables;
  public static Tile[] tiles;
  public static Trap[] traps;
  public static Thief[] thiefs;
  public static ThiefType[] thiefTypes;
  public static TrapType[] trapTypes;

  IntPtr connection;
  public static int iteration;
  bool initialized;

  public BaseAI(IntPtr c)
  {
    connection = c;
  }

  /// <summary>
  /// Make this your username, which should be provided.
  /// </summary>
  /// <returns>Returns the username of the player.</returns>
  public abstract String username();

  /// <summary>
  /// Make this your password, which should be provided.
  /// </summary>
  /// <returns>Returns the password of the player.</returns>
  public abstract String password();

  /// <summary>
  /// This is run once on turn one before run().
  /// </summary>
  public abstract void init();

  /// <summary>
  /// This is run every turn.
  /// </summary>
  /// <returns>
  /// Return true to end turn, false to resynchronize with the 
  /// server and run again.
  /// </returns>
  public abstract bool run();

  /// <summary>
  /// This is run once after your last turn.
  /// </summary>
  public abstract void end();

  /// <summary>
  /// Synchronizes with the server, then calls run().
  /// </summary>
  /// <returns>
  /// Return true to end turn, false to resynchronize with the 
  /// server and run again.
  /// </returns>
  public bool startTurn()
  {
    int count = 0;
    iteration++;

    count = Client.getPlayerCount(connection);
    players = new Player[count];
    for(int i = 0; i < count; i++)
      players[i] = new Player(Client.getPlayer(connection, i));

    count = Client.getMappableCount(connection);
    mappables = new Mappable[count];
    for(int i = 0; i < count; i++)
      mappables[i] = new Mappable(Client.getMappable(connection, i));

    count = Client.getTileCount(connection);
    tiles = new Tile[count];
    for(int i = 0; i < count; i++)
      tiles[i] = new Tile(Client.getTile(connection, i));

    count = Client.getTrapCount(connection);
    traps = new Trap[count];
    for(int i = 0; i < count; i++)
      traps[i] = new Trap(Client.getTrap(connection, i));

    count = Client.getThiefCount(connection);
    thiefs = new Thief[count];
    for(int i = 0; i < count; i++)
      thiefs[i] = new Thief(Client.getThief(connection, i));

    count = Client.getThiefTypeCount(connection);
    thiefTypes = new ThiefType[count];
    for(int i = 0; i < count; i++)
      thiefTypes[i] = new ThiefType(Client.getThiefType(connection, i));

    count = Client.getTrapTypeCount(connection);
    trapTypes = new TrapType[count];
    for(int i = 0; i < count; i++)
      trapTypes[i] = new TrapType(Client.getTrapType(connection, i));

    if(!initialized)
    {
      initialized = true;
      init();
    }

    return run();
  }

  /// <summary>
  /// The width of the total map.
  /// </summary>
  /// <returns>Returns the width of the total map.</returns>
  public int mapWidth()
  {
    int value = Client.getMapWidth(connection);
    return value;
  }

  /// <summary>
  /// The height of the total map.
  /// </summary>
  /// <returns>Returns the height of the total map.</returns>
  public int mapHeight()
  {
    int value = Client.getMapHeight(connection);
    return value;
  }

  /// <summary>
  /// The current turn number.
  /// </summary>
  /// <returns>Returns the current turn number.</returns>
  public int turnNumber()
  {
    int value = Client.getTurnNumber(connection);
    return value;
  }

  /// <summary>
  /// The current turn number for this round.
  /// </summary>
  /// <returns>Returns the current turn number for this round.</returns>
  public int roundTurnNumber()
  {
    int value = Client.getRoundTurnNumber(connection);
    return value;
  }

  /// <summary>
  /// The maximum number of Thieves allowed per player.
  /// </summary>
  /// <returns>Returns the maximum number of Thieves allowed per player.</returns>
  public int maxThieves()
  {
    int value = Client.getMaxThieves(connection);
    return value;
  }

  /// <summary>
  /// The maximum number of Traps allowed per player.
  /// </summary>
  /// <returns>Returns the maximum number of Traps allowed per player.</returns>
  public int maxTraps()
  {
    int value = Client.getMaxTraps(connection);
    return value;
  }

  /// <summary>
  /// The id of the current player.
  /// </summary>
  /// <returns>Returns the id of the current player.</returns>
  public int playerID()
  {
    int value = Client.getPlayerID(connection);
    return value;
  }

  /// <summary>
  /// What number game this is for the server.
  /// </summary>
  /// <returns>Returns what number game this is for the server.</returns>
  public int gameNumber()
  {
    int value = Client.getGameNumber(connection);
    return value;
  }

  /// <summary>
  /// What round of the game this is.
  /// </summary>
  /// <returns>Returns what round of the game this is.</returns>
  public int roundNumber()
  {
    int value = Client.getRoundNumber(connection);
    return value;
  }

  /// <summary>
  /// The scarabs given to a player to purchase traps per round.
  /// </summary>
  /// <returns>Returns the scarabs given to a player to purchase traps per round.</returns>
  public int scarabsForTraps()
  {
    int value = Client.getScarabsForTraps(connection);
    return value;
  }

  /// <summary>
  /// The scarabs given to a player to purchase thieves per round.
  /// </summary>
  /// <returns>Returns the scarabs given to a player to purchase thieves per round.</returns>
  public int scarabsForThieves()
  {
    int value = Client.getScarabsForThieves(connection);
    return value;
  }

  /// <summary>
  /// The maximum number of thieves per tile.
  /// </summary>
  /// <returns>Returns the maximum number of thieves per tile.</returns>
  public int maxStack()
  {
    int value = Client.getMaxStack(connection);
    return value;
  }

  /// <summary>
  /// The number of won rounds required to win.
  /// </summary>
  /// <returns>Returns the number of won rounds required to win.</returns>
  public int roundsToWin()
  {
    int value = Client.getRoundsToWin(connection);
    return value;
  }
}
