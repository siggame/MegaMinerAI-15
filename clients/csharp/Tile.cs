using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a tile.
/// </summary>
public class Tile: Mappable
{

  public Tile()
  {
  }

  public Tile(IntPtr p)
  {
    ptr = p;
    ID = Client.tileGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public override bool validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.tiles.Length; i++)
    {
      if(BaseAI.tiles[i].ID == ID)
      {
        ptr = BaseAI.tiles[i].ptr;
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
  public new int Id
  {
    get
    {
      validify();
      int value = Client.tileGetId(ptr);
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
      int value = Client.tileGetX(ptr);
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
      int value = Client.tileGetY(ptr);
      return value;
    }
  }

  /// <summary>
  /// What type of tile this is. 0: empty, 1: spawn: 2: wall.
  /// </summary>
  public int Type
  {
    get
    {
      validify();
      int value = Client.tileGetType(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
