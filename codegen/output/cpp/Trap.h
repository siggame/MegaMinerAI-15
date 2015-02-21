// -*-c++-*-

#ifndef TRAP_H
#define TRAP_H

#include <iostream>
#include "structures.h"

#include "Mappable.h"

///Represents a single trap on the map.
class Trap : public Mappable {
  public:
  Trap(_Trap* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///X position of the object
  int x();
  ///Y position of the object
  int y();
  ///The owner of this trap.
  int owner();
  ///The type of this trap. This type refers to list of trapTypes.
  int trapType();
  ///Whether the trap is visible to the enemy player.
  int visible();
  ///Whether the trap is active.
  int active();
  ///How many thieves this trap has killed.
  int bodyCount();

  // Actions
  ///Commands a trap to act on a location.
  bool act(int x, int y);
  ///Commands a trap to toggle between being activated or not.
  bool toggle();

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Trap ob);
};

#endif

