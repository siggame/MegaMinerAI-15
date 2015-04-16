//Copyright (C) 2009 - Missouri S&T ACM AI Team
//Please do not modify this file while building your AI
//See AI.h & AI.cpp for that

#include "BaseAI.h"
#include "game.h"

int BaseAI::mapWidth()
{
  return getMapWidth(c);
}
int BaseAI::mapHeight()
{
  return getMapHeight(c);
}
int BaseAI::turnNumber()
{
  return getTurnNumber(c);
}
int BaseAI::roundTurnNumber()
{
  return getRoundTurnNumber(c);
}
int BaseAI::maxThieves()
{
  return getMaxThieves(c);
}
int BaseAI::maxTraps()
{
  return getMaxTraps(c);
}
int BaseAI::playerID()
{
  return getPlayerID(c);
}
int BaseAI::gameNumber()
{
  return getGameNumber(c);
}
int BaseAI::roundNumber()
{
  return getRoundNumber(c);
}
int BaseAI::scarabsForTraps()
{
  return getScarabsForTraps(c);
}
int BaseAI::scarabsForThieves()
{
  return getScarabsForThieves(c);
}
int BaseAI::roundsToWin()
{
  return getRoundsToWin(c);
}
int BaseAI::roundTurnLimit()
{
  return getRoundTurnLimit(c);
}
int BaseAI::numberOfSarcophagi()
{
  return getNumberOfSarcophagi(c);
}

bool BaseAI::startTurn()
{
  static bool initialized = false;
  int count = 0;
  count = getPlayerCount(c);
  players.clear();
  players.resize(count);
  for(int i = 0; i < count; i++)
  {
    players[i] = Player(getPlayer(c, i));
  }

  count = getMappableCount(c);
  mappables.clear();
  mappables.resize(count);
  for(int i = 0; i < count; i++)
  {
    mappables[i] = Mappable(getMappable(c, i));
  }

  count = getTileCount(c);
  tiles.clear();
  tiles.resize(count);
  for(int i = 0; i < count; i++)
  {
    tiles[i] = Tile(getTile(c, i));
  }

  count = getTrapCount(c);
  traps.clear();
  traps.resize(count);
  for(int i = 0; i < count; i++)
  {
    traps[i] = Trap(getTrap(c, i));
  }

  count = getThiefCount(c);
  thiefs.clear();
  thiefs.resize(count);
  for(int i = 0; i < count; i++)
  {
    thiefs[i] = Thief(getThief(c, i));
  }

  count = getThiefTypeCount(c);
  thiefTypes.clear();
  thiefTypes.resize(count);
  for(int i = 0; i < count; i++)
  {
    thiefTypes[i] = ThiefType(getThiefType(c, i));
  }

  count = getTrapTypeCount(c);
  trapTypes.clear();
  trapTypes.resize(count);
  for(int i = 0; i < count; i++)
  {
    trapTypes[i] = TrapType(getTrapType(c, i));
  }

  if(!initialized)
  {
    initialized = true;
    init();
  }
  return run();
}

BaseAI::BaseAI(Connection* conn) : c(conn) {}
BaseAI::~BaseAI() {}
