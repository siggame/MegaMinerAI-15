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
  
  ///Unique Identifier
  override int getID() {
    validify();
    return (cast(_Thief*)ptr).id;
  }
  
  ///X position of the object
  override int getX() {
    validify();
    return (cast(_Thief*)ptr).x;
  }
  
  ///Y position of the object
  override int getY() {
    validify();
    return (cast(_Thief*)ptr).y;
  }
  
  ///The owner of this thief.
  int getOwner() {
    validify();
    return (cast(_Thief*)ptr).owner;
  }
  
  ///The type of this thief. This type refers to list of thiefTypes.
  int getThiefType() {
    validify();
    return (cast(_Thief*)ptr).thiefType;
  }
  
  ///Whether the thief is alive or not.
  bool isAlive() {
    return (cast(_Thief*)ptr).alive == 1;
  }
  
  ///How many more times this thief can use its special ability.
  int getSpecialsLeft() {
    validify();
    return (cast(_Thief*)ptr).specialsLeft;
  }
  
  ///The maximum number of times this thief can use its special ability.
  int getMaxSpecials() {
    validify();
    return (cast(_Thief*)ptr).maxSpecials;
  }
  
  ///The remaining number of times this thief can move.
  int getMovementLeft() {
    validify();
    return (cast(_Thief*)ptr).movementLeft;
  }
  
  ///The maximum number of times this thief can move.
  int getMaxMovement() {
    validify();
    return (cast(_Thief*)ptr).maxMovement;
  }
  
  ///How many turns this thief is frozen for.
  int getFrozenTurnsLeft() {
    validify();
    return (cast(_Thief*)ptr).frozenTurnsLeft;
  }
  
  ///Allows a thief to display messages on the screen
  bool thiefTalk(string message) {
    validify();
    return thiefThiefTalk((cast(_Thief*)ptr), toUTFz!(char*)(message)) == 1;
  }
  
  ///Commands a thief to move to a new location.
  bool move(int x, int y) {
    validify();
    return thiefMove((cast(_Thief*)ptr), x, y) == 1;
  }
  
  ///Commands a thief to use a special on a location.
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
