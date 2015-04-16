// -*-c++-*-

#ifndef THIEF_H
#define THIEF_H

#include <iostream>
#include "structures.h"

#include "Mappable.h"

///Represents a single thief on the map.
class Thief : public Mappable {
  public:
  Thief(_Thief* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///X position of the object
  int x();
  ///Y position of the object
  int y();
  ///The owner of this thief.
  int owner();
  ///The type of this thief. This type refers to list of thiefTypes.
  int thiefType();
  ///Whether the thief is alive or not.
  int alive();
  ///How many more times this thief can use its special ability.
  int specialsLeft();
  ///The maximum number of times this thief can use its special ability.
  int maxSpecials();
  ///The remaining number of times this thief can move.
  int movementLeft();
  ///The maximum number of times this thief can move.
  int maxMovement();
  ///How many turns this thief is frozen for.
  int frozenTurnsLeft();

  // Actions
  ///Allows a thief to display messages on the screen
  bool thiefTalk(char* message);
  ///Commands a thief to move to a new location.
  bool move(int x, int y);
  ///Commands a thief to use a special on a location.
  bool useSpecial(int x, int y);

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Thief ob);
};

#endif

