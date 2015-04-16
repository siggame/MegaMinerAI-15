//Copyright (C) 2015 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.d for that

import std.stdio, std.conv, std.string, AI, structures, game, network;

int main(string[] argv) {
  if (argv.length < 2) {
    writeln("Please enter a host name.");
    return 1;
  }
  
  Connection* c;
  c = createConnection();
  
  AI ai = new AI(c);
  
  int gameNumber;
  if (!serverConnect(c, argv[1].toStringz(), "19000")) {
    writeln("Unable to connect to server");
    return 1;
  }
  
  if (!serverLogin(c, ai.username().toStringz(), ai.password().toStringz())) {
    return 1;
  }
  
  if (argv.length < 3) {
    gameNumber = createGame(c);
  }
  else {
    if (!joinGame(c, to!int(argv[2]), "player")) {
      writeln("Error joining game.");
      return 1;
    }
  }
  
  while (networkLoop(c)) {
    if (ai.startTurn()) {
      endTurn(c);
    }
    else {
      getStatus(c);
    }
  }
  
  ai.end();
  
  //Grab a log
  networkLoop(c);
  
  //Grab the end game status
  networkLoop(c);
  
  destroyConnection(c);
  
  return 0;
}
