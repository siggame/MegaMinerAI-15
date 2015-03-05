import com.sun.jna.Library;
import com.sun.jna.Pointer;
import com.sun.jna.Native;

public interface Client extends Library {
  Client INSTANCE = (Client)Native.loadLibrary("client", Client.class);
  Pointer createConnection();
  boolean serverConnect(Pointer connection, String host, String port);

  boolean serverLogin(Pointer connection, String username, String password);
  int createGame(Pointer connection);
  int joinGame(Pointer connection, int id, String playerType);

  void endTurn(Pointer connection);
  void getStatus(Pointer connection);

  int networkLoop(Pointer connection);


    //commands
  int playerPlaceTrap(Pointer object, int x, int y, int trapType);
  int playerPurchaseThief(Pointer object, int x, int y, int thiefType);
  int playerPharaohTalk(Pointer object, String message);
  int trapAct(Pointer object, int x, int y);
  int trapToggle(Pointer object);
  int thiefThiefTalk(Pointer object, String message);
  int thiefMove(Pointer object, int x, int y);
  int thiefAct(Pointer object, int x, int y);

    //accessors
  int getMapWidth(Pointer connection);
  int getMapHeight(Pointer connection);
  int getTurnNumber(Pointer connection);
  int getRoundTurnNumber(Pointer connection);
  int getMaxThieves(Pointer connection);
  int getMaxTraps(Pointer connection);
  int getPlayerID(Pointer connection);
  int getGameNumber(Pointer connection);
  int getRoundNumber(Pointer connection);
  int getScarabsForTraps(Pointer connection);
  int getScarabsForThieves(Pointer connection);
  int getMaxStack(Pointer connection);

  Pointer getPlayer(Pointer connection, int num);
  int getPlayerCount(Pointer connection);
  Pointer getMappable(Pointer connection, int num);
  int getMappableCount(Pointer connection);
  Pointer getTile(Pointer connection, int num);
  int getTileCount(Pointer connection);
  Pointer getTrap(Pointer connection, int num);
  int getTrapCount(Pointer connection);
  Pointer getThief(Pointer connection, int num);
  int getThiefCount(Pointer connection);
  Pointer getThiefType(Pointer connection, int num);
  int getThiefTypeCount(Pointer connection);
  Pointer getTrapType(Pointer connection, int num);
  int getTrapTypeCount(Pointer connection);


    //getters
  int playerGetId(Pointer ptr);
  String playerGetPlayerName(Pointer ptr);
  float playerGetTime(Pointer ptr);
  int playerGetScarabs(Pointer ptr);
  int playerGetRoundsWon(Pointer ptr);

  int mappableGetId(Pointer ptr);
  int mappableGetX(Pointer ptr);
  int mappableGetY(Pointer ptr);

  int tileGetId(Pointer ptr);
  int tileGetX(Pointer ptr);
  int tileGetY(Pointer ptr);
  int tileGetType(Pointer ptr);

  int trapGetId(Pointer ptr);
  int trapGetX(Pointer ptr);
  int trapGetY(Pointer ptr);
  int trapGetOwner(Pointer ptr);
  int trapGetTrapType(Pointer ptr);
  int trapGetVisible(Pointer ptr);
  int trapGetActive(Pointer ptr);
  int trapGetBodyCount(Pointer ptr);

  int thiefGetId(Pointer ptr);
  int thiefGetX(Pointer ptr);
  int thiefGetY(Pointer ptr);
  int thiefGetOwner(Pointer ptr);
  int thiefGetThiefType(Pointer ptr);
  int thiefGetAlive(Pointer ptr);
  int thiefGetNinjaReflexesLeft(Pointer ptr);
  int thiefGetMaxNinjaReflexes(Pointer ptr);
  int thiefGetMovementLeft(Pointer ptr);
  int thiefGetMaxMovement(Pointer ptr);
  int thiefGetFrozenTurnsLeft(Pointer ptr);

  int thiefTypeGetId(Pointer ptr);
  String thiefTypeGetName(Pointer ptr);
  int thiefTypeGetType(Pointer ptr);
  int thiefTypeGetCost(Pointer ptr);
  int thiefTypeGetMaxMovement(Pointer ptr);
  int thiefTypeGetMaxNinjaReflexes(Pointer ptr);
  int thiefTypeGetMaxInstances(Pointer ptr);

  int trapTypeGetId(Pointer ptr);
  String trapTypeGetName(Pointer ptr);
  int trapTypeGetType(Pointer ptr);
  int trapTypeGetCost(Pointer ptr);
  int trapTypeGetStartsVisible(Pointer ptr);
  int trapTypeGetHasAction(Pointer ptr);
  int trapTypeGetActivatable(Pointer ptr);
  int trapTypeGetMaxBodyCount(Pointer ptr);
  int trapTypeGetMaxInstances(Pointer ptr);
  int trapTypeGetKillsOnWalkThrough(Pointer ptr);
  int trapTypeGetTurnsToKillOnTile(Pointer ptr);
  int trapTypeGetCanPlaceInWalls(Pointer ptr);
  int trapTypeGetCanPlaceInEmptyTiles(Pointer ptr);
  int trapTypeGetFreezesForTurns(Pointer ptr);


    //properties

}