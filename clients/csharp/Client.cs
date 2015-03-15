using System;
using System.Runtime.InteropServices;

public class Client {
  [DllImport("client")]
  public static extern IntPtr createConnection();
  [DllImport("client")]
  public static extern int serverConnect(IntPtr connection, string host, string port);

  [DllImport("client")]
  public static extern int serverLogin(IntPtr connection, string username, string password);
  [DllImport("client")]
  public static extern int createGame(IntPtr connection);
  [DllImport("client")]
  public static extern int joinGame(IntPtr connection, int id, string playerType);

  [DllImport("client")]
  public static extern void endTurn(IntPtr connection);
  [DllImport("client")]
  public static extern void getStatus(IntPtr connection);

  [DllImport("client")]
  public static extern int networkLoop(IntPtr connection);

#region Commands
  [DllImport("client")]
  public static extern int playerPlaceTrap(IntPtr self, int x, int y, int trapType);
  [DllImport("client")]
  public static extern int playerPurchaseThief(IntPtr self, int x, int y, int thiefType);
  [DllImport("client")]
  public static extern int playerPharaohTalk(IntPtr self, string message);
  [DllImport("client")]
  public static extern int trapAct(IntPtr self, int x, int y);
  [DllImport("client")]
  public static extern int trapToggle(IntPtr self);
  [DllImport("client")]
  public static extern int thiefThiefTalk(IntPtr self, string message);
  [DllImport("client")]
  public static extern int thiefMove(IntPtr self, int x, int y);
  [DllImport("client")]
  public static extern int thiefAct(IntPtr self, int x, int y);
#endregion

#region Accessors
  [DllImport("client")]
  public static extern int getMapWidth(IntPtr connection);
  [DllImport("client")]
  public static extern int getMapHeight(IntPtr connection);
  [DllImport("client")]
  public static extern int getTurnNumber(IntPtr connection);
  [DllImport("client")]
  public static extern int getRoundTurnNumber(IntPtr connection);
  [DllImport("client")]
  public static extern int getMaxThieves(IntPtr connection);
  [DllImport("client")]
  public static extern int getMaxTraps(IntPtr connection);
  [DllImport("client")]
  public static extern int getPlayerID(IntPtr connection);
  [DllImport("client")]
  public static extern int getGameNumber(IntPtr connection);
  [DllImport("client")]
  public static extern int getRoundNumber(IntPtr connection);
  [DllImport("client")]
  public static extern int getScarabsForTraps(IntPtr connection);
  [DllImport("client")]
  public static extern int getScarabsForThieves(IntPtr connection);
  [DllImport("client")]
  public static extern int getMaxStack(IntPtr connection);
  [DllImport("client")]
  public static extern int getRoundsToWin(IntPtr connection);
  [DllImport("client")]
  public static extern int getRoundTurnLimit(IntPtr connection);

  [DllImport("client")]
  public static extern IntPtr getPlayer(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getPlayerCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getMappable(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getMappableCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getTile(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getTileCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getTrap(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getTrapCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getThief(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getThiefCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getThiefType(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getThiefTypeCount(IntPtr connection);
  [DllImport("client")]
  public static extern IntPtr getTrapType(IntPtr connection, int num);
  [DllImport("client")]
  public static extern int getTrapTypeCount(IntPtr connection);
#endregion

#region Getters
  [DllImport("client")]
  public static extern int playerGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern IntPtr playerGetPlayerName(IntPtr ptr);
  [DllImport("client")]
  public static extern float playerGetTime(IntPtr ptr);
  [DllImport("client")]
  public static extern int playerGetScarabs(IntPtr ptr);
  [DllImport("client")]
  public static extern int playerGetRoundsWon(IntPtr ptr);

  [DllImport("client")]
  public static extern int mappableGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern int mappableGetX(IntPtr ptr);
  [DllImport("client")]
  public static extern int mappableGetY(IntPtr ptr);

  [DllImport("client")]
  public static extern int tileGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern int tileGetX(IntPtr ptr);
  [DllImport("client")]
  public static extern int tileGetY(IntPtr ptr);
  [DllImport("client")]
  public static extern int tileGetType(IntPtr ptr);

  [DllImport("client")]
  public static extern int trapGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetX(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetY(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetOwner(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetTrapType(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetVisible(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetActive(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetBodyCount(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetActivationsRemaining(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapGetTurnsTillActive(IntPtr ptr);

  [DllImport("client")]
  public static extern int thiefGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetX(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetY(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetOwner(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetThiefType(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetAlive(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetNinjaReflexesLeft(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetMaxNinjaReflexes(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetMovementLeft(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetMaxMovement(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefGetFrozenTurnsLeft(IntPtr ptr);

  [DllImport("client")]
  public static extern int thiefTypeGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern IntPtr thiefTypeGetName(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefTypeGetType(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefTypeGetCost(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefTypeGetMaxMovement(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefTypeGetMaxNinjaReflexes(IntPtr ptr);
  [DllImport("client")]
  public static extern int thiefTypeGetMaxInstances(IntPtr ptr);

  [DllImport("client")]
  public static extern int trapTypeGetId(IntPtr ptr);
  [DllImport("client")]
  public static extern IntPtr trapTypeGetName(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetType(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetCost(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetMaxInstances(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetStartsVisible(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetHasAction(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetDeactivatable(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetMaxActivations(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetActivatesOnWalkedThrough(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetTurnsToActivateOnTile(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetCanPlaceOnWalls(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetCanPlaceOnOpenTiles(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetFreezesForTurns(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetKillsOnActivate(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetCooldown(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetExplosive(IntPtr ptr);
  [DllImport("client")]
  public static extern int trapTypeGetUnpassable(IntPtr ptr);

#endregion

#region Properties
#endregion
}
