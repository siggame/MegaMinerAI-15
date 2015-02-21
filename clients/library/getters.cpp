#include "getters.h"

DLLEXPORT int playerGetId(_Player* ptr)
{
  return ptr->id;
}
DLLEXPORT char* playerGetPlayerName(_Player* ptr)
{
  return ptr->playerName;
}
DLLEXPORT float playerGetTime(_Player* ptr)
{
  return ptr->time;
}
DLLEXPORT int playerGetScarabs(_Player* ptr)
{
  return ptr->scarabs;
}
DLLEXPORT int mappableGetId(_Mappable* ptr)
{
  return ptr->id;
}
DLLEXPORT int mappableGetX(_Mappable* ptr)
{
  return ptr->x;
}
DLLEXPORT int mappableGetY(_Mappable* ptr)
{
  return ptr->y;
}
DLLEXPORT int tileGetId(_Tile* ptr)
{
  return ptr->id;
}
DLLEXPORT int tileGetIsWall(_Tile* ptr)
{
  return ptr->isWall;
}
DLLEXPORT int trapGetId(_Trap* ptr)
{
  return ptr->id;
}
DLLEXPORT int trapGetX(_Trap* ptr)
{
  return ptr->x;
}
DLLEXPORT int trapGetY(_Trap* ptr)
{
  return ptr->y;
}
DLLEXPORT int trapGetOwner(_Trap* ptr)
{
  return ptr->owner;
}
DLLEXPORT int trapGetTrapType(_Trap* ptr)
{
  return ptr->trapType;
}
DLLEXPORT int trapGetVisible(_Trap* ptr)
{
  return ptr->visible;
}
DLLEXPORT int trapGetActive(_Trap* ptr)
{
  return ptr->active;
}
DLLEXPORT int trapGetBodyCount(_Trap* ptr)
{
  return ptr->bodyCount;
}
DLLEXPORT int thiefGetId(_Thief* ptr)
{
  return ptr->id;
}
DLLEXPORT int thiefGetX(_Thief* ptr)
{
  return ptr->x;
}
DLLEXPORT int thiefGetY(_Thief* ptr)
{
  return ptr->y;
}
DLLEXPORT int thiefGetOwner(_Thief* ptr)
{
  return ptr->owner;
}
DLLEXPORT int thiefGetThiefType(_Thief* ptr)
{
  return ptr->thiefType;
}
DLLEXPORT int thiefGetAlive(_Thief* ptr)
{
  return ptr->alive;
}
DLLEXPORT int thiefGetActionsLeft(_Thief* ptr)
{
  return ptr->actionsLeft;
}
DLLEXPORT int thiefGetMaxActions(_Thief* ptr)
{
  return ptr->maxActions;
}
DLLEXPORT int thiefGetMovementLeft(_Thief* ptr)
{
  return ptr->movementLeft;
}
DLLEXPORT int thiefGetMaxMovement(_Thief* ptr)
{
  return ptr->maxMovement;
}
DLLEXPORT int thiefTypeGetId(_ThiefType* ptr)
{
  return ptr->id;
}
DLLEXPORT char* thiefTypeGetName(_ThiefType* ptr)
{
  return ptr->name;
}
DLLEXPORT int thiefTypeGetType(_ThiefType* ptr)
{
  return ptr->type;
}
DLLEXPORT int thiefTypeGetCost(_ThiefType* ptr)
{
  return ptr->cost;
}
DLLEXPORT int thiefTypeGetMaxActions(_ThiefType* ptr)
{
  return ptr->maxActions;
}
DLLEXPORT int thiefTypeGetMaxMovement(_ThiefType* ptr)
{
  return ptr->maxMovement;
}
DLLEXPORT int thiefTypeGetMaxInstances(_ThiefType* ptr)
{
  return ptr->maxInstances;
}
DLLEXPORT int trapTypeGetId(_TrapType* ptr)
{
  return ptr->id;
}
DLLEXPORT char* trapTypeGetName(_TrapType* ptr)
{
  return ptr->name;
}
DLLEXPORT int trapTypeGetType(_TrapType* ptr)
{
  return ptr->type;
}
DLLEXPORT int trapTypeGetCost(_TrapType* ptr)
{
  return ptr->cost;
}
DLLEXPORT int trapTypeGetStartsVisible(_TrapType* ptr)
{
  return ptr->startsVisible;
}
DLLEXPORT int trapTypeGetHasAction(_TrapType* ptr)
{
  return ptr->hasAction;
}

