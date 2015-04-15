import structures, std.conv, getters, ExistentialError, BaseAI;

static const int SARCOPHAGUS = 0;
static const int SNAKE_PIT = 1;
static const int SWINGING_BLADE = 2;
static const int BOULDER = 3;
static const int SPIDER_WEB = 4;
static const int QUICKSAND = 5;
static const int OIL_VASES = 6;
static const int ARROW_WALL = 7;
static const int HEAD_WIRE = 8;
static const int MERCURY_PIT = 9;
static const int MUMMY = 10;
static const int FAKE_ROTATING_WALL = 11;

class TrapType {
  private:
    _TrapType* ptr = null;
    int id, iteration;
  
  public:
    this(_TrapType* pointer) {
      ptr = pointer;
      id = trapTypeGetId(ptr);
      iteration = BaseAI.iteration;
    }
    
    bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (trapType; BaseAI.BaseAI.trapTypes) {
        if(trapType.id == id) {
          ptr = trapType.ptr;
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
      return to!string(ptr.name);
    }
    
    int getType() {
      validify();
      return ptr.type;
    }
    
    int getCost() {
      validify();
      return ptr.cost;
    }
    
    int getMaxInstances() {
      validify();
      return ptr.maxInstances;
    }
    
    bool startsVisible() {
      validify();
      return ptr.startsVisible == 1;
    }
    
    bool hasAction() {
      validify();
      return ptr.hasAction == 1;
    }
    
    bool isDeactivatable() {
      validify();
      return ptr.deactivatable == 1;
    }
    
    int getMaxActivations() {
      validify();
      return ptr.maxActivations;
    }
    
    bool activatesOnWalkedThrough() {
      validify();
      return ptr.activatesOnWalkedThrough == 1;
    }
    
    int turnsToActivateOnTile() {
      validify();
      return ptr.turnsToActivateOnTile;
    }
    
    bool canPlaceOnWalls() {
      validify();
      return ptr.canPlaceOnWalls == 1;
    }
    
    bool canPlaceOnOpenTiles() {
      validify();
      return ptr.canPlaceOnOpenTiles == 1;
    }
    
    int freezesForTurns() {
      validify();
      return ptr.freezesForTurns;
    }
    
    bool killsOnActivate() {
      validify();
      return ptr.killsOnActivate == 1;
    }
    
    int cooldown() {
      validify();
      return ptr.cooldown;
    }
    
    bool isExplosive() {
      validify();
      return ptr.explosive == 1;
    }
    
    bool isUnpassable() {
      validify();
      return ptr.unpassable == 1;
    }
    
    override string toString() {
      validify();
      return "id: " ~ to!string(ptr.id) ~ "\n" ~
             "name: " ~ to!string(ptr.name) ~ "\n" ~
             "type: " ~ to!string(ptr.type) ~ "\n" ~
             "cost: " ~ to!string(ptr.cost) ~ "\n" ~
             "maxInstances: " ~ to!string(ptr.maxInstances) ~ "\n" ~
             "startsVisible: " ~ to!string(ptr.startsVisible == 1) ~ "\n" ~
             "hasAction: " ~ to!string(ptr.hasAction == 1) ~ "\n" ~
             "deactivatable: " ~ to!string(ptr.deactivatable == 1) ~ "\n" ~
             "maxActivations: " ~ to!string(ptr.maxActivations) ~ "\n" ~
             "activatesOnWalkedThrough: " ~ to!string(ptr.activatesOnWalkedThrough == 1) ~ "\n" ~
             "turnsToActivateOnTile: " ~ to!string(ptr.turnsToActivateOnTile) ~ "\n" ~
             "canPlaceOnWalls: " ~ to!string(ptr.canPlaceOnWalls == 1) ~ "\n" ~
             "canPlaceOnOpenTiles: " ~ to!string(ptr.canPlaceOnOpenTiles == 1) ~ "\n" ~
             "freezesForTurns: " ~ to!string(ptr.freezesForTurns) ~ "\n" ~
             "killsOnActivate: " ~ to!string(ptr.killsOnActivate == 1) ~ "\n" ~
             "cooldown: " ~ to!string(ptr.cooldown) ~ "\n" ~
             "explosive: " ~ to!string(ptr.explosive == 1) ~ "\n" ~
             "unpassable: " ~ to!string(ptr.unpassable == 1) ~ "\n";
    }
}
