// -*-c++-*-

#include "Trap.h"
#include "game.h"


Trap::Trap(_Trap* pointer)
{
    ptr = (void*) pointer;
}

int Trap::id()
{
  return ((_Trap*)ptr)->id;
}

int Trap::x()
{
  return ((_Trap*)ptr)->x;
}

int Trap::y()
{
  return ((_Trap*)ptr)->y;
}

int Trap::owner()
{
  return ((_Trap*)ptr)->owner;
}

int Trap::trapType()
{
  return ((_Trap*)ptr)->trapType;
}

int Trap::visible()
{
  return ((_Trap*)ptr)->visible;
}

int Trap::active()
{
  return ((_Trap*)ptr)->active;
}

int Trap::bodyCount()
{
  return ((_Trap*)ptr)->bodyCount;
}


bool Trap::act(int x, int y)
{
  return trapAct( (_Trap*)ptr, x, y);
}

bool Trap::toggle()
{
  return trapToggle( (_Trap*)ptr);
}



std::ostream& operator<<(std::ostream& stream,Trap ob)
{
  stream << "id: " << ((_Trap*)ob.ptr)->id  <<'\n';
  stream << "x: " << ((_Trap*)ob.ptr)->x  <<'\n';
  stream << "y: " << ((_Trap*)ob.ptr)->y  <<'\n';
  stream << "owner: " << ((_Trap*)ob.ptr)->owner  <<'\n';
  stream << "trapType: " << ((_Trap*)ob.ptr)->trapType  <<'\n';
  stream << "visible: " << ((_Trap*)ob.ptr)->visible  <<'\n';
  stream << "active: " << ((_Trap*)ob.ptr)->active  <<'\n';
  stream << "bodyCount: " << ((_Trap*)ob.ptr)->bodyCount  <<'\n';
  return stream;
}
