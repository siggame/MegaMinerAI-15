// -*-c++-*-

#ifndef TILE_H
#define TILE_H

#include <iostream>
#include "vc_structures.h"


namespace client
{


///Represents a tile.
class Tile {
  public:
  void* ptr;
  Tile(_Tile* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///Whether this tile is a wall or not.
  int isWall();

  // Actions

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Tile ob);
};

}

#endif

