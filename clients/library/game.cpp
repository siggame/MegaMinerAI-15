//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#pragma warning(disable : 4996)

#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <cmath>
#include <map>

#include "game.h"
#include "network.h"
#include "structures.h"

#include "sexp/sfcompat.h"

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#ifdef _WIN32
//Doh, namespace collision.
namespace Windows
{
    #include <Windows.h>
};
#else
#include <unistd.h>
#endif

#ifdef ENABLE_THREADS
#define LOCK(X) pthread_mutex_lock(X)
#define UNLOCK(X) pthread_mutex_unlock(X)
#else
#define LOCK(X)
#define UNLOCK(X)
#endif

using std::cout;
using std::cerr;
using std::endl;
using std::stringstream;
using std::string;
using std::ofstream;
using std::abs;

DLLEXPORT Connection* createConnection()
{
  Connection* c = new Connection;
  c->socket = -1;
  #ifdef ENABLE_THREADS
  pthread_mutex_init(&c->mutex, NULL);
  #endif

  c->mapWidth = 0;
  c->mapHeight = 0;
  c->turnNumber = 0;
  c->roundTurnNumber = 0;
  c->maxThieves = 0;
  c->maxTraps = 0;
  c->playerID = 0;
  c->gameNumber = 0;
  c->roundNumber = 0;
  c->scarabsForTraps = 0;
  c->scarabsForThieves = 0;
  c->roundsToWin = 0;
  c->roundTurnLimit = 0;
  c->numberOfSarcophagi = 0;
  c->Players = NULL;
  c->PlayerCount = 0;
  c->Mappables = NULL;
  c->MappableCount = 0;
  c->Tiles = NULL;
  c->TileCount = 0;
  c->Traps = NULL;
  c->TrapCount = 0;
  c->Thiefs = NULL;
  c->ThiefCount = 0;
  c->ThiefTypes = NULL;
  c->ThiefTypeCount = 0;
  c->TrapTypes = NULL;
  c->TrapTypeCount = 0;
  return c;
}

DLLEXPORT void destroyConnection(Connection* c)
{
  #ifdef ENABLE_THREADS
  pthread_mutex_destroy(&c->mutex);
  #endif
  if(c->Players)
  {
    for(int i = 0; i < c->PlayerCount; i++)
    {
      delete[] c->Players[i].playerName;
    }
    delete[] c->Players;
  }
  if(c->Mappables)
  {
    for(int i = 0; i < c->MappableCount; i++)
    {
    }
    delete[] c->Mappables;
  }
  if(c->Tiles)
  {
    for(int i = 0; i < c->TileCount; i++)
    {
    }
    delete[] c->Tiles;
  }
  if(c->Traps)
  {
    for(int i = 0; i < c->TrapCount; i++)
    {
    }
    delete[] c->Traps;
  }
  if(c->Thiefs)
  {
    for(int i = 0; i < c->ThiefCount; i++)
    {
    }
    delete[] c->Thiefs;
  }
  if(c->ThiefTypes)
  {
    for(int i = 0; i < c->ThiefTypeCount; i++)
    {
      delete[] c->ThiefTypes[i].name;
    }
    delete[] c->ThiefTypes;
  }
  if(c->TrapTypes)
  {
    for(int i = 0; i < c->TrapTypeCount; i++)
    {
      delete[] c->TrapTypes[i].name;
    }
    delete[] c->TrapTypes;
  }
  delete c;
}

DLLEXPORT int serverConnect(Connection* c, const char* host, const char* port)
{
  c->socket = open_server_connection(host, port);
  return c->socket + 1; //false if socket == -1
}

DLLEXPORT int serverLogin(Connection* c, const char* username, const char* password)
{
  string expr = "(login \"";
  expr += username;
  expr += "\" \"";
  expr += password;
  expr +="\")";

  send_string(c->socket, expr.c_str());

  sexp_t* expression, *message;

  char* reply = rec_string(c->socket);
  expression = extract_sexpr(reply);
  delete[] reply;

  message = expression->list;
  if(message->val == NULL || strcmp(message->val, "login-accepted") != 0)
  {
    cerr << "Unable to login to server" << endl;
    destroy_sexp(expression);
    return 0;
  }
  destroy_sexp(expression);
  return 1;
}

DLLEXPORT int createGame(Connection* c)
{
  sexp_t* expression, *number;

  send_string(c->socket, "(create-game)");

  char* reply = rec_string(c->socket);
  expression = extract_sexpr(reply);
  delete[] reply;

  number = expression->list->next;
  c->gameNumber = atoi(number->val);
  destroy_sexp(expression);

  std::cout << "Creating game " << c->gameNumber << endl;

  c->playerID = 0;

  return c->gameNumber;
}

