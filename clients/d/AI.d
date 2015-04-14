import BaseAI, structures;

public class AI : BaseAI {
  public:
    this(Connection* conn) {
      super(conn);
    }
  
    override string getUsername() const {
      return "Shell AI";
    }
    
    override string getPassword() const {
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
