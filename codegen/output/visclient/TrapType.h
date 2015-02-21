// -*-c++-*-

#ifndef TRAPTYPE_H
#define TRAPTYPE_H

#include <iostream>
#include "vc_structures.h"


namespace client
{


///Represents a type of trap.
class TrapType {
  public:
  void* ptr;
  TrapType(_TrapType* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///The name of this type of trap.
  char* name();
  ///The type of this trap. This value is unique for all types.
  int type();
  ///The number of scarabs required to purchase this trap.
  int cost();
  ///Whether the trap starts visible to the enemy player.
  int startsVisible();
  ///Whether the trap is able to act().
  int hasAction();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, TrapType ob);
};

}

#endif

