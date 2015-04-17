import Mappable, structures, std.conv, game, ExistentialError;

class Trap : Mappable {
  public:
    this(_Trap* pointer) {
      super(cast(_Mappable*)pointer);
    }
    
    override bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (trap; BaseAI.BaseAI.traps) {
        if(trap.id == id) {
          ptr = trap.ptr;
          iteration = BaseAI.iteration;
          return true;
        }
      }
      throw new ExistentialError();
    }
    
    ///Unique identifier
    override int getID() {
      validify();
      return (cast(_Trap*)ptr).id;
    }
    
    ///X position of the object
    override int getX() {
      validify();
      return (cast(_Trap*)ptr).x;
    }
    
    ///Y position of the object
    override int getY() {
      validify();
      return (cast(_Trap*)ptr).y;
    }
    
    ///The owner of this trap.
    int getOwner() {
      validify();
      return (cast(_Trap*)ptr).owner;
    }
    
    ///The type of this trap. This type refers to list of trapTypes.
    int getTrapType() {
      validify();
      return (cast(_Trap*)ptr).trapType;
    }
    
    ///Whether the trap is visible to the enemy player.
    bool isVisible() {
      validify();
      return (cast(_Trap*)ptr).visible == 1;
    }
    
    ///Whether the trap is active.
    bool isActive() {
      validify();
      return (cast(_Trap*)ptr).active == 1;
    } 
    
    ///How many thieves this trap has killed.
    int getBodyCount() {
      validify();
      return (cast(_Trap*)ptr).bodyCount;
    }
    
    ///How many more times this trap can activate.
    int getActivationsRemaining() {
      validify();
      return (cast(_Trap*)ptr).activationsRemaining;
    }
    
    ///How many more turns this trap is inactive due to cooldown.
    int getTurnsTillActive() {
      validify();
      return (cast(_Trap*)ptr).turnsTillActive;
    }
    
    ///Commands a trap to act on a location.
    bool act(int x, int y) {
      validify();
      return trapAct((cast(_Trap*)ptr), x, y) == 1;
    }
    
    ///Commands a trap to toggle between being activated or not.
    bool toggle() {
      validify();
      return trapToggle((cast(_Trap*)ptr)) == 1;
    }
    
    override string toString() {
      validify();
      _Trap* trap_ptr = cast(_Trap*)ptr;
      return "id: " ~ to!string(trap_ptr.id) ~ "\n" ~
             "x: " ~ to!string(trap_ptr.x) ~ "\n" ~
             "y: " ~ to!string(trap_ptr.y) ~ "\n" ~
             "owner: " ~ to!string(trap_ptr.owner) ~ "\n" ~
             "trapType: " ~ to!string(trap_ptr.trapType) ~ "\n" ~
             "visible: " ~ to!string(trap_ptr.visible == 1) ~ "\n" ~
             "active: " ~ to!string(trap_ptr.active == 1) ~ "\n" ~
             "bodyCount: " ~ to!string(trap_ptr.bodyCount) ~ "\n" ~
             "activationsRemaining: " ~ to!string(trap_ptr.activationsRemaining) ~ "\n" ~
             "turnsTillActive: " ~ to!string(trap_ptr.turnsTillActive) ~ "\n";
    }
}
