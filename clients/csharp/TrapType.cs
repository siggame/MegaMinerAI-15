using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a type of trap.
/// </summary>
public class TrapType
{
  public IntPtr ptr;
  protected int ID;
  protected int iteration;

  public TrapType()
  {
  }

  public TrapType(IntPtr p)
  {
    ptr = p;
    ID = Client.trapTypeGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.trapTypes.Length; i++)
    {
      if(BaseAI.trapTypes[i].ID == ID)
      {
        ptr = BaseAI.trapTypes[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

  #region Commands
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
      int value = Client.trapTypeGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// The name of this type of trap.
  /// </summary>
  public string Name
  {
    get
    {
      validify();
      IntPtr value = Client.trapTypeGetName(ptr);
      return Marshal.PtrToStringAuto(value);
    }
  }

  /// <summary>
  /// The type of this trap. This value is unique for all types.
  /// </summary>
  public int Type
  {
    get
    {
      validify();
      int value = Client.trapTypeGetType(ptr);
      return value;
    }
  }

  /// <summary>
  /// The number of scarabs required to purchase this trap.
  /// </summary>
  public int Cost
  {
    get
    {
      validify();
      int value = Client.trapTypeGetCost(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether the trap starts visible to the enemy player.
  /// </summary>
  public int StartsVisible
  {
    get
    {
      validify();
      int value = Client.trapTypeGetStartsVisible(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether the trap is able to act().
  /// </summary>
  public int HasAction
  {
    get
    {
      validify();
      int value = Client.trapTypeGetHasAction(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
