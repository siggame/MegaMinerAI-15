import structures, std.conv, std.string, std.utf, game, getters, ExistentialError, BaseAI;

class Player {
  private:
    _Player* ptr = null;
    int id, iteration;
  
  public:
    this(_Player* pointer) {
      ptr = pointer;
      id = playerGetId(ptr);
      iteration = BaseAI.iteration;
    }
    
    bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (player; BaseAI.BaseAI.players) {
        if(player.id == id) {
          ptr = player.ptr;
          iteration = BaseAI.iteration;
          return true;
        }
      }
      throw new ExistentialError();
    }
    
    int getID() {
      validify();
      return ptr.id;
    }
    
    string getName() {
      validify();
      return to!string(ptr.playerName);
    }
    
    float getTime() {
      validify();
      return ptr.time;
    }
    
    int getScarabs() {
      validify();
      return ptr.scarabs;
    }
    
    int getRoundWon() {
      validify();
      return ptr.roundsWon;
    }
    
    bool placeTrap(int x, int y, int trapType) {
      validify();
      return playerPlaceTrap(ptr, x, y, trapType) == 1;
    }
    
    bool purchaseThief(int x, int y, int thiefType) {
      validify();
      return playerPurchaseThief(ptr, x, y, thiefType) == 1;
    }
    
    bool pharaohTalk(string message) {
      validify();
      return playerPharaohTalk(ptr, toUTFz!(char*)(message)) == 1;
    }
    
    override string toString() {
      validify();
      return "id: " ~ to!string(ptr.id) ~ "\n" ~
             "playerName: " ~ to!string(ptr.playerName) ~ "\n" ~
             "time: " ~ to!string(ptr.time) ~ "\n" ~
             "scarabs: " ~ to!string(ptr.scarabs) ~ "\n" ~
             "roundsWon: " ~ to!string(ptr.roundsWon) ~ "\n";
    }
}
