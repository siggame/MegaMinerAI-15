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
const int MOVE = 1;
const int KILL = 2;
const int PHARAOHTALK = 3;
const int THIEFTALK = 4;
const int ACTIVATE = 5;
const int BOMB = 6;

struct Player
{
  int id;
  char* playerName;
  float time;
  int scarabs;

  friend std::ostream& operator<<(std::ostream& stream, Player obj);
};

struct Mappable
{
  int id;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, Mappable obj);
};

struct Tile
{
  int id;
  int isWall;

  friend std::ostream& operator<<(std::ostream& stream, Tile obj);
};

struct Trap: public Mappable 
{
  int owner;
  int trapType;
  int visible;
  int active;
  int bodyCount;

  friend std::ostream& operator<<(std::ostream& stream, Trap obj);
};

struct Thief: public Mappable 
{
  int owner;
  int thiefType;
  int alive;
  int actionsLeft;
  int maxActions;
  int movementLeft;
  int maxMovement;

  friend std::ostream& operator<<(std::ostream& stream, Thief obj);
};

struct ThiefType
{
  int id;
  char* name;
  int type;
  int cost;
  int maxActions;
  int maxMovement;
  int maxInstances;

  friend std::ostream& operator<<(std::ostream& stream, ThiefType obj);
};

struct TrapType
{
  int id;
  char* name;
  int type;
  int cost;
  int startsVisible;
  int hasAction;

  friend std::ostream& operator<<(std::ostream& stream, TrapType obj);
};


struct Animation
{
  int type;
};

struct spawn : public Animation
{
  int actingID;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, spawn obj);
};

struct move : public Animation
{
  int actingID;
  int fromX;
  int fromY;
  int toX;
  int toY;

  friend std::ostream& operator<<(std::ostream& stream, move obj);
};

struct kill : public Animation
{
  int actingID;
  int targetID;

  friend std::ostream& operator<<(std::ostream& stream, kill obj);
};

struct pharaohTalk : public Animation
{
  int actingID;
  char* message;

  friend std::ostream& operator<<(std::ostream& stream, pharaohTalk obj);
};

struct thiefTalk : public Animation
{
  int actingID;
  char* message;

  friend std::ostream& operator<<(std::ostream& stream, thiefTalk obj);
};

struct activate : public Animation
{
  int actingID;

  friend std::ostream& operator<<(std::ostream& stream, activate obj);
};

struct bomb : public Animation
{
  int actingID;
  int x;
  int y;

  friend std::ostream& operator<<(std::ostream& stream, bomb obj);
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
  int maxThieves;
  int maxTraps;
  int playerID;
  int gameNumber;
  int roundNumber;
  int scarabsForTraps;
  int scarabsForThieves;
  int maxStack;

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
