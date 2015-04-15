using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a type of thief.
/// </summary>
public class ThiefType
{
  public IntPtr ptr;
  protected int ID;
  protected int iteration;

  public ThiefType()
  {
  }

  public ThiefType(IntPtr p)
  {
    ptr = p;
    ID = Client.thiefTypeGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.thiefTypes.Length; i++)
    {
      if(BaseAI.thiefTypes[i].ID == ID)
      {
        ptr = BaseAI.thiefTypes[i].ptr;
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
      int value = Client.thiefTypeGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// The name of this type of thief.
  /// </summary>
  public string Name
  {
    get
    {
      validify();
      IntPtr value = Client.thiefTypeGetName(ptr);
      return Marshal.PtrToStringAuto(value);
    }
  }

  /// <summary>
  /// The type of this thief. This value is unique for all types.
  /// </summary>
  public int Type
  {
    get
    {
      validify();
      int value = Client.thiefTypeGetType(ptr);
      return value;
    }
  }

  /// <summary>
  /// The number of scarabs required to purchase this thief.
  /// </summary>
  public int Cost
  {
    get
    {
      validify();
      int value = Client.thiefTypeGetCost(ptr);
      return value;
    }
  }

  /// <summary>
  /// The maximum number of times this thief can move.
  /// </summary>
  public int MaxMovement
  {
    get
    {
      validify();
      int value = Client.thiefTypeGetMaxMovement(ptr);
      return value;
    }
  }

  /// <summary>
  /// The maximum number of times this thief can use its special ability.
  /// </summary>
  public int MaxSpecials
  {
    get
    {
      validify();
      int value = Client.thiefTypeGetMaxSpecials(ptr);
      return value;
    }
  }

  /// <summary>
  /// The maximum number of this type thief that can be purchased each round.
  /// </summary>
  public int MaxInstances
  {
    get
    {
      validify();
      int value = Client.thiefTypeGetMaxInstances(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
