import structures, std.conv;

class TrapType {
  private _TrapType* ptr = null;
  
  public:
  
  this(_TrapType* pointer) {
    ptr = pointer;
  }
  
  int getID() {
    return ptr.id;
  }
  
  string getName() {
    return to!string(ptr.name);
  }
  
  int getType() {
    return ptr.type;
  }
  
  int getCost() {
    return ptr.cost;
  }
  
  int getMaxInstances() {
    return ptr.maxInstances;
  }
  
  bool startsVisible() {
    return ptr.startsVisible == 1;
  }
  
  bool hasAction() {
    return ptr.hasAction == 1;
  }
  
  bool isDeactivatable() {
    return ptr.deactivatable == 1;
  }
  
  int getMaxActivations() {
    return ptr.maxActivations;
  }
  
  bool activatesOnWalkedThrough() {
    return ptr.activatesOnWalkedThrough == 1;
  }
  
  int turnsToActivateOnTile() {
    return ptr.turnsToActivateOnTile;
  }
  
  bool canPlaceOnWalls() {
    return ptr.canPlaceOnWalls == 1;
  }
  
  bool canPlaceOnOpenTiles() {
    return ptr.canPlaceOnOpenTiles == 1;
  }
  
  int freezesForTurns() {
    return ptr.freezesForTurns;
  }
  
  bool killsOnActivate() {
    return ptr.killsOnActivate == 1;
  }
  
  int cooldown() {
    return ptr.cooldown;
  }
  
  bool isExplosive() {
    return ptr.explosive == 1;
  }
  
  bool isUnpassable() {
    return ptr.unpassable == 1;
  }
  
  override string toString() {
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
