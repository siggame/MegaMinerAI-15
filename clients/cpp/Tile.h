// -*-c++-*-

#ifndef TILE_H
#define TILE_H

#include <iostream>
#include "structures.h"

#include "Mappable.h"

///Represents a tile.
class Tile : public Mappable {
  public:
  Tile(_Tile* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///X position of the object
  int x();
  ///Y position of the object
  int y();
  ///What type of tile this is. 0: empty, 1: spawn: 2: wall.
  int type();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Tile ob);
};

#endif

