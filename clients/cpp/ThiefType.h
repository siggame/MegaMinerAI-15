// -*-c++-*-

#ifndef THIEFTYPE_H
#define THIEFTYPE_H

#include <iostream>
#include "structures.h"


///Represents a type of thief.
class ThiefType {
  public:
  static const int BOMBER = 0;
  static const int DIGGER = 1;
  static const int NINJA = 2;
  static const int GUIDE = 3;
  static const int SLAVE = 4;
  
  void* ptr;
  ThiefType(_ThiefType* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///The name of this type of thief.
  char* name();
  ///The type of this thief. This value is unique for all types.
  int type();
  ///The number of scarabs required to purchase this thief.
  int cost();
  ///The maximum number of times this thief can move.
  int maxMovement();
  ///The maximum number of times this thief can use its special ability.
  int maxSpecials();
  ///The maximum number of this type thief that can be purchased each round.
  int maxInstances();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, ThiefType ob);
};

#endif

