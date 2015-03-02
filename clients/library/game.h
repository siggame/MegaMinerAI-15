//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef GAME_H
#define GAME_H

#include "network.h"
#include "structures.h"

#ifdef _WIN32
#define DLLEXPORT extern "C" __declspec(dllexport)

#ifdef ENABLE_THREADS
#include "pthread.h"
#endif

#else
#define DLLEXPORT

#ifdef ENABLE_THREADS
#include <pthread.h>
#endif

#endif

struct Connection
{
  int socket;
  
  #ifdef ENABLE_THREADS
  pthread_mutex_t mutex;
  #endif
  
  int mapWidth;
  int mapHeight;
  int turnNumber;
  int roundTurnNumber;
  int maxThieves;
  int maxTraps;
  int playerID;
  int gameNumber;
  int roundNumber;
  int scarabsForTraps;
  int scarabsForThieves;
  int maxStack;

  _Player* Players;
  int PlayerCount;
  _Mappable* Mappables;
  int MappableCount;
  _Tile* Tiles;
  int TileCount;
  _Trap* Traps;
  int TrapCount;
  _Thief* Thiefs;
  int ThiefCount;
  _ThiefType* ThiefTypes;
  int ThiefTypeCount;
  _TrapType* TrapTypes;
  int TrapTypeCount;
};

#ifdef __cplusplus
extern "C"
{
#endif
  DLLEXPORT Connection* createConnection();
  DLLEXPORT void destroyConnection(Connection* c);
  DLLEXPORT int serverConnect(Connection* c, const char* host, const char* port);

  DLLEXPORT int serverLogin(Connection* c, const char* username, const char* password);
  DLLEXPORT int createGame(Connection* c);
  DLLEXPORT int joinGame(Connection* c, int id, const char* playerType);

  DLLEXPORT void endTurn(Connection* c);
  DLLEXPORT void getStatus(Connection* c);


//commands

  ///Place the specified trap type at the given location.
  DLLEXPORT int playerPlaceTrap(_Player* object, int x, int y, int trapType);
  ///Place the specified thief type at the given location.
  DLLEXPORT int playerPurchaseThief(_Player* object, int x, int y, int thiefType);
  ///Display a message on the screen.
  DLLEXPORT int playerPharaohTalk(_Player* object, char* message);
  ///Commands a trap to act on a location.
  DLLEXPORT int trapAct(_Trap* object, int x, int y);
  ///Commands a trap to toggle between being activated or not.
  DLLEXPORT int trapToggle(_Trap* object);
  ///Allows a thief to display messages on the screen
  DLLEXPORT int thiefThiefTalk(_Thief* object, char* message);
  ///Commands a thief to move to a new location.
  DLLEXPORT int thiefMove(_Thief* object, int x, int y);
  ///Commands a thief to act on a location.
  DLLEXPORT int thiefAct(_Thief* object, int x, int y);

//derived properties



//accessors

DLLEXPORT int getMapWidth(Connection* c);
DLLEXPORT int getMapHeight(Connection* c);
DLLEXPORT int getTurnNumber(Connection* c);
DLLEXPORT int getRoundTurnNumber(Connection* c);
DLLEXPORT int getMaxThieves(Connection* c);
DLLEXPORT int getMaxTraps(Connection* c);
DLLEXPORT int getPlayerID(Connection* c);
DLLEXPORT int getGameNumber(Connection* c);
DLLEXPORT int getRoundNumber(Connection* c);
DLLEXPORT int getScarabsForTraps(Connection* c);
DLLEXPORT int getScarabsForThieves(Connection* c);
DLLEXPORT int getMaxStack(Connection* c);

DLLEXPORT _Player* getPlayer(Connection* c, int num);
DLLEXPORT int getPlayerCount(Connection* c);

DLLEXPORT _Mappable* getMappable(Connection* c, int num);
DLLEXPORT int getMappableCount(Connection* c);

DLLEXPORT _Tile* getTile(Connection* c, int num);
DLLEXPORT int getTileCount(Connection* c);

DLLEXPORT _Trap* getTrap(Connection* c, int num);
DLLEXPORT int getTrapCount(Connection* c);

DLLEXPORT _Thief* getThief(Connection* c, int num);
DLLEXPORT int getThiefCount(Connection* c);

DLLEXPORT _ThiefType* getThiefType(Connection* c, int num);
DLLEXPORT int getThiefTypeCount(Connection* c);

DLLEXPORT _TrapType* getTrapType(Connection* c, int num);
DLLEXPORT int getTrapTypeCount(Connection* c);



  DLLEXPORT int networkLoop(Connection* c);
#ifdef __cplusplus
}
#endif

#endif
