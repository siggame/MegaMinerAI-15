//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef BASEAI_H
#define BASEAI_H

#include <vector>
#include <ctime>
#include "game.h"

#include "Player.h"
#include "Mappable.h"
#include "Tile.h"
#include "Trap.h"
#include "Thief.h"
#include "ThiefType.h"
#include "TrapType.h"

/// \brief A basic AI interface.

///This class implements most the code an AI would need to interface with the lower-level game code.
///AIs should extend this class to get a lot of boiler-plate code out of the way
///The provided AI class does just that.
class BaseAI
{
protected:
  Connection* c;
  std::vector<Player> players;
  std::vector<Mappable> mappables;
  std::vector<Tile> tiles;
  std::vector<Trap> traps;
  std::vector<Thief> thiefs;
  std::vector<ThiefType> thiefTypes;
  std::vector<TrapType> trapTypes;
public:
  ///The width of the total map.
  int mapWidth();
  ///The height of the total map.
  int mapHeight();
  ///The current turn number.
  int turnNumber();
  ///The current turn number for this round.
  int roundTurnNumber();
  ///The maximum number of Thieves allowed per player.
  int maxThieves();
  ///The maximum number of Traps allowed per player.
  int maxTraps();
  ///The id of the current player.
  int playerID();
  ///What number game this is for the server.
  int gameNumber();
  ///What round of the game this is.
  int roundNumber();
  ///The scarabs given to a player to purchase traps per round.
  int scarabsForTraps();
  ///The scarabs given to a player to purchase thieves per round.
  int scarabsForThieves();
  ///The maximum number of thieves per tile.
  int maxStack();
  ///The number of won rounds required to win.
  int roundsToWin();
  ///The maximum number of round turns before a winner is decided.
  int roundTurnLimit();
  
  BaseAI(Connection* c);
  virtual ~BaseAI();
  ///
  ///Make this your username, which should be provided.
  virtual const char* username() = 0;
  ///
  ///Make this your password, which should be provided.
  virtual const char* password() = 0;
  ///
  ///This function is run once, before your first turn.
  virtual void init() = 0;
  ///
  ///This function is called each time it is your turn
  ///Return true to end your turn, return false to ask the server for updated information
  virtual bool run() = 0;
  ///
  ///This function is called after the last turn.
  virtual void end() = 0;


  bool startTurn();
};

#endif
