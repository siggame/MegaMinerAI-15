import structures, std.conv;

class ThiefType {
  private _ThiefType* ptr = null;
  
  public:
  
  this(_ThiefType* pointer) {
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
  
  int getMaxMovement() {
    return ptr.maxMovement;
  }
  
  int getMaxSpecials() {
    return ptr.maxSpecials;
  }
  
  int getMaxInstances() {
    return ptr.maxInstances;
  }
  
  override string toString() {
    return "id: " ~ to!string(ptr.id) ~ "\n" ~
           "name: " ~ to!string(ptr.name) ~ "\n" ~
           "type: " ~ to!string(ptr.type) ~ "\n" ~
           "cost: " ~ to!string(ptr.cost) ~ "\n" ~
           "maxMovement: " ~ to!string(ptr.maxMovement) ~ "\n" ~
           "maxSpecials: " ~ to!string(ptr.maxSpecials) ~ "\n" ~
           "maxInstances: " ~ to!string(ptr.maxInstances) ~ "\n";
  }
}
