//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef STRUCTURES_H
#define STRUCTURES_H

#include <iostream>
#include <vector>
#include <map>
#include <string>

#include "smartpointer.h"

namespace parser
{

const int SPAWN = 0;
const int ACTIVATE = 1;
const int BOMB = 2;
const int MOVE = 3;
const int KILL = 4;
const int PHARAOHTALK = 5;
const int THIEFTALK = 6;
const int DIG = 7;
const int ROLL = 8;

struct Player
{
  int id;
  char* playerName;
  float time;
  int scarabs;
  int roundsWon;
  int sarcophagiCaptured;

  friend std::ostream& operator<<(std::ostream& stream, Player obj);
};

struct Mappable
{
  int id;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, Mappable obj);
};

struct Tile: public Mappable 
{
  int type;

  friend std::ostream& operator<<(std::ostream& stream, Tile obj);
};

struct Trap: public Mappable 
{
  int owner;
  int trapType;
  int visible;
  int active;
  int bodyCount;
  int activationsRemaining;
  int turnsTillActive;

  friend std::ostream& operator<<(std::ostream& stream, Trap obj);
};

struct Thief: public Mappable 
{
  int owner;
  int thiefType;
  int alive;
  int specialsLeft;
  int maxSpecials;
  int movementLeft;
  int maxMovement;
  int frozenTurnsLeft;

  friend std::ostream& operator<<(std::ostream& stream, Thief obj);
};

struct ThiefType
{
  int id;
  char* name;
  int type;
  int cost;
  int maxMovement;
  int maxSpecials;
  int maxInstances;

  friend std::ostream& operator<<(std::ostream& stream, ThiefType obj);
};

struct TrapType
{
  int id;
  char* name;
  int type;
  int cost;
  int maxInstances;
  int startsVisible;
  int hasAction;
  int deactivatable;
  int maxActivations;
  int activatesOnWalkedThrough;
  int turnsToActivateOnTile;
  int canPlaceOnWalls;
  int canPlaceOnOpenTiles;
  int freezesForTurns;
  int killsOnActivate;
  int cooldown;
  int explosive;
  int unpassable;

  friend std::ostream& operator<<(std::ostream& stream, TrapType obj);
};


struct Animation
{
  int type;
};

struct spawn : public Animation
{
  int sourceID;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, spawn obj);
};

struct activate : public Animation
{
  int sourceID;

  friend std::ostream& operator<<(std::ostream& stream, activate obj);
};

struct bomb : public Animation
{
  int sourceID;
  int targetID;

  friend std::ostream& operator<<(std::ostream& stream, bomb obj);
};

struct move : public Animation
{
  int sourceID;
  int fromX;
  int fromY;
  int toX;
  int toY;

  friend std::ostream& operator<<(std::ostream& stream, move obj);
};

struct kill : public Animation
{
  int sourceID;
  int targetID;

  friend std::ostream& operator<<(std::ostream& stream, kill obj);
};

struct pharaohTalk : public Animation
{
  int playerID;
  char* message;

  friend std::ostream& operator<<(std::ostream& stream, pharaohTalk obj);
};

struct thiefTalk : public Animation
{
  int sourceID;
  char* message;

  friend std::ostream& operator<<(std::ostream& stream, thiefTalk obj);
};

struct dig : public Animation
{
  int sourceID;
  int targetID;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, dig obj);
};

struct roll : public Animation
{
  int sourceID;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, roll obj);
};


struct AnimOwner: public Animation
{
  int owner;
};

struct GameState
{
  std::map<int,Player> players;
  std::map<int,Mappable> mappables;
  std::map<int,Tile> tiles;
  std::map<int,Trap> traps;
  std::map<int,Thief> thiefs;
  std::map<int,ThiefType> thiefTypes;
  std::map<int,TrapType> trapTypes;

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
  int roundsToWin;
  int roundTurnLimit;
  int numberOfSarcophagi;

  std::map< int, std::vector< SmartPointer< Animation > > > animations;
  friend std::ostream& operator<<(std::ostream& stream, GameState obj);
};

struct Game
{
  std::vector<GameState> states;
  std::string players[2];
  int winner;
	std::string winReason;

  Game();
};

} // parser

#endif
