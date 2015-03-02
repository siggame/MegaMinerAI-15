import com.sun.jna.Pointer;

///
class Player
{
  Pointer ptr;
  int ID;
  int iteration;
  public Player(Pointer p)
  {
    ptr = p;
    ID = Client.INSTANCE.playerGetId(ptr);
    iteration = BaseAI.iteration;
  }
  boolean validify()
  {
    if(iteration == BaseAI.iteration) return true;
    for(int i = 0; i < BaseAI.players.length; i++)
    {
      if(BaseAI.players[i].ID == ID)
      {
        ptr = BaseAI.players[i].ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }

    //commands

  ///Place the specified trap type at the given location.
  boolean placeTrap(int x, int y, int trapType)
  {
    validify();
    return (Client.INSTANCE.playerPlaceTrap(ptr, x, y, trapType) == 0) ? false : true;
  }
  ///Place the specified thief type at the given location.
  boolean purchaseThief(int x, int y, int thiefType)
  {
    validify();
    return (Client.INSTANCE.playerPurchaseThief(ptr, x, y, thiefType) == 0) ? false : true;
  }
  ///Display a message on the screen.
  boolean pharaohTalk(String message)
  {
    validify();
    return (Client.INSTANCE.playerPharaohTalk(ptr, message) == 0) ? false : true;
  }

    //getters

  ///Unique Identifier
  public int getId()
  {
    validify();
    return Client.INSTANCE.playerGetId(ptr);
  }
  ///Player's Name
  public String getPlayerName()
  {
    validify();
    return Client.INSTANCE.playerGetPlayerName(ptr);
  }
  ///Time remaining, updated at start of turn
  public float getTime()
  {
    validify();
    return Client.INSTANCE.playerGetTime(ptr);
  }
  ///The number of scarabs this player has to purchase traps or thieves.
  public int getScarabs()
  {
    validify();
    return Client.INSTANCE.playerGetScarabs(ptr);
  }
  ///The number of rounds won by this player.
  public int getRoundsWon()
  {
    validify();
    return Client.INSTANCE.playerGetRoundsWon(ptr);
  }

}
