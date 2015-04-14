import Mappable, structures, std.conv;

class Tile : Mappable {
  private _Tile* tile_ptr = null;
  
  public:
  
  this(_Tile* pointer) {
	  super(cast(_Mappable*)pointer);
    tile_ptr = pointer;
  }
  
  override int getID() {
    return tile_ptr.id;
  }
  
  override int getX() {
    return tile_ptr.x;
  }
  
  override int getY() {
    return tile_ptr.y;
  }
  
  int getType() {
    return tile_ptr.type;
  }
  
  override string toString() {
    return "id: " ~ to!string(tile_ptr.id) ~ "\n" ~
           "x: " ~ to!string(tile_ptr.x) ~ "\n" ~
           "y: " ~ to!string(tile_ptr.y) ~ "\n" ~
           "type: " ~ to!string(tile_ptr.type) ~ "\n";
  }
}
