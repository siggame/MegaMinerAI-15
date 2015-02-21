import com.sun.jna.Pointer;

///Represents a tile.
class Tile
{
  Pointer ptr;
  int ID;
  int iteration;
  public Tile(Pointer p)
  {
    ptr = p;
    ID = Client.INSTANCE.tileGetId(ptr);
    iteration = BaseAI.iteration;
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.tiles.length; i++)
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

    //commands


    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.tileGetId(ptr);
  }
  ///Whether this tile is a wall or not.
  public int getIsWall()
  {
    validify();
    return Client.INSTANCE.tileGetIsWall(ptr);
  }

}
