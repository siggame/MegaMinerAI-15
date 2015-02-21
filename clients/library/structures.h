//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that
#ifndef STRUCTURES_H
#define STRUCTURES_H

struct Connection;
struct _Player;
struct _Mappable;
struct _Tile;
struct _Trap;
struct _Thief;
struct _ThiefType;
struct _TrapType;


struct _Player
{
  Connection* _c;
  int id;
  char* playerName;
  float time;
  int scarabs;
};
struct _Mappable
{
  Connection* _c;
  int id;
  int x;
  int y;
};
struct _Tile
{
  Connection* _c;
  int id;
  int isWall;
};
struct _Trap
{
  Connection* _c;
  int id;
  int x;
  int y;
  int owner;
  int trapType;
  int visible;
  int active;
  int bodyCount;
};
struct _Thief
{
  Connection* _c;
  int id;
  int x;
  int y;
  int owner;
  int thiefType;
  int alive;
  int actionsLeft;
  int maxActions;
  int movementLeft;
  int maxMovement;
};
struct _ThiefType
{
  Connection* _c;
  int id;
  char* name;
  int type;
  int cost;
  int maxActions;
  int maxMovement;
  int maxInstances;
};
struct _TrapType
{
  Connection* _c;
  int id;
  char* name;
  int type;
  int cost;
  int startsVisible;
  int hasAction;
};

#endif
