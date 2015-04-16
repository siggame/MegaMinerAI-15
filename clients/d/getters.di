import structures;

extern (C):

int playerGetId(_Player*);
char* playerGetPlayerName(_Player*);
float playerGetTime(_Player*);
int playerGetScarabs(_Player*);
int playerGetRoundsWon(_Player*);
int playerGetSarcophagiCaptured(_Player*);

int mappableGetId(_Mappable*);
int mappableGetX(_Mappable*);
int mappableGetY(_Mappable*);


int tileGetId(_Tile*);
int tileGetX(_Tile*);
int tileGetY(_Tile*);
int tileGetType(_Tile*);


int trapGetId(_Trap*);
int trapGetX(_Trap*);
int trapGetY(_Trap*);
int trapGetOwner(_Trap*);
int trapGetTrapType(_Trap*);
int trapGetVisible(_Trap*);
int trapGetActive(_Trap*);
int trapGetBodyCount(_Trap*);
int trapGetActivationsRemaining(_Trap*);
int trapGetTurnsTillActive(_Trap*);


int thiefGetId(_Thief*);
int thiefGetX(_Thief*);
int thiefGetY(_Thief*);
int thiefGetOwner(_Thief*);
int thiefGetThiefType(_Thief*);
int thiefGetAlive(_Thief*);
int thiefGetSpecialsLeft(_Thief*);
int thiefGetMaxSpecials(_Thief*);
int thiefGetMovementLeft(_Thief*);
int thiefGetMaxMovement(_Thief*);
int thiefGetFrozenTurnsLeft(_Thief*);


int thiefTypeGetId(_ThiefType*);
char* thiefTypeGetName(_ThiefType*);
int thiefTypeGetType(_ThiefType*);
int thiefTypeGetCost(_ThiefType*);
int thiefTypeGetMaxMovement(_ThiefType*);
int thiefTypeGetMaxSpecials(_ThiefType*);
int thiefTypeGetMaxInstances(_ThiefType*);


int trapTypeGetId(_TrapType*);
char* trapTypeGetName(_TrapType*);
int trapTypeGetType(_TrapType*);
int trapTypeGetCost(_TrapType*);
int trapTypeGetMaxInstances(_TrapType*);
int trapTypeGetStartsVisible(_TrapType*);
int trapTypeGetHasAction(_TrapType*);
int trapTypeGetDeactivatable(_TrapType*);
int trapTypeGetMaxActivations(_TrapType*);
int trapTypeGetActivatesOnWalkedThrough(_TrapType*);
int trapTypeGetTurnsToActivateOnTile(_TrapType*);
int trapTypeGetCanPlaceOnWalls(_TrapType*);
int trapTypeGetCanPlaceOnOpenTiles(_TrapType*);
int trapTypeGetFreezesForTurns(_TrapType*);
int trapTypeGetKillsOnActivate(_TrapType*);
int trapTypeGetCooldown(_TrapType*);
int trapTypeGetExplosive(_TrapType*);
int trapTypeGetUnpassable(_TrapType*);
