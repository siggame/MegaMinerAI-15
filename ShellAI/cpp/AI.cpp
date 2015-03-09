#include "AI.h"

AI::AI(Connection* conn) : BaseAI(conn) {}

const char* AI::username() {
  return "Shell AI";
  }

const char* AI::password() {
  return "password";
}

// Function called once, before your first turn.
void AI::init() {}

// Function called every turn.
bool AI::run() {}

// Function called once, after your last turn.
void AI::end() {}
