// -*-c++-*-

#include "ThiefType.h"
#include "game.h"


ThiefType::ThiefType(_ThiefType* pointer)
{
    ptr = (void*) pointer;
}

int ThiefType::id()
{
  return ((_ThiefType*)ptr)->id;
}

char* ThiefType::name()
{
  return ((_ThiefType*)ptr)->name;
}

int ThiefType::type()
{
  return ((_ThiefType*)ptr)->type;
}

int ThiefType::cost()
{
  return ((_ThiefType*)ptr)->cost;
}

int ThiefType::maxMovement()
{
  return ((_ThiefType*)ptr)->maxMovement;
}

int ThiefType::maxNinjaReflexes()
{
  return ((_ThiefType*)ptr)->maxNinjaReflexes;
}

int ThiefType::maxInstances()
{
  return ((_ThiefType*)ptr)->maxInstances;
}




std::ostream& operator<<(std::ostream& stream,ThiefType ob)
{
  stream << "id: " << ((_ThiefType*)ob.ptr)->id  <<'\n';
  stream << "name: " << ((_ThiefType*)ob.ptr)->name  <<'\n';
  stream << "type: " << ((_ThiefType*)ob.ptr)->type  <<'\n';
  stream << "cost: " << ((_ThiefType*)ob.ptr)->cost  <<'\n';
  stream << "maxMovement: " << ((_ThiefType*)ob.ptr)->maxMovement  <<'\n';
  stream << "maxNinjaReflexes: " << ((_ThiefType*)ob.ptr)->maxNinjaReflexes  <<'\n';
  stream << "maxInstances: " << ((_ThiefType*)ob.ptr)->maxInstances  <<'\n';
  return stream;
}