DLLEXPORT int joinGame(Connection* c, int gameNum, const char* playerType)
{
  sexp_t* expression;
  stringstream expr;

  c->gameNumber = gameNum;

  expr << "(join-game " << c->gameNumber << " "<< playerType << ")";
  send_string(c->socket, expr.str().c_str());

  char* reply = rec_string(c->socket);
  expression = extract_sexpr(reply);
  delete[] reply;

  if(strcmp(expression->list->val, "join-accepted") == 0)
  {
    destroy_sexp(expression);
    c->playerID = 1;
    send_string(c->socket, "(game-start)");
    return 1;
  }
  else if(strcmp(expression->list->val, "create-game") == 0)
  {
    std::cout << "Game did not exist, creating game " << c->gameNumber << endl;
    destroy_sexp(expression);
    c->playerID = 0;
    return 1;
  }
  else
  {
    cerr << "Cannot join game "<< c->gameNumber << ": " << expression->list->next->val << endl;
    destroy_sexp(expression);
    return 0;
  }
}

DLLEXPORT void endTurn(Connection* c)
{
  LOCK( &c->mutex );
  send_string(c->socket, "(end-turn)");
  UNLOCK( &c->mutex );
}

DLLEXPORT void getStatus(Connection* c)
{
  LOCK( &c->mutex );
  send_string(c->socket, "(game-status)");
  UNLOCK( &c->mutex );
}

struct Point
{
  int x; int y;
  Point(int x, int y):
  x(x),
  y(y)
  {}
};

static std::vector<Point> trapsThisTurn;
static std::vector<int> trapInstanceCount;
static int turnNo = -1;

DLLEXPORT int playerPlaceTrap(_Player* object, int x, int y, int trapType)
{
  stringstream expr;
  expr << "(game-place-trap " << object->id
       << " " << x
       << " " << y
       << " " << trapType
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  Connection* c = object->_c;
  int trapMoney = object->scarabs;

  
  //after trap phase
  if (c->roundTurnNumber > 1)
    return 0;
    
  if (turnNo != c->turnNumber)
  {
    turnNo = c->turnNumber;
    trapsThisTurn.clear();
    trapInstanceCount.clear();
    trapInstanceCount.resize(c->TrapTypeCount, 0);

    for (int i = 0; i < c->TrapCount; ++i)
    {
      if(getTrap(c, i)->owner == object->id)
      {
        _TrapType* junk;
        for(int i = 0; i < c->TrapTypeCount; ++i)
        {
          junk = getTrapType(c, i);
          if(junk->type == getTrap(c, i)->trapType)
          {
            break;
          }
        }
        trapInstanceCount[junk->type] += 1;
      }
    }
  }
  
    
  //out of bounds
  if(x < 0 || x >= c->mapWidth || y < 0 || y >= c->mapHeight)
    return 0;

  //wrong pyramid
  int width = c->mapWidth/2;
  int minX = object->id * width;
  if(x < minX || x >= minX + width)
    return 0;

  //already trap here
  for (int i = 0; i < c->TrapCount; ++i)
  {
    _Trap* t = getTrap(c, i);
    if(t->x == x && t->y == y)
      return 0;
  }
  for (int i = 0; i < trapsThisTurn.size(); ++i)
    if(trapsThisTurn[i].x == x && trapsThisTurn[i].y == y)
      return 0;

  //invalid type
  if(trapType < 0 or trapType >= c->TrapTypeCount)
    return 0;

  _TrapType* type;
  for(int i = 0; i < c->TrapTypeCount; ++i)
  {
    type = getTrapType(c, i);
    if(type->type == trapType)
    {
      break;
    }
  }

  _Tile* tile;
  for (int i = 0; i < c->TileCount; ++i)
  {
    tile = getTile(c, i);
    if(tile->x == x && tile->y == y)
      break;
  }

  //cant place on wall
  if(tile->type == 2 && type->canPlaceOnWalls != 1)
    return 0;

  //must place on wall
  if(tile->type == 0 && type->canPlaceOnOpenTiles != 1)
    return 0;

  if(trapType != 0)
  {
    // cant spawn anymore
    if(trapInstanceCount[trapType] >= type->maxInstances)
      return 0;
  }

  //not enough money
  if(trapMoney < type->cost)
    return 0;
    
  // Move sarcophagus
  if (trapType == 0)
  {
    for (int i = 0; i < c->TrapCount; ++i)
    {
      _Trap* t = getTrap(c, i);
      if(t->trapType == 0 && t->turnsTillActive == 0)
      {
        t->x = x;
        t->y = y;
        t->turnsTillActive = 1;
        break;
      }
    }
  }

  trapsThisTurn.push_back(Point(x, y));
  trapInstanceCount[trapType] += 1;
  object->scarabs -= type->cost;
  
  return 1;
}

static std::vector<int> thiefInstanceCount;

