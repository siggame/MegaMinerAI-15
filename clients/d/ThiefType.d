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
    
    ///Unique identifier
    int getID() {
      validify();
      return ptr.id;
    }
    
    ///The name of this type of thief.
    string getName() {
      validify();
      return to!string(ptr.name);
    }
    
    ///The type of this thief. This value is unique for all types.
    int getType() {
      validify();
      return ptr.type;
    }
    
    ///The number of scarabs required to purchase this thief.
    int getCost() {
      validify();
      return ptr.cost;
    }
    
    ///The maximum number of times this thief can move.
    int getMaxMovement() {
      validify();
      return ptr.maxMovement;
    }
    
    ///The maximum number of times this thief can use its special ability.
    int getMaxSpecials() {
      validify();
      return ptr.maxSpecials;
    }
    
    ///The maximum number of this type thief that can be purchased each round.
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
