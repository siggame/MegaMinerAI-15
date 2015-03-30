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
  ///The maximum number of this type of trap that can be placed in a round by a player.
  int maxInstances();
  ///Whether the trap starts visible to the enemy player.
  int startsVisible();
  ///Whether the trap is able to act().
  int hasAction();
  ///Whether the trap can be deactivated by the player, stopping the trap from automatically activating.
  int deactivatable();
  ///The maximum number of times this trap can be activated before being disabled.
  int maxActivations();
  ///This trap activates when a thief moves onto and then off of this tile.
  int activatesOnWalkedThrough();
  ///The maximum number of turns a thief can stay on this tile before it activates.
  int turnsToActivateOnTile();
  ///Whether this trap can be placed inside of walls.
  int canPlaceOnWalls();
  ///Whether this trap can be placed on empty tiles.
  int canPlaceOnOpenTiles();
  ///How many turns a thief will be frozen when this trap activates.
  int freezesForTurns();
  ///Whether this trap kills thieves when activated.
  int killsOnActivate();
  ///How many turns this trap has to wait between activations.
  int cooldown();
  ///When destroyed via dynamite kills adjacent thieves.
  int explosive();
  ///Cannot be passed through, stopping a thief that tries to move onto its tile.
  int unpassable();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, TrapType ob);
};

#endif