DLLEXPORT int playerPurchaseThief(_Player* object, int x, int y, int thiefType)
{
  stringstream expr;
  expr << "(game-purchase-thief " << object->id
       << " " << x
       << " " << y
       << " " << thiefType
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  int thiefMoney = object->scarabs;

  Connection* c = object->_c;

  //trap phase
  if(c->roundTurnNumber < 2)
    return 0;

  if (turnNo != c->turnNumber)
  {
    turnNo = c->turnNumber;
    thiefInstanceCount.resize(c->ThiefTypeCount, 0);

    for (int i = 0; i < c->ThiefCount; ++i)
    {
      if(getThief(c, i)->owner == object->id)
      {
        _ThiefType* type;
        for(int i2 = 0; i2 < c->ThiefTypeCount; ++i2)
        {
          type = getThiefType(c, i2);
          if(getThief(c, i)->thiefType == type->type)
          {
            break;
          }
        }
        thiefInstanceCount[type->type] += 1;
      }
    }
  }

  //out of bounds
  if(x < 0 || x >= c->mapWidth || y < 0 || y >= c->mapHeight)
    return 0;

  //wrong pyramid
  int width = c->mapWidth/2;
  int minX = (object->id == 1) ? 0 : width;
  if(x < minX || x >= minX + width)
    return 0;

  //not spawn
  for (int i = 0; i < c->TileCount; ++i)
  {
    _Tile* t = getTile(c, i);
    if(t->x == x && t->y == y)
    {
      if(t->type != 1)
        return 0;
      else
        break;
    }
  }

  // invalid type
  if(thiefType < 0 || thiefType >= c->ThiefTypeCount)
    return 0;

  _ThiefType* type;
  for(int i = 0; i < c->ThiefTypeCount; ++i)
  {
    type = getThiefType(c, i);
    if(type->type == thiefType)
    {
      break;
    }
  }

  if(thiefMoney < type->cost)
    return 0;

  if(thiefInstanceCount[thiefType] >= type->maxInstances)
    return 0;
  
  thiefInstanceCount[thiefType] += 1;
  object->scarabs -= type->cost;
  return 1;
}

DLLEXPORT int playerPharaohTalk(_Player* object, char* message)
{
  stringstream expr;
  expr << "(game-pharaoh-talk " << object->id
      << " \"" << escape_string(message) << "\""
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);
  return 1;
}

DLLEXPORT int trapAct(_Trap* object, int x, int y)
{
  stringstream expr;
  expr << "(game-act " << object->id
       << " " << x
       << " " << y
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  static std::map<int, bool> hasMoved;

  Connection* c = object->_c;

  if(turnNo != c->turnNumber)
  {
    hasMoved.clear();
  }

  //proper owner
  if(object->owner != c->playerID)
    return 0;

  //has action
  if(object->activationsRemaining <= 0)
    return 0;

  //not on cooldown
  if(object->turnsTillActive > 0)
    return 0;

  //active
  if(object->active != 1)
    return 0;

  //boulder roll
  if(object->trapType == 3)
  {
    //adjacent target
    if(abs(x) + abs(y) != 1)
      return 0;

    int deathX = object->x;
    int deathY = object->y;
    _Tile* tile;

    do
    {
      //get tile
      for(int i = 0; i < c->TileCount; ++i)
      {
        tile = getTile(c, i);
        if(tile->x == deathX && tile->y == deathY)
        {
          break;
        }
      }
      for(int i = 0; i < c->ThiefCount; ++i)
      {
        _Thief* thief = getThief(c, i);
        if(thief->x == deathX && thief->y == deathY)
        { 
          if(thief->thiefType == 2 && thief->specialsLeft > 0)
          {
            --thief->specialsLeft;
          }
          else
          {
            thief->alive = false;
          }
        }
      }
      deathX += x;
      deathY += y;
    }while(tile->type != 2);
  }

  //mummy
  if(object->trapType == 10)
  {
    //has already moved
    if(hasMoved[object->id])
    {
      return 0;
    }
    //adjacent target
    if(abs(object->x - x) + abs(object->y - y) != 1)
      return 0;

    //out of bounds
    if(x < 0 || x >= c->mapWidth || y < 0 || y >= c->mapHeight)
      return 0;

    //moving on empty tile
    for (int i = 0; i < c->TileCount; ++i)
    {
      _Tile* t = getTile(c, i);
      if(t->x == x && t->y == y)
      {
        if(t->type != 0)
          return 0;
        else
          break;
      }
    }
    object->x = x;
    object->y = y;
    hasMoved[object->id] = true;
    for(int i = 0; i < c->ThiefCount; ++i)
    {
      _Thief* thief = getThief(c, i);
      if(thief->x == x && thief->y == y)
      {
        if(thief->thiefType == 2 && thief->specialsLeft > 0)
        {
          --thief->specialsLeft;
        }
        else
        {
          thief->alive = false;
        }
      }
    }
  }

  object->activationsRemaining -= 1;
  _TrapType* trap;
  for(int i = 0; i < c->TrapTypeCount; ++i)
  {
    trap = getTrapType(c, i);
    if(trap->type == object->trapType)
    {
      break;
    }
  }
  if(object->activationsRemaining == 0)
  {
    object->active = 0;
  }
  else if(trap->cooldown)
  {
    object->active = 0;
    object->turnsTillActive = trap->cooldown;
  }

  return 1;
}

DLLEXPORT int trapToggle(_Trap* object)
{
  stringstream expr;
  expr << "(game-toggle " << object->id
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  Connection* c = object->_c;

  _TrapType* trap;
  for(int i = 0; i < c->TrapTypeCount; ++i)
  {
    trap = getTrapType(c, i);
    if(trap->type == object->trapType)
    {
      break;
    }
  }
  if(trap->deactivatable != 1)
    return 0;
  else if(!object->active && object->activationsRemaining == 0)
    return 0;
  else if(!object->active && object->turnsTillActive >0)
    return 0;

  if(object->active)
  {
    object->active = 0;
  }
  else if(object->activationsRemaining && object->turnsTillActive == 0)
  {
    object->active = 1;
  }

  return 1;
}


