class ExistentialError : Error {
  public this() {
    super("Object does not exist anymore.");
  }
}
