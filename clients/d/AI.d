import BaseAI, TrapType, ThiefType, structures;
import std.typecons, std.stdio;

/**
  The class implementing basic AI logic.
*/
public class AI : BaseAI {
  public:
    this(Connection* conn) {
      super(conn);
    }
  
    override const string username() {
      return "Shell AI";
    }
    
    override const string password() {
      return "password";
    }
    
    /**
      Runs before the first turn.
    */
    override void init() {

    }
    
    /**
      Runs every turn in which you can move.
      Return true to end your turn. Return false to request game information to be resent.
    */
    override bool run() {
      
      return true;
    }
    
    /**
      Runs once the game is over.
    */
    void end() {
    
    }
}