DLLEXPORT int thiefThiefTalk(_Thief* object, char* message)
{
  stringstream expr;
  expr << "(game-thief-talk " << object->id
      << " \"" << escape_string(message) << "\""
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);
  return 1;
}

DLLEXPORT int thiefMove(_Thief* object, int x, int y)
{
  stringstream expr;
  expr << "(game-move " << object->id
       << " " << x
       << " " << y
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  Connection* c = object->_c;

  //proper owner
  if(object->owner != c->playerID)
  {
    return 0;
  }

  //alive
  if(object->alive == 0)
  {
    return 0;
  }

  //not frozen
  if(object->frozenTurnsLeft > 0)
  {
    return 0;
  }

  //can move
  if(object->movementLeft <= 0)
  {
    return 0;
  }

  //out of bounds
  if(x < 0 || x >= c->mapWidth || y < 0 || y >= c->mapHeight)
  {
    return 0;
  }

  //wrong pyramid
  int width = c->mapWidth/2;
  int minX = (object->owner == 1) ? 0 : width;
  if(x < minX || x >= minX + width)
  {
    return 0;
  }

  //not moving on wall
  for (int i = 0; i < c->TileCount; ++i)
  {
    _Tile* t = getTile(c, i);
    if(t->x == x && t->y == y)
    {
      if(t->type == 2)
      {
        return 0;
      }
      else
        break;
    }
  }

  //move one space
  if(abs(object->x - x) + abs(object->y - y) != 1)
  {
    return 0;
  }

  //check for activatesOnWalkedThrough
  //check for traps on the tile
  _Trap* trap = 0;
  _Trap* lastTrap = 0;
  for(int i = 0; i < c->TrapCount; ++i)
  {
    trap = getTrap(c, i);
    if(trap->x == x && trap->y == y)
    {
      break;
    }
    trap = 0;
  }
  for(int i = 0; i < c->TrapCount; ++i)
  {
    lastTrap = getTrap(c, i);
    if(lastTrap->x == object->x && lastTrap->y == object->y)
    {
      break;
    }
    lastTrap = 0;
  }
  if(lastTrap != 0)
  {
    //make sure it's active and all that
    _TrapType* trapType;
    for(int i = 0; i < c->TrapTypeCount; ++i)
    {
      trapType = getTrapType(c, i);
      if(trapType->type == lastTrap->trapType)
      {
        break;
      }
    }
    if(lastTrap->active && trapType->activatesOnWalkedThrough && trapType->turnsToActivateOnTile == 0 && object->movementLeft < object->maxMovement)
    {
      --lastTrap->activationsRemaining;
      if(lastTrap->activationsRemaining == 0)
      {
        lastTrap->active = 0;
      }
      else if(trapType->cooldown)
      {
        lastTrap->active = 0;
        lastTrap->turnsTillActive = trapType->cooldown;
      }
      if(object->thiefType == 2 && object->specialsLeft > 0)
      {
        --object->specialsLeft;
      }
      else
      {
        if(trapType->killsOnActivate)
        {
          object->alive = false;
        }
      }
    }
  }
  //blocking trap
  if(trap != 0)
  {
    //make sure it's active and all that
    _TrapType* trapType;
    for(int i = 0; i < c->TrapTypeCount; ++i)
    {
      trapType = getTrapType(c, i);
      if(trapType->type == trap->trapType)
      {
        break;
      }
    }
    if(trap->active && trapType->unpassable)
    {
      --object->movementLeft;
      --trap->activationsRemaining;
      if(trap->activationsRemaining <= 0)
      {
        trap->active = 0;
      }
      return 1;
    }
    //on move trap
    else if(trap->active && trapType->activatesOnWalkedThrough && trapType->turnsToActivateOnTile == 1)
    {
      --trap->activationsRemaining;
      if(trap->activationsRemaining == 0)
      {
        trap->active = 0;
      }
      else if(trapType->cooldown)
      {
        trap->active = 0;
        trap->turnsTillActive = trapType->cooldown;
      }
      if(object->thiefType == 2 && object->specialsLeft > 0)
      {
        --object->specialsLeft;
      }
      else
      {
        if(trapType->killsOnActivate)
        {
          object->alive = false;
        }
      }
    }
  }

  object->x = x;
  object->y = y;
  --object->movementLeft;

  return 1;
}

