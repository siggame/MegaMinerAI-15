import Mappable, structures, std.conv, game;

class Trap : Mappable {
  private _Trap* trap_ptr = null;
  
  public:
  
  this(_Trap* pointer) {
	super(cast(_Mappable*)pointer);
    trap_ptr = pointer;
  }
  
  override int getID() {
    return trap_ptr.id;
  }
  
  override int getX() {
    return trap_ptr.x;
  }
  
  override int getY() {
    return trap_ptr.y;
  }
  
  int getOwner() {
    return trap_ptr.owner;
  }
  
  int getTrapType() {
    return trap_ptr.trapType;
  }
  
  bool isVisible() {
    return trap_ptr.visible == 1;
  }
  
  bool isActive() {
    return trap_ptr.active == 1;
  } 
  
  int getBodyCount() {
    return trap_ptr.bodyCount;
  }
  
  int getActivationsRemaining() {
    return trap_ptr.activationsRemaining;
  }
  
  int getTurnsTillActive() {
    return trap_ptr.turnsTillActive;
  }
  
  bool act(int x, int y) {
    return trapAct(trap_ptr, x, y) == 1;
  }
  
  bool toggle() {
    return trapToggle(trap_ptr) == 1;
  }
  
  override string toString() {
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
