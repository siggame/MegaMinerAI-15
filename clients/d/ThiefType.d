import structures, std.conv, BaseAI, getters, ExistentialError;

static const int BOMBER = 0;
static const int DIGGER = 1;
static const int NINJA = 2;
static const int GUIDE = 3;
static const int SLAVE = 4;

class ThiefType {
  private:
    _ThiefType* ptr = null;
    int id, iteration;
  
  public:
    this(_ThiefType* pointer) {
      ptr = pointer;
      id = thiefTypeGetId(ptr);
      iteration = BaseAI.iteration;
    }
    
    bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (thiefType; BaseAI.BaseAI.thiefTypes) {
        if(thiefType.id == id) {
          ptr = thiefType.ptr;
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
    
    int getMaxMovement() {
      validify();
      return ptr.maxMovement;
    }
    
    int getMaxSpecials() {
      validify();
      return ptr.maxSpecials;
    }
    
    int getMaxInstances() {
      validify();
      return ptr.maxInstances;
    }
    
    override string toString() {
      validify();
      return "id: " ~ to!string(ptr.id) ~ "\n" ~
             "name: " ~ to!string(ptr.name) ~ "\n" ~
             "type: " ~ to!string(ptr.type) ~ "\n" ~
             "cost: " ~ to!string(ptr.cost) ~ "\n" ~
             "maxMovement: " ~ to!string(ptr.maxMovement) ~ "\n" ~
             "maxSpecials: " ~ to!string(ptr.maxSpecials) ~ "\n" ~
             "maxInstances: " ~ to!string(ptr.maxInstances) ~ "\n";
    }
}
