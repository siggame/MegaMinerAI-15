#ifndef AI_H
#define AI_H

#include "BaseAI.h"

///The class implementing gameplay logic.
class AI: public BaseAI
{
public:
  AI(Connection* c);
  virtual const char* username();
  virtual const char* password();
  virtual void init();
  virtual bool run();
  virtual void end();
};

// Function for bounds checking
bool withinBounds(int x, int y) {
  if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight()) {
    return false;
  }
  return true;
}
#endif
