// -*-c++-*-

#ifndef THIEF_H
#define THIEF_H

#include <iostream>
#include "vc_structures.h"

#include "Mappable.h"

namespace client
{


///Represents a single thief on the map.
class Thief : public Mappable {
  public:
  Thief(_Thief* ptr = NULL);

  // Accessors
  ///Unique Identifier
  int id();
  ///X position of the object
  int x();
  ///Y position of the object
  int y();
  ///The owner of this thief.
  int owner();
  ///The type of this thief. This type refers to list of thiefTypes.
  int thiefType();
  ///Whether the thief is alive or not.
  int alive();
  ///The remaining number of times the thief can act.
  int actionsLeft();
  ///The maximum number of times the thief can act.
  int maxActions();
  ///The remaining number of times this thief can move.
  int movementLeft();
  ///The maximum number of times this thief can move.
  int maxMovement();

  // Actions
  ///Allows a thief to display messages on the screen
  int thiefTalk(char* message);
  ///Commands a thief to move to a new location.
  int move(int x, int y);
  ///Commands a thief to act on a location.
  int act(int x, int y);

  // Properties


  friend std::ostream& operator<<(std::ostream& stream, Thief ob);
};

}

#endif

