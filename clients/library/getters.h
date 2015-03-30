#ifndef GETTERS_H 
#define GETTERS_H
#include "structures.h"

#ifdef _WIN32
#define DLLEXPORT extern "C" __declspec(dllexport)
#else
#define DLLEXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

DLLEXPORT int playerGetId(_Player* ptr);
DLLEXPORT char* playerGetPlayerName(_Player* ptr);
DLLEXPORT float playerGetTime(_Player* ptr);
DLLEXPORT int playerGetScarabs(_Player* ptr);
DLLEXPORT int playerGetRoundsWon(_Player* ptr);


DLLEXPORT int mappableGetId(_Mappable* ptr);
DLLEXPORT int mappableGetX(_Mappable* ptr);
DLLEXPORT int mappableGetY(_Mappable* ptr);


DLLEXPORT int tileGetId(_Tile* ptr);
DLLEXPORT int tileGetX(_Tile* ptr);
DLLEXPORT int tileGetY(_Tile* ptr);
DLLEXPORT int tileGetType(_Tile* ptr);


DLLEXPORT int trapGetId(_Trap* ptr);
DLLEXPORT int trapGetX(_Trap* ptr);
DLLEXPORT int trapGetY(_Trap* ptr);
DLLEXPORT int trapGetOwner(_Trap* ptr);
DLLEXPORT int trapGetTrapType(_Trap* ptr);
DLLEXPORT int trapGetVisible(_Trap* ptr);
DLLEXPORT int trapGetActive(_Trap* ptr);
DLLEXPORT int trapGetBodyCount(_Trap* ptr);
DLLEXPORT int trapGetActivationsRemaining(_Trap* ptr);
DLLEXPORT int trapGetTurnsTillActive(_Trap* ptr);


DLLEXPORT int thiefGetId(_Thief* ptr);
DLLEXPORT int thiefGetX(_Thief* ptr);
DLLEXPORT int thiefGetY(_Thief* ptr);
DLLEXPORT int thiefGetOwner(_Thief* ptr);
DLLEXPORT int thiefGetThiefType(_Thief* ptr);
DLLEXPORT int thiefGetAlive(_Thief* ptr);
DLLEXPORT int thiefGetSpecialsLeft(_Thief* ptr);
DLLEXPORT int thiefGetMaxSpecials(_Thief* ptr);
DLLEXPORT int thiefGetMovementLeft(_Thief* ptr);
DLLEXPORT int thiefGetMaxMovement(_Thief* ptr);
DLLEXPORT int thiefGetFrozenTurnsLeft(_Thief* ptr);


DLLEXPORT int thiefTypeGetId(_ThiefType* ptr);
DLLEXPORT char* thiefTypeGetName(_ThiefType* ptr);
DLLEXPORT int thiefTypeGetType(_ThiefType* ptr);
DLLEXPORT int thiefTypeGetCost(_ThiefType* ptr);
DLLEXPORT int thiefTypeGetMaxMovement(_ThiefType* ptr);
DLLEXPORT int thiefTypeGetMaxSpecials(_ThiefType* ptr);
DLLEXPORT int thiefTypeGetMaxInstances(_ThiefType* ptr);


DLLEXPORT int trapTypeGetId(_TrapType* ptr);
DLLEXPORT char* trapTypeGetName(_TrapType* ptr);
DLLEXPORT int trapTypeGetType(_TrapType* ptr);
DLLEXPORT int trapTypeGetCost(_TrapType* ptr);
DLLEXPORT int trapTypeGetMaxInstances(_TrapType* ptr);
DLLEXPORT int trapTypeGetStartsVisible(_TrapType* ptr);
DLLEXPORT int trapTypeGetHasAction(_TrapType* ptr);
DLLEXPORT int trapTypeGetDeactivatable(_TrapType* ptr);
DLLEXPORT int trapTypeGetMaxActivations(_TrapType* ptr);
DLLEXPORT int trapTypeGetActivatesOnWalkedThrough(_TrapType* ptr);
DLLEXPORT int trapTypeGetTurnsToActivateOnTile(_TrapType* ptr);
DLLEXPORT int trapTypeGetCanPlaceOnWalls(_TrapType* ptr);
DLLEXPORT int trapTypeGetCanPlaceOnOpenTiles(_TrapType* ptr);
DLLEXPORT int trapTypeGetFreezesForTurns(_TrapType* ptr);
DLLEXPORT int trapTypeGetKillsOnActivate(_TrapType* ptr);
DLLEXPORT int trapTypeGetCooldown(_TrapType* ptr);
DLLEXPORT int trapTypeGetExplosive(_TrapType* ptr);
DLLEXPORT int trapTypeGetUnpassable(_TrapType* ptr);



#ifdef __cplusplus
}
#endif

#endif
