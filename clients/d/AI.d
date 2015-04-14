import BaseAI, structures;

public class AI : BaseAI {
  public:
    this(Connection* conn) {
      super(conn);
    }
  
    override const string getUsername() {
      return "Shell AI";
    }
    
    override const string getPassword() {
      return "password";
    }
    
    override void init() {
    
    }
    
    override bool run() {
      
      return true;
    }
    
    void end() {
    
    }
}
