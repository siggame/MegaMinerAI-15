// -*-c++-*-

#ifndef PLAYER_H
#define PLAYER_H

#include <iostream>
#include "structures.h"


class Player {
  public:
  void* ptr;
  Player(_Player* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///Player's Name
  char* playerName();
  ///Time remaining, updated at start of turn
  float time();
  ///The number of scarabs this player has to purchase traps or thieves.
  int scarabs();
  ///The number of rounds won by this player.
  int roundsWon();
  ///The number of sarcophagi captured by this player this round.
  int sarcophagiCaptured();

  // Actions
  ///Place the specified trap type at the given location.
  bool placeTrap(int x, int y, int trapType);
  ///Place the specified thief type at the given location.
  bool purchaseThief(int x, int y, int thiefType);
  ///Display a message on the screen.
  bool pharaohTalk(char* message);

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Player ob);
};

#endif

