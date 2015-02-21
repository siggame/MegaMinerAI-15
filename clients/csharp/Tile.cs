using System;
using System.Runtime.InteropServices;

/// <summary>
/// Represents a tile.
/// </summary>
public class Tile
{
  public IntPtr ptr;
  protected int ID;
  protected int iteration;

  public Tile()
  {
  }

  public Tile(IntPtr p)
  {
    ptr = p;
    ID = Client.tileGetId(ptr);
    iteration = BaseAI.iteration;
  }

  public bool validify()
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
  public int Id
  {
    get
    {
      validify();
      int value = Client.tileGetId(ptr);
      return value;
    }
  }

  /// <summary>
  /// Whether this tile is a wall or not.
  /// </summary>
  public int IsWall
  {
    get
    {
      validify();
      int value = Client.tileGetIsWall(ptr);
      return value;
    }
  }

  #endregion

  #region Properties
  #endregion
}
