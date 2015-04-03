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

int TrapType::maxInstances()
{
  return ((_TrapType*)ptr)->maxInstances;
}

int TrapType::startsVisible()
{
  return ((_TrapType*)ptr)->startsVisible;
}

int TrapType::hasAction()
{
  return ((_TrapType*)ptr)->hasAction;
}

int TrapType::deactivatable()
{
  return ((_TrapType*)ptr)->deactivatable;
}

int TrapType::maxActivations()
{
  return ((_TrapType*)ptr)->maxActivations;
}

int TrapType::activatesOnWalkedThrough()
{
  return ((_TrapType*)ptr)->activatesOnWalkedThrough;
}

int TrapType::turnsToActivateOnTile()
{
  return ((_TrapType*)ptr)->turnsToActivateOnTile;
}

int TrapType::canPlaceOnWalls()
{
  return ((_TrapType*)ptr)->canPlaceOnWalls;
}

int TrapType::canPlaceOnOpenTiles()
{
  return ((_TrapType*)ptr)->canPlaceOnOpenTiles;
}

int TrapType::freezesForTurns()
{
  return ((_TrapType*)ptr)->freezesForTurns;
}

int TrapType::killsOnActivate()
{
  return ((_TrapType*)ptr)->killsOnActivate;
}

int TrapType::cooldown()
{
  return ((_TrapType*)ptr)->cooldown;
}

int TrapType::explosive()
{
  return ((_TrapType*)ptr)->explosive;
}

int TrapType::unpassable()
{
  return ((_TrapType*)ptr)->unpassable;
}




std::ostream& operator<<(std::ostream& stream,TrapType ob)
{
  stream << "id: " << ((_TrapType*)ob.ptr)->id  <<'\n';
  stream << "name: " << ((_TrapType*)ob.ptr)->name  <<'\n';
  stream << "type: " << ((_TrapType*)ob.ptr)->type  <<'\n';
  stream << "cost: " << ((_TrapType*)ob.ptr)->cost  <<'\n';
  stream << "maxInstances: " << ((_TrapType*)ob.ptr)->maxInstances  <<'\n';
  stream << "startsVisible: " << ((_TrapType*)ob.ptr)->startsVisible  <<'\n';
  stream << "hasAction: " << ((_TrapType*)ob.ptr)->hasAction  <<'\n';
  stream << "deactivatable: " << ((_TrapType*)ob.ptr)->deactivatable  <<'\n';
  stream << "maxActivations: " << ((_TrapType*)ob.ptr)->maxActivations  <<'\n';
  stream << "activatesOnWalkedThrough: " << ((_TrapType*)ob.ptr)->activatesOnWalkedThrough  <<'\n';
  stream << "turnsToActivateOnTile: " << ((_TrapType*)ob.ptr)->turnsToActivateOnTile  <<'\n';
  stream << "canPlaceOnWalls: " << ((_TrapType*)ob.ptr)->canPlaceOnWalls  <<'\n';
  stream << "canPlaceOnOpenTiles: " << ((_TrapType*)ob.ptr)->canPlaceOnOpenTiles  <<'\n';
  stream << "freezesForTurns: " << ((_TrapType*)ob.ptr)->freezesForTurns  <<'\n';
  stream << "killsOnActivate: " << ((_TrapType*)ob.ptr)->killsOnActivate  <<'\n';
  stream << "cooldown: " << ((_TrapType*)ob.ptr)->cooldown  <<'\n';
  stream << "explosive: " << ((_TrapType*)ob.ptr)->explosive  <<'\n';
  stream << "unpassable: " << ((_TrapType*)ob.ptr)->unpassable  <<'\n';
  return stream;
}
