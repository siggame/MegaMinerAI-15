import structures, std.conv;

class Mappable {
  private _Mappable* ptr;
  
  public:
  
  this(_Mappable* pointer) {
    ptr = pointer;
  }
  
  int getID() {
    return ptr.id;
  }
  
  int getX() {
    return ptr.x;
  }
  
  int getY() {
    return ptr.y;
  }
  
  override string toString() {
    return "id: " ~ to!string(ptr.id) ~ "\n" ~
           "x: " ~ to!string(ptr.x) ~ "\n" ~
           "y: " ~ to!string(ptr.y) ~ "\n";
  }
}
