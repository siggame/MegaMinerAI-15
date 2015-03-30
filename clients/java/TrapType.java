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
  ///The maximum number of this type of trap that can be placed in a round by a player.
  public int getMaxInstances()
  {
    validify();
    return Client.INSTANCE.trapTypeGetMaxInstances(ptr);
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
  ///Whether the trap can be deactivated by the player, stopping the trap from automatically activating.
  public int getDeactivatable()
  {
    validify();
    return Client.INSTANCE.trapTypeGetDeactivatable(ptr);
  }
  ///The maximum number of times this trap can be activated before being disabled.
  public int getMaxActivations()
  {
    validify();
    return Client.INSTANCE.trapTypeGetMaxActivations(ptr);
  }
  ///This trap activates when a thief moves onto and then off of this tile.
  public int getActivatesOnWalkedThrough()
  {
    validify();
    return Client.INSTANCE.trapTypeGetActivatesOnWalkedThrough(ptr);
  }
  ///The maximum number of turns a thief can stay on this tile before it activates.
  public int getTurnsToActivateOnTile()
  {
    validify();
    return Client.INSTANCE.trapTypeGetTurnsToActivateOnTile(ptr);
  }
  ///Whether this trap can be placed inside of walls.
  public int getCanPlaceOnWalls()
  {
    validify();
    return Client.INSTANCE.trapTypeGetCanPlaceOnWalls(ptr);
  }
  ///Whether this trap can be placed on empty tiles.
  public int getCanPlaceOnOpenTiles()
  {
    validify();
    return Client.INSTANCE.trapTypeGetCanPlaceOnOpenTiles(ptr);
  }
  ///How many turns a thief will be frozen when this trap activates.
  public int getFreezesForTurns()
  {
    validify();
    return Client.INSTANCE.trapTypeGetFreezesForTurns(ptr);
  }
  ///Whether this trap kills thieves when activated.
  public int getKillsOnActivate()
  {
    validify();
    return Client.INSTANCE.trapTypeGetKillsOnActivate(ptr);
  }
  ///How many turns this trap has to wait between activations.
  public int getCooldown()
  {
    validify();
    return Client.INSTANCE.trapTypeGetCooldown(ptr);
  }
  ///When destroyed via dynamite kills adjacent thieves.
  public int getExplosive()
  {
    validify();
    return Client.INSTANCE.trapTypeGetExplosive(ptr);
  }
  ///Cannot be passed through, stopping a thief that tries to move onto its tile.
  public int getUnpassable()
  {
    validify();
    return Client.INSTANCE.trapTypeGetUnpassable(ptr);
  }

}
