import Mappable, structures, std.conv, ExistentialError;

public static const int EMPTY = 0;
public static const int SPAWN = 1;
public static const int WALL = 2;

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
    
    ///Unique identifier
    override int getID() {
      validify();
      return (cast(_Tile*)ptr).id;
    }
    
    ///X position of the object
    override int getX() {
      validify();
      return (cast(_Tile*)ptr).x;
    }
    
    ///Y position of the object
    override int getY() {
      validify();
      return (cast(_Tile*)ptr).y;
    }
    
    ///What type of tile this is. 0: empty, 1: spawn: 2: wall.
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
