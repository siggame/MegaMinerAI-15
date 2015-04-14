import com.sun.jna.Pointer;

///Represents a single thief on the map.
class Thief extends Mappable
{
  public Thief(Pointer p)
  {
    super(p);
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.thiefs.length; i++)
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

    //commands

  ///Allows a thief to display messages on the screen
  boolean thiefTalk(String message)
  {
    validify();
    return (Client.INSTANCE.thiefThiefTalk(ptr, message) == 0) ? false : true;
  }
  ///Commands a thief to move to a new location.
  boolean move(int x, int y)
  {
    validify();
    return (Client.INSTANCE.thiefMove(ptr, x, y) == 0) ? false : true;
  }
  ///Commands a thief to use a special on a location.
  boolean useSpecial(int x, int y)
  {
    validify();
    return (Client.INSTANCE.thiefUseSpecial(ptr, x, y) == 0) ? false : true;
  }

    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.thiefGetId(ptr);
  }
  ///X position of the object
  public int getX()
  {
    validify();
    return Client.INSTANCE.thiefGetX(ptr);
  }
  ///Y position of the object
  public int getY()
  {
    validify();
    return Client.INSTANCE.thiefGetY(ptr);
  }
  ///The owner of this thief.
  public int getOwner()
  {
    validify();
    return Client.INSTANCE.thiefGetOwner(ptr);
  }
  ///The type of this thief. This type refers to list of thiefTypes.
  public int getThiefType()
  {
    validify();
    return Client.INSTANCE.thiefGetThiefType(ptr);
  }
  ///Whether the thief is alive or not.
  public int getAlive()
  {
    validify();
    return Client.INSTANCE.thiefGetAlive(ptr);
  }
  ///How many more times this thief can use its special ability.
  public int getSpecialsLeft()
  {
    validify();
    return Client.INSTANCE.thiefGetSpecialsLeft(ptr);
  }
  ///The maximum number of times this thief can use its special ability.
  public int getMaxSpecials()
  {
    validify();
    return Client.INSTANCE.thiefGetMaxSpecials(ptr);
  }
  ///The remaining number of times this thief can move.
  public int getMovementLeft()
  {
    validify();
    return Client.INSTANCE.thiefGetMovementLeft(ptr);
  }
  ///The maximum number of times this thief can move.
  public int getMaxMovement()
  {
    validify();
    return Client.INSTANCE.thiefGetMaxMovement(ptr);
  }
  ///How many turns this thief is frozen for.
  public int getFrozenTurnsLeft()
  {
    validify();
    return Client.INSTANCE.thiefGetFrozenTurnsLeft(ptr);
  }

}
