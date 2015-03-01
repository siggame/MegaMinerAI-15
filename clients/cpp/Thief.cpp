// -*-c++-*-

#include "Thief.h"
#include "game.h"


Thief::Thief(_Thief* pointer)
{
    ptr = (void*) pointer;
}

int Thief::id()
{
  return ((_Thief*)ptr)->id;
}

int Thief::x()
{
  return ((_Thief*)ptr)->x;
}

int Thief::y()
{
  return ((_Thief*)ptr)->y;
}

int Thief::owner()
{
  return ((_Thief*)ptr)->owner;
}

int Thief::thiefType()
{
  return ((_Thief*)ptr)->thiefType;
}

int Thief::alive()
{
  return ((_Thief*)ptr)->alive;
}

int Thief::ninjaReflexesLeft()
{
  return ((_Thief*)ptr)->ninjaReflexesLeft;
}

int Thief::maxNinjaReflexes()
{
  return ((_Thief*)ptr)->maxNinjaReflexes;
}

int Thief::movementLeft()
{
  return ((_Thief*)ptr)->movementLeft;
}

int Thief::maxMovement()
{
  return ((_Thief*)ptr)->maxMovement;
}

int Thief::frozenTurnsLeft()
{
  return ((_Thief*)ptr)->frozenTurnsLeft;
}


bool Thief::thiefTalk(char* message)
{
  return thiefThiefTalk( (_Thief*)ptr, message);
}

bool Thief::move(int x, int y)
{
  return thiefMove( (_Thief*)ptr, x, y);
}

bool Thief::act(int x, int y)
{
  return thiefAct( (_Thief*)ptr, x, y);
}



std::ostream& operator<<(std::ostream& stream,Thief ob)
{
  stream << "id: " << ((_Thief*)ob.ptr)->id  <<'\n';
  stream << "x: " << ((_Thief*)ob.ptr)->x  <<'\n';
  stream << "y: " << ((_Thief*)ob.ptr)->y  <<'\n';
  stream << "owner: " << ((_Thief*)ob.ptr)->owner  <<'\n';
  stream << "thiefType: " << ((_Thief*)ob.ptr)->thiefType  <<'\n';
  stream << "alive: " << ((_Thief*)ob.ptr)->alive  <<'\n';
  stream << "ninjaReflexesLeft: " << ((_Thief*)ob.ptr)->ninjaReflexesLeft  <<'\n';
  stream << "maxNinjaReflexes: " << ((_Thief*)ob.ptr)->maxNinjaReflexes  <<'\n';
  stream << "movementLeft: " << ((_Thief*)ob.ptr)->movementLeft  <<'\n';
  stream << "maxMovement: " << ((_Thief*)ob.ptr)->maxMovement  <<'\n';
  stream << "frozenTurnsLeft: " << ((_Thief*)ob.ptr)->frozenTurnsLeft  <<'\n';
  return stream;
}