DLLEXPORT int thiefUseSpecial(_Thief* object, int x, int y)
{
  stringstream expr;
  expr << "(game-use-special " << object->id
       << " " << x
       << " " << y
       << ")";
  LOCK( &object->_c->mutex);
  send_string(object->_c->socket, expr.str().c_str());
  UNLOCK( &object->_c->mutex);

  Connection* c = object->_c;

  //proper owner
  if(object->owner != c->playerID)
    return 0;

  //proper type
  if(object->thiefType != 0 && object->thiefType != 1)
    return 0;

  //has specials
  if(object->specialsLeft <= 0)
    return 0;

  //out of bounds
  if(x < 0 || x >= c->mapWidth || y < 0 || y >= c->mapHeight)
    return 0;

  //wrong pyramid
  int width = c->mapWidth/2;
  int minX = object->owner == 1 ? 0 : width;
  if(x < minX || x >= minX + width)
    return 0;

  //hasnt moved
  if(object->movementLeft != object->maxMovement)
    return 0;

  //adjacent target
  if(abs(object->x - x) + abs(object->y - y) != 1)
    return 0;

  //digger
  if(object->thiefType == 1)
  {
    int newx = x - object->x + x;
    int newy = y - object->y + y;
    for (int i = 0; i < c->TileCount; ++i)
    {
      _Tile* t = getTile(c, i);
      if(t->x == newx && t->y == newy)
      {
        if(t->type != 0)
          return 0;
        else if(newx < 0 || newx >= c->mapWidth || newy < 0 || newy >= c->mapHeight)
          return 0;
      }
    }
    object->x = newx;
    object->y = newy;
    
    // Check for oil vase
    _Trap* vase;
    bool isVase = false;
    for(int i = 0; i < c->TrapCount; ++i)
    {
      vase = getTrap(c, i);
      if(vase->active && vase->x == newx&& vase->y == y && vase->trapType == 6)
      {
        isVase = true;
      }
    }
    if (isVase)
    {
      _TrapType* trapType = getTrapType(c, vase->trapType);
    
      --vase->activationsRemaining;
      if(vase->activationsRemaining == 0)
      {
        vase->active = 0;
      }
      else if(trapType->cooldown)
      {
        vase->active = 0;
        vase->turnsTillActive = trapType->cooldown;
      }
    
      int xds[] = {1, -1, 0, 0};
      int yds[] = {0, 0, 1, -1};
      for (int di = 0; di < 4; ++di) {
        int tx = x + xds[di];
        int ty = y + yds[di];
        
        // Kill adjacent thieves
        for(int i = 0; i < c->ThiefCount; ++i)
        {
          _Thief* thief = getThief(c, i);
          if(thief->x == tx && thief->y == ty)
          {
            if(thief->thiefType == 2 && thief->specialsLeft > 0)
            {
              --thief->specialsLeft;
            }
            else
            {
              if(trapType->killsOnActivate)
              {
                thief->alive = false;
              }
            }
          }
        }
      }
    }
    
    // Check for traps at digger destination
    _Trap* trap;
    bool okay = false;
    //trap
    for(int i = 0; i < c->TrapCount; ++i)
    {
      trap = getTrap(c, i);
      if(trap->active && trap->x == newx&& trap->y == y)
      {
        okay = true;
      }
    }
    if(okay)
    {
      _TrapType* trapType = getTrapType(c, trap->trapType);

      if(trap->active && trapType->activatesOnWalkedThrough && trapType->turnsToActivateOnTile == 1)
      {
        --trap->activationsRemaining;
        if(trap->activationsRemaining == 0)
        {
          trap->active = 0;
        }
        else if(trapType->cooldown)
        {
          trap->active = 0;
          trap->turnsTillActive = trapType->cooldown;
        }
        if(object->thiefType == 2 && object->specialsLeft > 0)
        {
          --object->specialsLeft;
        }
        else
        {
          if(trapType->killsOnActivate)
          {
            object->alive = false;
          }
        }
      }
    }
  }
  else //bomber
  {
    for(int i = 0; i < c->TrapCount; ++i)
    {
      _Trap* trap = getTrap(c, i);
      if(trap->x == x && trap->y == y)
      {
        _TrapType* trapType = getTrapType(c, trap->trapType);
        //FIRE VASE OF DOOOOOOOOOM
        if(trap->trapType == 6)
        {
          --trap->activationsRemaining;
          if(trap->activationsRemaining == 0)
          {
            trap->active = 0;
          }
          else if(trapType->cooldown)
          {
            trap->active = 0;
            trap->turnsTillActive = trapType->cooldown;
          }
        
          int xds[] = {1, -1, 0, 0};
          int yds[] = {0, 0, 1, -1};
          for (int di = 0; di < 4; ++di) {
            int tx = x + xds[di];
            int ty = y + yds[di];
            
            // Kill adjacent thieves
            for(int i = 0; i < c->ThiefCount; ++i)
            {
              _Thief* thief = getThief(c, i);
              if(thief->x == tx && thief->y == ty)
              {
                if(thief->thiefType == 2 && thief->specialsLeft > 0)
                {
                  --thief->specialsLeft;
                }
                else
                {
                  if(trapType->killsOnActivate)
                  {
                    thief->alive = false;
                  }
                }
              }
            }
          }
          
          // Kill calling thief
          if(object->thiefType == 2 && object->specialsLeft > 0)
          {
            --object->specialsLeft;
          }
          else
          {
            if(trapType->killsOnActivate)
            {
              object->alive = false;
            }
          }
        }
        else
        {
          trap->active = 0;
        }
      }
    }
    //thievzzzzzzz
    for(int i = 0; i < c->ThiefCount; ++i)
    {
      _Thief* thief = getThief(c, i);
      if(thief->x == x && thief->y == y)
      {
        thief->alive = 0;
      }
    }
    //wall get dead
    for(int i = 0; i < c->TileCount; ++i)
    {
      _Tile* tile = getTile(c, i);
      if(tile->x == x && tile->y == y)
      {
        tile->type = 0;
      }
    }
  }
  object->movementLeft = 0;
  --object->specialsLeft;
  
  return 1;
}




