import BaseAI, TrapType, ThiefType, structures;
import std.typecons, std.stdio;

public class AI : BaseAI {
  public:
    Player me;
    alias position = Tuple!(int, "x", int, "y");
    position[] spawnPoints; 
    
    this(Connection* conn) {
      super(conn);
    }
  
    override const string username() {
      return "Shell AI";
    }
    
    override const string password() {
      return "password";
    }
    
    override void init() {
      me = players[playerID()];
      
      int mapSize = mapHeight();
      spawnPoints = new position[4];
      spawnPoints[0] = position(mapSize/2-1 + (1-playerID())*mapSize, 0);
      spawnPoints[1] = position(mapSize-1 + (1-playerID())*mapSize, mapSize/2-1);
      spawnPoints[2] = position(mapSize/2+1 + (1-playerID())*mapSize, mapSize-1);
      spawnPoints[3] = position((1-playerID())*mapHeight(), mapSize/2+1);
    }
    
    override bool run() {
      if (roundTurnNumber() <= 1) {
        int mapSize = mapHeight();
        me.placeTrap(mapSize/2-1 + playerID()*mapSize, 1, TrapType.SARCOPHAGUS);
      }
      else if (roundTurnNumber() <= 3) {
        me.purchaseThief(spawnPoints[0].x, spawnPoints[0].y, ThiefType.SLAVE);
      }
      
      foreach (thief; thieves) {
        if (thief.getOwner() == playerID())
          thief.move(thief.getX(), thief.getY()+1);
      }
      return true;
    }
    
    void end() {
    
    }
}
