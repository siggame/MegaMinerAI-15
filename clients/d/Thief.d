import Mappable, structures, std.conv, std.string;

class Thief : Mappable {
  private _Thief* thief_ptr = null;
  
  public this(_Thief* thief_ptr) { 
    thief_ptr = pointer;
  }
  
  override int getID() {
    return thief_ptr.id;
  }
  
  override int getX() {
    return thief_ptr.x;
  }
  
  override int getY() {
    return thief_ptr.y;
  }
  
  int getOwner() {
    return thief_ptr.owner;
  }
  
  int getThiefType() {
    return thief_ptr.thiefType;
  }
  
  bool isAlive() {
    return thief_ptr.alive == 1;
  }
  
  int getSpecialsLeft() {
    return thief_ptr.specialsLeft;
  }
  
  int getMaxSpecials() {
    return thief_ptr.maxSpecials;
  }
  
  int getMovementLeft() {
    return thief_ptr.movementLeft;
  }
  
  int getMaxMovement() {
    return thief_ptr.maxMovement;
  }
  
  int getFrozenTurnsLeft() {
    return thief_ptr.frozenTurnsLeft;
  }
  
  bool thiefTalk(string message) {
    return thiefThiefTalk(thief_ptr, message.toStringz());
  }
  
  bool move(int x, int y) {
    return thiefMove(thief_ptr, x, y);
  }
  
  bool useSpecial(int x, int y) {
    return thiefUseSpecial(thief_ptr, x, y);
  }
  
  override string toString() {
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
