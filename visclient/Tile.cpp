// -*-c++-*-

#include "Tile.h"
#include "game.h"


namespace client
{

Tile::Tile(_Tile* pointer)
{
    ptr = (void*) pointer;
}

int Tile::id()
{
  return ((_Tile*)ptr)->id;
}

int Tile::isWall()
{
  return ((_Tile*)ptr)->isWall;
}




std::ostream& operator<<(std::ostream& stream,Tile ob)
{
  stream << "id: " << ((_Tile*)ob.ptr)->id  <<'\n';
  stream << "isWall: " << ((_Tile*)ob.ptr)->isWall  <<'\n';
  return stream;
}

}
