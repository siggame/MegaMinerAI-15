using System;
using System.Runtime.InteropServices;

/// <summary>
/// 
/// </summary>
public class Player
{
  public IntPtr ptr;
  protected int ID;
  protected int iteration;

  public Player()
  {
  }

  public Player(IntPtr p)
  {
    ptr = p;
    ID = Client.playerGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.players.Length; i++)
    {
      if(BaseAI.players[i].ID == ID)
      {
        ptr = BaseAI.players[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

  #region Commands
  /// <summary>
  /// Place the specified trap type at the given location.
  /// </summary>
  public bool placeTrap(int x, int y, int trapType)
  {
    validify();
    return (Client.playerPlaceTrap(ptr, x, y, trapType) == 0) ? false : true;
  }
  /// <summary>
  /// Place the specified thief type at the given location.
  /// </summary>
  public bool purchaseThief(int x, int y, int thiefType)
  {
    validify();
    return (Client.playerPurchaseThief(ptr, x, y, thiefType) == 0) ? false : true;
  }
  /// <summary>
  /// Display a message on the screen.
  /// </summary>
  public bool pharaohTalk(string message)
  {
    validify();
    return (Client.playerPharaohTalk(ptr, message) == 0) ? false : true;
  }
  #endregion

  #region Getters
  /// <summary>
  /// Unique Identifier
  /// </summary>
  public int Id
  {
    get
    {
      validify();
      int value = Client.playerGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// Player's Name
  /// </summary>
  public string PlayerName
  {
    get
    {
      validify();
      IntPtr value = Client.playerGetPlayerName(ptr);
      return Marshal.PtrToStringAuto(value);
    }
  }

  /// <summary>
  /// Time remaining, updated at start of turn
  /// </summary>
  public float Time
  {
    get
    {
      validify();
      float value = Client.playerGetTime(ptr);
      return value;
    }
  }

  /// <summary>
  /// The number of scarabs this player has to purchase traps or thieves.
  /// </summary>
  public int Scarabs
  {
    get
    {
      validify();
      int value = Client.playerGetScarabs(ptr);
      return value;
    }
  }

  /// <summary>
  /// The number of rounds won by this player.
  /// </summary>
  public int RoundsWon
  {
    get
    {
      validify();
      int value = Client.playerGetRoundsWon(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
