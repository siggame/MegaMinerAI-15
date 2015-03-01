// -*-c++-*-

#ifndef TRAPTYPE_H
#define TRAPTYPE_H

#include <iostream>
#include "structures.h"


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
  ///Whether the trap can be activated by the player.
  int activatable();
  ///The maximum number of bodies needed to disable this trap.
  int maxBodyCount();
  ///The maximum number of this type of trap that can be placed in a round by a player.
  int maxInstances();
  ///Thieves who move onto and then off of this tile die.
  int killsOnWalkThrough();
  ///The maximum number of turns a thief can stay on this tile before it dies.
  int turnsToKillOnTile();
  ///Whether this trap can be placed inside of walls.
  int canPlaceInWalls();
  ///Whether this trap can be placed on empty tiles.
  int canPlaceInEmptyTiles();
  ///How many turns a thief will be frozen when this trap activates.
  int freezesForTurns();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, TrapType ob);
};

#endif