//Utility functions for parsing data
void parsePlayer(Connection* c, _Player* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->playerName = new char[strlen(sub->val)+1];
  strncpy(object->playerName, sub->val, strlen(sub->val));
  object->playerName[strlen(sub->val)] = 0;
  sub = sub->next;
  object->time = atof(sub->val);
  sub = sub->next;
  object->scarabs = atoi(sub->val);
  sub = sub->next;
  object->roundsWon = atoi(sub->val);
  sub = sub->next;
  object->sarcophagiCaptured = atoi(sub->val);
  sub = sub->next;

}
void parseMappable(Connection* c, _Mappable* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;

}
void parseTile(Connection* c, _Tile* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->type = atoi(sub->val);
  sub = sub->next;

}
void parseTrap(Connection* c, _Trap* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->owner = atoi(sub->val);
  sub = sub->next;
  object->trapType = atoi(sub->val);
  sub = sub->next;
  object->visible = atoi(sub->val);
  sub = sub->next;
  object->active = atoi(sub->val);
  sub = sub->next;
  object->bodyCount = atoi(sub->val);
  sub = sub->next;
  object->activationsRemaining = atoi(sub->val);
  sub = sub->next;
  object->turnsTillActive = atoi(sub->val);
  sub = sub->next;

}
void parseThief(Connection* c, _Thief* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->x = atoi(sub->val);
  sub = sub->next;
  object->y = atoi(sub->val);
  sub = sub->next;
  object->owner = atoi(sub->val);
  sub = sub->next;
  object->thiefType = atoi(sub->val);
  sub = sub->next;
  object->alive = atoi(sub->val);
  sub = sub->next;
  object->specialsLeft = atoi(sub->val);
  sub = sub->next;
  object->maxSpecials = atoi(sub->val);
  sub = sub->next;
  object->movementLeft = atoi(sub->val);
  sub = sub->next;
  object->maxMovement = atoi(sub->val);
  sub = sub->next;
  object->frozenTurnsLeft = atoi(sub->val);
  sub = sub->next;

}
void parseThiefType(Connection* c, _ThiefType* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->name = new char[strlen(sub->val)+1];
  strncpy(object->name, sub->val, strlen(sub->val));
  object->name[strlen(sub->val)] = 0;
  sub = sub->next;
  object->type = atoi(sub->val);
  sub = sub->next;
  object->cost = atoi(sub->val);
  sub = sub->next;
  object->maxMovement = atoi(sub->val);
  sub = sub->next;
  object->maxSpecials = atoi(sub->val);
  sub = sub->next;
  object->maxInstances = atoi(sub->val);
  sub = sub->next;

}
void parseTrapType(Connection* c, _TrapType* object, sexp_t* expression)
{
  sexp_t* sub;
  sub = expression->list;

  object->_c = c;

  object->id = atoi(sub->val);
  sub = sub->next;
  object->name = new char[strlen(sub->val)+1];
  strncpy(object->name, sub->val, strlen(sub->val));
  object->name[strlen(sub->val)] = 0;
  sub = sub->next;
  object->type = atoi(sub->val);
  sub = sub->next;
  object->cost = atoi(sub->val);
  sub = sub->next;
  object->maxInstances = atoi(sub->val);
  sub = sub->next;
  object->startsVisible = atoi(sub->val);
  sub = sub->next;
  object->hasAction = atoi(sub->val);
  sub = sub->next;
  object->deactivatable = atoi(sub->val);
  sub = sub->next;
  object->maxActivations = atoi(sub->val);
  sub = sub->next;
  object->activatesOnWalkedThrough = atoi(sub->val);
  sub = sub->next;
  object->turnsToActivateOnTile = atoi(sub->val);
  sub = sub->next;
  object->canPlaceOnWalls = atoi(sub->val);
  sub = sub->next;
  object->canPlaceOnOpenTiles = atoi(sub->val);
  sub = sub->next;
  object->freezesForTurns = atoi(sub->val);
  sub = sub->next;
  object->killsOnActivate = atoi(sub->val);
  sub = sub->next;
  object->cooldown = atoi(sub->val);
  sub = sub->next;
  object->explosive = atoi(sub->val);
  sub = sub->next;
  object->unpassable = atoi(sub->val);
  sub = sub->next;

}

