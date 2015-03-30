import com.sun.jna.Pointer;

///Represents a type of thief.
class ThiefType
{
  Pointer ptr;
  int ID;
  int iteration;
  public ThiefType(Pointer p)
  {
    ptr = p;
    ID = Client.INSTANCE.thiefTypeGetId(ptr);
    iteration = BaseAI.iteration;
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.thiefTypes.length; i++)
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

    //commands


    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetId(ptr);
  }
  ///The name of this type of thief.
  public String getName()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetName(ptr);
  }
  ///The type of this thief. This value is unique for all types.
  public int getType()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetType(ptr);
  }
  ///The number of scarabs required to purchase this thief.
  public int getCost()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetCost(ptr);
  }
  ///The maximum number of times this thief can move.
  public int getMaxMovement()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetMaxMovement(ptr);
  }
  ///The maximum number of times this thief can use its special ability.
  public int getMaxSpecials()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetMaxSpecials(ptr);
  }
  ///The maximum number of this type thief that can be purchased each round.
  public int getMaxInstances()
  {
    validify();
    return Client.INSTANCE.thiefTypeGetMaxInstances(ptr);
  }

}
