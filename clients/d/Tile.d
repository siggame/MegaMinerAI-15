import Mappable, structures, std.conv, ExistentialError;

class Tile : Mappable {
  public:
    this(_Tile* pointer) {
      super(cast(_Mappable*)pointer);
    }
    
    override bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (tile; BaseAI.BaseAI.tiles) {
        if(tile.id == id) {
          ptr = tile.ptr;
          iteration = BaseAI.iteration;
          return true;
        }
      }
      throw new ExistentialError();
    }
    
    override int getID() {
      validify();
      return (cast(_Tile*)ptr).id;
    }
    
    override int getX() {
      validify();
      return (cast(_Tile*)ptr).x;
    }
    
    override int getY() {
      validify();
      return (cast(_Tile*)ptr).y;
    }
    
    int getType() {
      validify();
      return (cast(_Tile*)ptr).type;
    }
    
    override string toString() {
      validify();
      _Tile* tile_ptr = cast(_Tile*)ptr;
      return "id: " ~ to!string(tile_ptr.id) ~ "\n" ~
             "x: " ~ to!string(tile_ptr.x) ~ "\n" ~
             "y: " ~ to!string(tile_ptr.y) ~ "\n" ~
             "type: " ~ to!string(tile_ptr.type) ~ "\n";
    }
}
