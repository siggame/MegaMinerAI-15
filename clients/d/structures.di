extern (C++):

struct Connection
{
  int socket;
  
  //#ifdef ENABLE_THREADS
  //pthread_mutex_t mutex;
  //#endif
  
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

struct _Player
{
  Connection* _c;
  int id;
  char* playerName;
  float time;
  int scarabs;
  int roundsWon;
  int sarcophagiCaptured;
};

struct _Tile
{
  Connection* _c;
  int id;
  int x;
  int y;
  int type;
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
  int activationsRemaining;
  int turnsTillActive;
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
  int specialsLeft;
  int maxSpecials;
  int movementLeft;
  int maxMovement;
  int frozenTurnsLeft;
};

struct _ThiefType
{
  Connection* _c;
  int id;
  char* name;
  int type;
  int cost;
  int maxMovement;
  int maxSpecials;
  int maxInstances;
};

struct _TrapType
{
  Connection* _c;
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
};

struct _Mappable {
  Connection* _c;
  int id;
  int x;
  int y;
}