DLLEXPORT int networkLoop(Connection* c)
{
  while(true)
  {
    sexp_t* base, *expression, *sub, *subsub;

    char* message = rec_string(c->socket);
    string text = message;
    base = extract_sexpr(message);
    delete[] message;
    expression = base->list;
    if(expression->val != NULL && strcmp(expression->val, "game-winner") == 0)
    {
      expression = expression->next->next->next;
      int winnerID = atoi(expression->val);
      if(winnerID == c->playerID)
      {
        cout << "You win!" << endl << expression->next->val << endl;
      }
      else
      {
        cout << "You lose. :(" << endl << expression->next->val << endl;
      }
      stringstream expr;
      expr << "(request-log " << c->gameNumber << ")";
      send_string(c->socket, expr.str().c_str());
      destroy_sexp(base);
      return 0;
    }
    else if(expression->val != NULL && strcmp(expression->val, "log") == 0)
    {
      ofstream out;
      stringstream filename;
      expression = expression->next;
      filename << expression->val;
      filename << ".gamelog";
      expression = expression->next;
      out.open(filename.str().c_str());
      if (out.good())
        out.write(expression->val, strlen(expression->val));
      else
        cerr << "Error : Could not create log." << endl;
      out.close();
      destroy_sexp(base);
      return 0;
    }
    else if(expression->val != NULL && strcmp(expression->val, "game-accepted")==0)
    {
      char gameID[30];

      expression = expression->next;
      strcpy(gameID, expression->val);
      cout << "Created game " << gameID << endl;
    }
    else if(expression->val != NULL && strstr(expression->val, "denied"))
    {
      cout << expression->val << endl;
      cout << expression->next->val << endl;
    }
    else if(expression->val != NULL && strcmp(expression->val, "status") == 0)
    {
      while(expression->next != NULL)
      {
        expression = expression->next;
        sub = expression->list;
        if(string(sub->val) == "game")
        {
          sub = sub->next;
          c->mapWidth = atoi(sub->val);
          sub = sub->next;

          c->mapHeight = atoi(sub->val);
          sub = sub->next;

          c->turnNumber = atoi(sub->val);
          sub = sub->next;

          c->roundTurnNumber = atoi(sub->val);
          sub = sub->next;

          c->maxThieves = atoi(sub->val);
          sub = sub->next;

          c->maxTraps = atoi(sub->val);
          sub = sub->next;

          c->playerID = atoi(sub->val);
          sub = sub->next;

          c->gameNumber = atoi(sub->val);
          sub = sub->next;

          c->roundNumber = atoi(sub->val);
          sub = sub->next;

          c->scarabsForTraps = atoi(sub->val);
          sub = sub->next;

          c->scarabsForThieves = atoi(sub->val);
          sub = sub->next;

          c->roundsToWin = atoi(sub->val);
          sub = sub->next;

          c->roundTurnLimit = atoi(sub->val);
          sub = sub->next;

          c->numberOfSarcophagi = atoi(sub->val);
          sub = sub->next;

        }
        else if(string(sub->val) == "Player")
        {
          if(c->Players)
          {
            for(int i = 0; i < c->PlayerCount; i++)
            {
              delete[] c->Players[i].playerName;
            }
            delete[] c->Players;
          }
          c->PlayerCount =  sexp_list_length(expression)-1; //-1 for the header
          c->Players = new _Player[c->PlayerCount];
          for(int i = 0; i < c->PlayerCount; i++)
          {
            sub = sub->next;
            parsePlayer(c, c->Players+i, sub);
          }
        }
        else if(string(sub->val) == "Mappable")
        {
          if(c->Mappables)
          {
            for(int i = 0; i < c->MappableCount; i++)
            {
            }
            delete[] c->Mappables;
          }
          c->MappableCount =  sexp_list_length(expression)-1; //-1 for the header
          c->Mappables = new _Mappable[c->MappableCount];
          for(int i = 0; i < c->MappableCount; i++)
          {
            sub = sub->next;
            parseMappable(c, c->Mappables+i, sub);
          }
        }
        else if(string(sub->val) == "Tile")
        {
          if(c->Tiles)
          {
            sub = sub->next;
            for(int i = 0; i < c->TileCount; i++)
            {
              if(!sub)
              {
                break;
              }
              int id = atoi(sub->list->val);
              if(id == c->Tiles[i].id)
              {
                parseTile(c, c->Tiles+i, sub);
                sub = sub->next;
              }
            }
          }
          else
          {
            c->TileCount =  sexp_list_length(expression)-1; //-1 for the header
            c->Tiles = new _Tile[c->TileCount];
            for(int i = 0; i < c->TileCount; i++)
            {
              sub = sub->next;
              parseTile(c, c->Tiles+i, sub);
            }
          }
        }
        else if(string(sub->val) == "Trap")
        {
          if(c->Traps)
          {
            for(int i = 0; i < c->TrapCount; i++)
            {
            }
            delete[] c->Traps;
          }
          c->TrapCount =  sexp_list_length(expression)-1; //-1 for the header
          c->Traps = new _Trap[c->TrapCount];
          for(int i = 0; i < c->TrapCount; i++)
          {
            sub = sub->next;
            parseTrap(c, c->Traps+i, sub);
          }
        }
        else if(string(sub->val) == "Thief")
        {
          if(c->Thiefs)
          {
            for(int i = 0; i < c->ThiefCount; i++)
            {
            }
            delete[] c->Thiefs;
          }
          c->ThiefCount =  sexp_list_length(expression)-1; //-1 for the header
          c->Thiefs = new _Thief[c->ThiefCount];
          for(int i = 0; i < c->ThiefCount; i++)
          {
            sub = sub->next;
            parseThief(c, c->Thiefs+i, sub);
          }
        }
        else if(string(sub->val) == "ThiefType")
        {
          if(c->ThiefTypes)
          {
            sub = sub->next;
            for(int i = 0; i < c->ThiefTypeCount; i++)
            {
              if(!sub)
              {
                break;
              }
              int id = atoi(sub->list->val);
              if(id == c->ThiefTypes[i].id)
              {
                delete[] c->ThiefTypes[i].name;
                parseThiefType(c, c->ThiefTypes+i, sub);
                sub = sub->next;
              }
            }
          }
          else
          {
            c->ThiefTypeCount =  sexp_list_length(expression)-1; //-1 for the header
            c->ThiefTypes = new _ThiefType[c->ThiefTypeCount];
            for(int i = 0; i < c->ThiefTypeCount; i++)
            {
              sub = sub->next;
              parseThiefType(c, c->ThiefTypes+i, sub);
            }
          }
        }
        else if(string(sub->val) == "TrapType")
        {
          if(c->TrapTypes)
          {
            sub = sub->next;
            for(int i = 0; i < c->TrapTypeCount; i++)
            {
              if(!sub)
              {
                break;
              }
              int id = atoi(sub->list->val);
              if(id == c->TrapTypes[i].id)
              {
                delete[] c->TrapTypes[i].name;
                parseTrapType(c, c->TrapTypes+i, sub);
                sub = sub->next;
              }
            }
          }
          else
          {
            c->TrapTypeCount =  sexp_list_length(expression)-1; //-1 for the header
            c->TrapTypes = new _TrapType[c->TrapTypeCount];
            for(int i = 0; i < c->TrapTypeCount; i++)
            {
              sub = sub->next;
              parseTrapType(c, c->TrapTypes+i, sub);
            }
          }
        }
      }
      destroy_sexp(base);
      return 1;
    }
    else
    {
#ifdef SHOW_WARNINGS
      cerr << "Unrecognized message: " << text << endl;
#endif
    }
    destroy_sexp(base);
  }
}

