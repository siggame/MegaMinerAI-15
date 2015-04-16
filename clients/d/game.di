import structures;

extern (C):

//server stuff
Connection* createConnection();
void destroyConnection(Connection*);
int serverConnect(Connection*, const char*, const char*);
int serverLogin(Connection*, const char*, const char*);
int createGame(Connection*);
int joinGame(Connection*, int, const char*);
void endTurn(Connection*);
void getStatus(Connection*);

//commands
int playerPlaceTrap(_Player*, int, int, int);
int playerPurchaseThief(_Player*, int, int, int);
int playerPharaohTalk(_Player*, char*);
int trapAct(_Trap*, int, int);
int trapToggle(_Trap*);
int thiefThiefTalk(_Thief*, char*);
int thiefMove(_Thief*, int, int);
int thiefUseSpecial(_Thief*, int, int);

//accessors
int getMapWidth(Connection*);
int getMapHeight(Connection*);
int getTurnNumber(Connection*);
int getRoundTurnNumber(Connection*);
int getMaxThieves(Connection*);
int getMaxTraps(Connection*);
int getPlayerID(Connection*);
int getGameNumber(Connection*);
int getRoundNumber(Connection*);
int getScarabsForTraps(Connection*);
int getScarabsForThieves(Connection*);
int getRoundsToWin(Connection*);
int getRoundTurnLimit(Connection*);
int getNumberOfSarcophagi(Connection*);

_Player* getPlayer(Connection*, int);
int getPlayerCount(Connection*);

_Mappable* getMappable(Connection*, int);
int getMappableCount(Connection*);

_Tile* getTile(Connection*, int);
int getTileCount(Connection*);

_Trap* getTrap(Connection*, int);
int getTrapCount(Connection*);

_Thief* getThief(Connection*, int);
int getThiefCount(Connection*);

_ThiefType* getThiefType(Connection*, int);
int getThiefTypeCount(Connection*);

_TrapType* getTrapType(Connection*, int);
int getTrapTypeCount(Connection*);

int networkLoop(Connection*);
