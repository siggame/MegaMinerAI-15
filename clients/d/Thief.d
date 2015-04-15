import Mappable, structures, game, ExistentialError;
import std.conv, std.string, std.utf;

class Thief : Mappable {
  public this(_Thief* pointer) {
    super(cast(_Mappable*)pointer); 
  }
  
  override bool validify() {
    if (iteration == BaseAI.iteration) return true;
    foreach (thief; BaseAI.BaseAI.thieves) {
      if(thief.id == id) {
        ptr = thief.ptr;
        iteration = BaseAI.iteration;
        return true;
      }
    }
    throw new ExistentialError();
  }
  
  override int getID() {
    validify();
    return (cast(_Thief*)ptr).id;
  }
  
  override int getX() {
    validify();
    return (cast(_Thief*)ptr).x;
  }
  
  override int getY() {
    validify();
    return (cast(_Thief*)ptr).y;
  }
  
  int getOwner() {
    validify();
    return (cast(_Thief*)ptr).owner;
  }
  
  int getThiefType() {
    validify();
    return (cast(_Thief*)ptr).thiefType;
  }
  
  bool isAlive() {
    return (cast(_Thief*)ptr).alive == 1;
  }
  
  int getSpecialsLeft() {
    validify();
    return (cast(_Thief*)ptr).specialsLeft;
  }
  
  int getMaxSpecials() {
    validify();
    return (cast(_Thief*)ptr).maxSpecials;
  }
  
  int getMovementLeft() {
    validify();
    return (cast(_Thief*)ptr).movementLeft;
  }
  
  int getMaxMovement() {
    validify();
    return (cast(_Thief*)ptr).maxMovement;
  }
  
  int getFrozenTurnsLeft() {
    validify();
    return (cast(_Thief*)ptr).frozenTurnsLeft;
  }
  
  bool thiefTalk(string message) {
    validify();
    return thiefThiefTalk((cast(_Thief*)ptr), toUTFz!(char*)(message)) == 1;
  }
  
  bool move(int x, int y) {
    validify();
    return thiefMove((cast(_Thief*)ptr), x, y) == 1;
  }
  
  bool useSpecial(int x, int y) {
    validify();
    return thiefUseSpecial((cast(_Thief*)ptr), x, y) == 1;
  }
  
  override string toString() {
    validify();
    _Thief* thief_ptr = cast(_Thief*)ptr;
    return "id: " ~ to!string(thief_ptr.id) ~ "\n" ~
           "x: " ~ to!string(thief_ptr.x) ~ "\n" ~
           "y: " ~ to!string(thief_ptr.y) ~ "\n" ~
           "owner: " ~ to!string(thief_ptr.owner) ~ "\n" ~
           "thiefType: " ~ to!string(thief_ptr.thiefType) ~ "\n" ~
           "alive: " ~ to!string(thief_ptr.alive == 1) ~ "\n" ~
           "specialsLeft: " ~ to!string(thief_ptr.specialsLeft) ~ "\n" ~
           "maxSpecials: " ~ to!string(thief_ptr.maxSpecials) ~ "\n" ~
           "movementLeft: " ~ to!string(thief_ptr.movementLeft) ~ "\n" ~
           "maxMovement: " ~ to!string(thief_ptr.maxMovement) ~ "\n" ~
           "frozenTurnsLeft: " ~ to!string(thief_ptr.frozenTurnsLeft) ~ "\n";
  }
}
