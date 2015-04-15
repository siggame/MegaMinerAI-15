// -*-c++-*-

#include "Player.h"
#include "game.h"


Player::Player(_Player* pointer)
{
    ptr = (void*) pointer;
}

int Player::id()
{
  return ((_Player*)ptr)->id;
}

char* Player::playerName()
{
  return ((_Player*)ptr)->playerName;
}

float Player::time()
{
  return ((_Player*)ptr)->time;
}

int Player::scarabs()
{
  return ((_Player*)ptr)->scarabs;
}

int Player::roundsWon()
{
  return ((_Player*)ptr)->roundsWon;
}

int Player::sarcophagiCaptured()
{
  return ((_Player*)ptr)->sarcophagiCaptured;
}


bool Player::placeTrap(int x, int y, int trapType)
{
  return playerPlaceTrap( (_Player*)ptr, x, y, trapType);
}

bool Player::purchaseThief(int x, int y, int thiefType)
{
  return playerPurchaseThief( (_Player*)ptr, x, y, thiefType);
}

bool Player::pharaohTalk(char* message)
{
  return playerPharaohTalk( (_Player*)ptr, message);
}



std::ostream& operator<<(std::ostream& stream,Player ob)
{
  stream << "id: " << ((_Player*)ob.ptr)->id  <<'\n';
  stream << "playerName: " << ((_Player*)ob.ptr)->playerName  <<'\n';
  stream << "time: " << ((_Player*)ob.ptr)->time  <<'\n';
  stream << "scarabs: " << ((_Player*)ob.ptr)->scarabs  <<'\n';
  stream << "roundsWon: " << ((_Player*)ob.ptr)->roundsWon  <<'\n';
  stream << "sarcophagiCaptured: " << ((_Player*)ob.ptr)->sarcophagiCaptured  <<'\n';
  return stream;
}
