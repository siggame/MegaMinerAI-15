import structures, std.conv, getters, BaseAI, ExistentialError;

class Mappable { 
  protected:
    _Mappable* ptr;
    int id, iteration;
    
  public:  
    this(_Mappable* pointer) {
      ptr = pointer;
      id = mappableGetId(pointer);
      iteration = BaseAI.iteration;
    }
    
    bool validify() {
      if (iteration == BaseAI.iteration) return true;
      foreach (mappable; BaseAI.BaseAI.mappables) {
        if (mappable.id == id) {
          ptr = mappable.ptr;
          iteration = BaseAI.iteration;
          return true;
        }
      }
      throw new ExistentialError();
    }
    
    int getID() {
      validify();
      return ptr.id;
    }
    
    int getX() {
      validify();
      return ptr.x;
    }
    
    int getY() {
      validify();
      return ptr.y;
    }
    
    override string toString() {
      validify();
      return "id: " ~ to!string(ptr.id) ~ "\n" ~
             "x: " ~ to!string(ptr.x) ~ "\n" ~
             "y: " ~ to!string(ptr.y) ~ "\n";
    }
}
