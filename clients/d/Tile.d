import Mappable, structures, std.conv;

class Tile : Mappable {
  private _Tile* tile_ptr = null;
  
  public:
  
  this(_Tile* pointer) {
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
    tile_ptr.type;
  }
  
  override string toString() {
    return "id: " ~ to!string(tile_ptr.id) ~ "\n" ~
           "x: " ~ to!string(tile_ptr.name) ~ "\n" ~
           "y: " ~ to!string(tile_ptr.cost) ~ "\n" ~
           "type: " ~ to!string(tile_ptr.type) ~ "\n";
  }
}
