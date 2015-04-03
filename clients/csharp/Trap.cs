using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a single trap on the map.
/// </summary>
public class Trap: Mappable
{

  public Trap()
  {
  }

  public Trap(IntPtr p)
  {
    ptr = p;
    ID = Client.trapGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public override bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.traps.Length; i++)
    {
      if(BaseAI.traps[i].ID == ID)
      {
        ptr = BaseAI.traps[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

  #region Commands
  /// <summary>
  /// Commands a trap to act on a location.
  /// </summary>
  public bool act(int x, int y)
  {
    validify();
    return (Client.trapAct(ptr, x, y) == 0) ? false : true;
  }
  /// <summary>
  /// Commands a trap to toggle between being activated or not.
  /// </summary>
  public bool toggle()
  {
    validify();
    return (Client.trapToggle(ptr) == 0) ? false : true;
  }
  #endregion

  #region Getters
  /// <summary>
  /// Unique Identifier
  /// </summary>
  public new int Id
  {
    get
    {
      validify();
      int value = Client.trapGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// X position of the object
  /// </summary>
  public new int X
  {
    get
    {
      validify();
      int value = Client.trapGetX(ptr);
      return value;
    }
  }

  /// <summary>
  /// Y position of the object
  /// </summary>
  public new int Y
  {
    get
    {
      validify();
      int value = Client.trapGetY(ptr);
      return value;
    }
  }

  /// <summary>
  /// The owner of this trap.
  /// </summary>
  public int Owner
  {
    get
    {
      validify();
      int value = Client.trapGetOwner(ptr);
      return value;
    }
  }

  /// <summary>
  /// The type of this trap. This type refers to list of trapTypes.
  /// </summary>
  public int TrapType
  {
    get
    {
      validify();
      int value = Client.trapGetTrapType(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether the trap is visible to the enemy player.
  /// </summary>
  public int Visible
  {
    get
    {
      validify();
      int value = Client.trapGetVisible(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether the trap is active.
  /// </summary>
  public int Active
  {
    get
    {
      validify();
      int value = Client.trapGetActive(ptr);
      return value;
    }
  }

  /// <summary>
  /// How many thieves this trap has killed.
  /// </summary>
  public int BodyCount
  {
    get
    {
      validify();
      int value = Client.trapGetBodyCount(ptr);
      return value;
    }
  }

  /// <summary>
  /// How many more times this trap can activate.
  /// </summary>
  public int ActivationsRemaining
  {
    get
    {
      validify();
      int value = Client.trapGetActivationsRemaining(ptr);
      return value;
    }
  }

  /// <summary>
  /// How many more turns this trap is inactive due to cooldown.
  /// </summary>
  public int TurnsTillActive
  {
    get
    {
      validify();
      int value = Client.trapGetTurnsTillActive(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
