import com.sun.jna.Pointer;

///Represents a type of trap.
class TrapType
{
  Pointer ptr;
  int ID;
  int iteration;
  public TrapType(Pointer p)
  {
    ptr = p;
    ID = Client.INSTANCE.trapTypeGetId(ptr);
    iteration = BaseAI.iteration;
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.trapTypes.length; i++)
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

    //commands


    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.trapTypeGetId(ptr);
  }
  ///The name of this type of trap.
  public String getName()
  {
    validify();
    return Client.INSTANCE.trapTypeGetName(ptr);
  }
  ///The type of this trap. This value is unique for all types.
  public int getType()
  {
    validify();
    return Client.INSTANCE.trapTypeGetType(ptr);
  }
  ///The number of scarabs required to purchase this trap.
  public int getCost()
  {
    validify();
    return Client.INSTANCE.trapTypeGetCost(ptr);
  }
  ///Whether the trap starts visible to the enemy player.
  public int getStartsVisible()
  {
    validify();
    return Client.INSTANCE.trapTypeGetStartsVisible(ptr);
  }
  ///Whether the trap is able to act().
  public int getHasAction()
  {
    validify();
    return Client.INSTANCE.trapTypeGetHasAction(ptr);
  }

}
