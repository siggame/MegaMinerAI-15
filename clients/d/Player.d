import structures, std.conv, std.string, std.utf, game;

class Player {
  private _Player* ptr = null;
  
  public:
  
  this(_Player* pointer) {
    ptr = pointer;
  }
  
  int getID() {
    return ptr.id;
  }
  
  string getName() {
    return to!string(ptr.playerName);
  }
  
  float getTime() {
    return ptr.time;
  }
  
  int getScarabs() {
    return ptr.scarabs;
  }
  
  int getRoundWon() {
    return ptr.roundsWon;
  }
  
  bool placeTrap(int x, int y, int trapType) {
    return playerPlaceTrap(ptr, x, y, trapType) == 1;
  }
  
  bool purchaseThief(int x, int y, int thiefType) {
    return playerPurchaseThief(ptr, x, y, thiefType) == 1;
  }
  
  bool pharaohTalk(string message) {
    return playerPharaohTalk(ptr, toUTFz!(char*)(message)) == 1;
  }
  
  override string toString() {
    return "id: " ~ to!string(ptr.id) ~ "\n" ~
           "playerName: " ~ to!string(ptr.playerName) ~ "\n" ~
           "time: " ~ to!string(ptr.time) ~ "\n" ~
           "scarabs: " ~ to!string(ptr.scarabs) ~ "\n" ~
           "roundsWon: " ~ to!string(ptr.roundsWon) ~ "\n";
  }
}