DLLEXPORT _Player* getPlayer(Connection* c, int num)
{
  return c->Players + num;
}
DLLEXPORT int getPlayerCount(Connection* c)
{
  return c->PlayerCount;
}

DLLEXPORT _Mappable* getMappable(Connection* c, int num)
{
  return c->Mappables + num;
}
DLLEXPORT int getMappableCount(Connection* c)
{
  return c->MappableCount;
}

DLLEXPORT _Tile* getTile(Connection* c, int num)
{
  return c->Tiles + num;
}
DLLEXPORT int getTileCount(Connection* c)
{
  return c->TileCount;
}

DLLEXPORT _Trap* getTrap(Connection* c, int num)
{
  return c->Traps + num;
}
DLLEXPORT int getTrapCount(Connection* c)
{
  return c->TrapCount;
}

DLLEXPORT _Thief* getThief(Connection* c, int num)
{
  return c->Thiefs + num;
}
DLLEXPORT int getThiefCount(Connection* c)
{
  return c->ThiefCount;
}

DLLEXPORT _ThiefType* getThiefType(Connection* c, int num)
{
  return c->ThiefTypes + num;
}
DLLEXPORT int getThiefTypeCount(Connection* c)
{
  return c->ThiefTypeCount;
}

DLLEXPORT _TrapType* getTrapType(Connection* c, int num)
{
  return c->TrapTypes + num;
}
DLLEXPORT int getTrapTypeCount(Connection* c)
{
  return c->TrapTypeCount;
}


DLLEXPORT int getMapWidth(Connection* c)
{
  return c->mapWidth;
}
DLLEXPORT int getMapHeight(Connection* c)
{
  return c->mapHeight;
}
DLLEXPORT int getTurnNumber(Connection* c)
{
  return c->turnNumber;
}
DLLEXPORT int getRoundTurnNumber(Connection* c)
{
  return c->roundTurnNumber;
}
DLLEXPORT int getMaxThieves(Connection* c)
{
  return c->maxThieves;
}
DLLEXPORT int getMaxTraps(Connection* c)
{
  return c->maxTraps;
}
DLLEXPORT int getPlayerID(Connection* c)
{
  return c->playerID;
}
DLLEXPORT int getGameNumber(Connection* c)
{
  return c->gameNumber;
}
DLLEXPORT int getRoundNumber(Connection* c)
{
  return c->roundNumber;
}
DLLEXPORT int getScarabsForTraps(Connection* c)
{
  return c->scarabsForTraps;
}
DLLEXPORT int getScarabsForThieves(Connection* c)
{
  return c->scarabsForThieves;
}
DLLEXPORT int getRoundsToWin(Connection* c)
{
  return c->roundsToWin;
}
DLLEXPORT int getRoundTurnLimit(Connection* c)
{
  return c->roundTurnLimit;
}
DLLEXPORT int getNumberOfSarcophagi(Connection* c)
{
  return c->numberOfSarcophagi;
}
