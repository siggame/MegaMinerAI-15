// -*-c++-*-

#include "TrapType.h"
#include "game.h"


TrapType::TrapType(_TrapType* pointer)
{
    ptr = (void*) pointer;
}

int TrapType::id()
{
  return ((_TrapType*)ptr)->id;
}

char* TrapType::name()
{
  return ((_TrapType*)ptr)->name;
}

int TrapType::type()
{
  return ((_TrapType*)ptr)->type;
}

int TrapType::cost()
{
  return ((_TrapType*)ptr)->cost;
}

int TrapType::startsVisible()
{
  return ((_TrapType*)ptr)->startsVisible;
}

int TrapType::hasAction()
{
  return ((_TrapType*)ptr)->hasAction;
}

int TrapType::activatable()
{
  return ((_TrapType*)ptr)->activatable;
}

int TrapType::maxBodyCount()
{
  return ((_TrapType*)ptr)->maxBodyCount;
}

int TrapType::maxInstances()
{
  return ((_TrapType*)ptr)->maxInstances;
}

int TrapType::killsOnWalkThrough()
{
  return ((_TrapType*)ptr)->killsOnWalkThrough;
}

int TrapType::turnsToKillOnTile()
{
  return ((_TrapType*)ptr)->turnsToKillOnTile;
}

int TrapType::canPlaceInWalls()
{
  return ((_TrapType*)ptr)->canPlaceInWalls;
}

int TrapType::canPlaceInEmptyTiles()
{
  return ((_TrapType*)ptr)->canPlaceInEmptyTiles;
}

int TrapType::freezesForTurns()
{
  return ((_TrapType*)ptr)->freezesForTurns;
}




std::ostream& operator<<(std::ostream& stream,TrapType ob)
{
  stream << "id: " << ((_TrapType*)ob.ptr)->id  <<'\n';
  stream << "name: " << ((_TrapType*)ob.ptr)->name  <<'\n';
  stream << "type: " << ((_TrapType*)ob.ptr)->type  <<'\n';
  stream << "cost: " << ((_TrapType*)ob.ptr)->cost  <<'\n';
  stream << "startsVisible: " << ((_TrapType*)ob.ptr)->startsVisible  <<'\n';
  stream << "hasAction: " << ((_TrapType*)ob.ptr)->hasAction  <<'\n';
  stream << "activatable: " << ((_TrapType*)ob.ptr)->activatable  <<'\n';
  stream << "maxBodyCount: " << ((_TrapType*)ob.ptr)->maxBodyCount  <<'\n';
  stream << "maxInstances: " << ((_TrapType*)ob.ptr)->maxInstances  <<'\n';
  stream << "killsOnWalkThrough: " << ((_TrapType*)ob.ptr)->killsOnWalkThrough  <<'\n';
  stream << "turnsToKillOnTile: " << ((_TrapType*)ob.ptr)->turnsToKillOnTile  <<'\n';
  stream << "canPlaceInWalls: " << ((_TrapType*)ob.ptr)->canPlaceInWalls  <<'\n';
  stream << "canPlaceInEmptyTiles: " << ((_TrapType*)ob.ptr)->canPlaceInEmptyTiles  <<'\n';
  stream << "freezesForTurns: " << ((_TrapType*)ob.ptr)->freezesForTurns  <<'\n';
  return stream;
}
