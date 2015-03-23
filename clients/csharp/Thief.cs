using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a single thief on the map.
/// </summary>
public class Thief: Mappable
{

  public Thief()
  {
  }

  public Thief(IntPtr p)
  {
    ptr = p;
    ID = Client.thiefGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public override bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.thiefs.Length; i++)
    {
      if(BaseAI.thiefs[i].ID == ID)
      {
        ptr = BaseAI.thiefs[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

  #region Commands
  /// <summary>
  /// Allows a thief to display messages on the screen
  /// </summary>
  public bool thiefTalk(string message)
  {
    validify();
    return (Client.thiefThiefTalk(ptr, message) == 0) ? false : true;
  }
  /// <summary>
  /// Commands a thief to move to a new location.
  /// </summary>
  public bool move(int x, int y)
  {
    validify();
    return (Client.thiefMove(ptr, x, y) == 0) ? false : true;
  }
  /// <summary>
  /// Commands a thief to act on a location.
  /// </summary>
  public bool act(int x, int y)
  {
    validify();
    return (Client.thiefAct(ptr, x, y) == 0) ? false : true;
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
      int value = Client.thiefGetId(ptr);
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
      int value = Client.thiefGetX(ptr);
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
      int value = Client.thiefGetY(ptr);
      return value;
    }
  }

  /// <summary>
  /// The owner of this thief.
  /// </summary>
  public int Owner
  {
    get
    {
      validify();
      int value = Client.thiefGetOwner(ptr);
      return value;
    }
  }

  /// <summary>
  /// The type of this thief. This type refers to list of thiefTypes.
  /// </summary>
  public int ThiefType
  {
    get
    {
      validify();
      int value = Client.thiefGetThiefType(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether the thief is alive or not.
  /// </summary>
  public int Alive
  {
    get
    {
      validify();
      int value = Client.thiefGetAlive(ptr);
      return value;
    }
  }

  /// <summary>
  /// How many more times this thief can use its special ability.
  /// </summary>
  public int SpecialsLeft
  {
    get
    {
      validify();
      int value = Client.thiefGetSpecialsLeft(ptr);
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
      int value = Client.thiefGetMaxSpecials(ptr);
      return value;
    }
  }

  /// <summary>
  /// The remaining number of times this thief can move.
  /// </summary>
  public int MovementLeft
  {
    get
    {
      validify();
      int value = Client.thiefGetMovementLeft(ptr);
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
      int value = Client.thiefGetMaxMovement(ptr);
      return value;
    }
  }

  /// <summary>
  /// How many turns this thief is frozen for.
  /// </summary>
  public int FrozenTurnsLeft
  {
    get
    {
      validify();
      int value = Client.thiefGetFrozenTurnsLeft(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
