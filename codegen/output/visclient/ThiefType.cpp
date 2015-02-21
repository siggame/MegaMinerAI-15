// -*-c++-*-

#include "ThiefType.h"
#include "game.h"


namespace client
{

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

int ThiefType::maxActions()
{
  return ((_ThiefType*)ptr)->maxActions;
}

int ThiefType::maxMovement()
{
  return ((_ThiefType*)ptr)->maxMovement;
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
  stream << "maxActions: " << ((_ThiefType*)ob.ptr)->maxActions  <<'\n';
  stream << "maxMovement: " << ((_ThiefType*)ob.ptr)->maxMovement  <<'\n';
  stream << "maxInstances: " << ((_ThiefType*)ob.ptr)->maxInstances  <<'\n';
  return stream;
}

}
