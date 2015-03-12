import com.sun.jna.Pointer;

///Represents a single trap on the map.
class Trap extends Mappable
{
  public Trap(Pointer p)
  {
    super(p);
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.traps.length; i++)
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

    //commands

  ///Commands a trap to act on a location.
  boolean act(int x, int y)
  {
    validify();
    return (Client.INSTANCE.trapAct(ptr, x, y) == 0) ? false : true;
  }
  ///Commands a trap to toggle between being activated or not.
  boolean toggle()
  {
    validify();
    return (Client.INSTANCE.trapToggle(ptr) == 0) ? false : true;
  }

    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.trapGetId(ptr);
  }
  ///X position of the object
  public int getX()
  {
    validify();
    return Client.INSTANCE.trapGetX(ptr);
  }
  ///Y position of the object
  public int getY()
  {
    validify();
    return Client.INSTANCE.trapGetY(ptr);
  }
  ///The owner of this trap.
  public int getOwner()
  {
    validify();
    return Client.INSTANCE.trapGetOwner(ptr);
  }
  ///The type of this trap. This type refers to list of trapTypes.
  public int getTrapType()
  {
    validify();
    return Client.INSTANCE.trapGetTrapType(ptr);
  }
  ///Whether the trap is visible to the enemy player.
  public int getVisible()
  {
    validify();
    return Client.INSTANCE.trapGetVisible(ptr);
  }
  ///Whether the trap is active.
  public int getActive()
  {
    validify();
    return Client.INSTANCE.trapGetActive(ptr);
  }
  ///How many thieves this trap has killed.
  public int getBodyCount()
  {
    validify();
    return Client.INSTANCE.trapGetBodyCount(ptr);
  }
  ///How many more times this trap can activate.
  public int getActivationsRemaining()
  {
    validify();
    return Client.INSTANCE.trapGetActivationsRemaining(ptr);
  }
  ///How many more turns this trap is inactive due to cooldown.
  public int getTurnsTillActive()
  {
    validify();
    return Client.INSTANCE.trapGetTurnsTillActive(ptr);
  }

}
