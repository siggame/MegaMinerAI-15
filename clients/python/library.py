# -*-python-*-

import os

from ctypes import *

try:
  if os.name == 'posix':
    library = CDLL("./libclient.so")
  elif os.name == 'nt':
    library = CDLL("./client.dll")
  else:
    raise Exception("Unrecognized OS: "+os.name)
except OSError:
  raise Exception("It looks like you didn't build libclient. Run 'make' and try again.")

# commands

library.createConnection.restype = c_void_p
library.createConnection.argtypes = []

library.serverConnect.restype = c_int
library.serverConnect.argtypes = [c_void_p, c_char_p, c_char_p]

library.serverLogin.restype = c_int
library.serverLogin.argtypes = [c_void_p, c_char_p, c_char_p]

library.createGame.restype = c_int
library.createGame.argtypes = [c_void_p]

library.joinGame.restype = c_int
library.joinGame.argtypes = [c_void_p, c_int, c_char_p]

library.endTurn.restype = None
library.endTurn.argtypes = [c_void_p]

library.getStatus.restype = None
library.getStatus.argtypes = [c_void_p]

library.networkLoop.restype = c_int
library.networkLoop.argtypes = [c_void_p]

#Functions
library.playerPlaceTrap.restype = c_int
library.playerPlaceTrap.argtypes = [c_void_p, c_int, c_int, c_int]

library.playerPurchaseThief.restype = c_int
library.playerPurchaseThief.argtypes = [c_void_p, c_int, c_int, c_int]

library.playerPharaohTalk.restype = c_int
library.playerPharaohTalk.argtypes = [c_void_p, c_char_p]

library.trapAct.restype = c_int
library.trapAct.argtypes = [c_void_p, c_int, c_int]

library.trapToggle.restype = c_int
library.trapToggle.argtypes = [c_void_p]

library.thiefThiefTalk.restype = c_int
library.thiefThiefTalk.argtypes = [c_void_p, c_char_p]

library.thiefMove.restype = c_int
library.thiefMove.argtypes = [c_void_p, c_int, c_int]

library.thiefUseSpecial.restype = c_int
library.thiefUseSpecial.argtypes = [c_void_p, c_int, c_int]

# accessors

#Globals
library.getMapWidth.restype = c_int
library.getMapWidth.argtypes = [c_void_p]

library.getMapHeight.restype = c_int
library.getMapHeight.argtypes = [c_void_p]

library.getTurnNumber.restype = c_int
library.getTurnNumber.argtypes = [c_void_p]

library.getRoundTurnNumber.restype = c_int
library.getRoundTurnNumber.argtypes = [c_void_p]

library.getMaxThieves.restype = c_int
library.getMaxThieves.argtypes = [c_void_p]

library.getMaxTraps.restype = c_int
library.getMaxTraps.argtypes = [c_void_p]

library.getPlayerID.restype = c_int
library.getPlayerID.argtypes = [c_void_p]

library.getGameNumber.restype = c_int
library.getGameNumber.argtypes = [c_void_p]

library.getRoundNumber.restype = c_int
library.getRoundNumber.argtypes = [c_void_p]

library.getScarabsForTraps.restype = c_int
library.getScarabsForTraps.argtypes = [c_void_p]

library.getScarabsForThieves.restype = c_int
library.getScarabsForThieves.argtypes = [c_void_p]

library.getMaxStack.restype = c_int
library.getMaxStack.argtypes = [c_void_p]

library.getRoundsToWin.restype = c_int
library.getRoundsToWin.argtypes = [c_void_p]

library.getRoundTurnLimit.restype = c_int
library.getRoundTurnLimit.argtypes = [c_void_p]

library.getPlayer.restype = c_void_p
library.getPlayer.argtypes = [c_void_p, c_int]

library.getPlayerCount.restype = c_int
library.getPlayerCount.argtypes = [c_void_p]

library.getMappable.restype = c_void_p
library.getMappable.argtypes = [c_void_p, c_int]

library.getMappableCount.restype = c_int
library.getMappableCount.argtypes = [c_void_p]

library.getTile.restype = c_void_p
library.getTile.argtypes = [c_void_p, c_int]

library.getTileCount.restype = c_int
library.getTileCount.argtypes = [c_void_p]

library.getTrap.restype = c_void_p
library.getTrap.argtypes = [c_void_p, c_int]

library.getTrapCount.restype = c_int
library.getTrapCount.argtypes = [c_void_p]

library.getThief.restype = c_void_p
library.getThief.argtypes = [c_void_p, c_int]

library.getThiefCount.restype = c_int
library.getThiefCount.argtypes = [c_void_p]

library.getThiefType.restype = c_void_p
library.getThiefType.argtypes = [c_void_p, c_int]

library.getThiefTypeCount.restype = c_int
library.getThiefTypeCount.argtypes = [c_void_p]

library.getTrapType.restype = c_void_p
library.getTrapType.argtypes = [c_void_p, c_int]

library.getTrapTypeCount.restype = c_int
library.getTrapTypeCount.argtypes = [c_void_p]

# getters

#Data
library.playerGetId.restype = c_int
library.playerGetId.argtypes = [c_void_p]

library.playerGetPlayerName.restype = c_char_p
library.playerGetPlayerName.argtypes = [c_void_p]

library.playerGetTime.restype = c_float
library.playerGetTime.argtypes = [c_void_p]

library.playerGetScarabs.restype = c_int
library.playerGetScarabs.argtypes = [c_void_p]

library.playerGetRoundsWon.restype = c_int
library.playerGetRoundsWon.argtypes = [c_void_p]

library.mappableGetId.restype = c_int
library.mappableGetId.argtypes = [c_void_p]

library.mappableGetX.restype = c_int
library.mappableGetX.argtypes = [c_void_p]

library.mappableGetY.restype = c_int
library.mappableGetY.argtypes = [c_void_p]

library.tileGetId.restype = c_int
library.tileGetId.argtypes = [c_void_p]

library.tileGetX.restype = c_int
library.tileGetX.argtypes = [c_void_p]

library.tileGetY.restype = c_int
library.tileGetY.argtypes = [c_void_p]

library.tileGetType.restype = c_int
library.tileGetType.argtypes = [c_void_p]

library.trapGetId.restype = c_int
library.trapGetId.argtypes = [c_void_p]

library.trapGetX.restype = c_int
library.trapGetX.argtypes = [c_void_p]

library.trapGetY.restype = c_int
library.trapGetY.argtypes = [c_void_p]

library.trapGetOwner.restype = c_int
library.trapGetOwner.argtypes = [c_void_p]

library.trapGetTrapType.restype = c_int
library.trapGetTrapType.argtypes = [c_void_p]

library.trapGetVisible.restype = c_int
library.trapGetVisible.argtypes = [c_void_p]

library.trapGetActive.restype = c_int
library.trapGetActive.argtypes = [c_void_p]

library.trapGetBodyCount.restype = c_int
library.trapGetBodyCount.argtypes = [c_void_p]

library.trapGetActivationsRemaining.restype = c_int
library.trapGetActivationsRemaining.argtypes = [c_void_p]

library.trapGetTurnsTillActive.restype = c_int
library.trapGetTurnsTillActive.argtypes = [c_void_p]

library.thiefGetId.restype = c_int
library.thiefGetId.argtypes = [c_void_p]

library.thiefGetX.restype = c_int
library.thiefGetX.argtypes = [c_void_p]

library.thiefGetY.restype = c_int
library.thiefGetY.argtypes = [c_void_p]

library.thiefGetOwner.restype = c_int
library.thiefGetOwner.argtypes = [c_void_p]

library.thiefGetThiefType.restype = c_int
library.thiefGetThiefType.argtypes = [c_void_p]

library.thiefGetAlive.restype = c_int
library.thiefGetAlive.argtypes = [c_void_p]

library.thiefGetSpecialsLeft.restype = c_int
library.thiefGetSpecialsLeft.argtypes = [c_void_p]

library.thiefGetMaxSpecials.restype = c_int
library.thiefGetMaxSpecials.argtypes = [c_void_p]

library.thiefGetMovementLeft.restype = c_int
library.thiefGetMovementLeft.argtypes = [c_void_p]

library.thiefGetMaxMovement.restype = c_int
library.thiefGetMaxMovement.argtypes = [c_void_p]

library.thiefGetFrozenTurnsLeft.restype = c_int
library.thiefGetFrozenTurnsLeft.argtypes = [c_void_p]

library.thiefTypeGetId.restype = c_int
library.thiefTypeGetId.argtypes = [c_void_p]

library.thiefTypeGetName.restype = c_char_p
library.thiefTypeGetName.argtypes = [c_void_p]

library.thiefTypeGetType.restype = c_int
library.thiefTypeGetType.argtypes = [c_void_p]

library.thiefTypeGetCost.restype = c_int
library.thiefTypeGetCost.argtypes = [c_void_p]

library.thiefTypeGetMaxMovement.restype = c_int
library.thiefTypeGetMaxMovement.argtypes = [c_void_p]

library.thiefTypeGetMaxSpecials.restype = c_int
library.thiefTypeGetMaxSpecials.argtypes = [c_void_p]

library.thiefTypeGetMaxInstances.restype = c_int
library.thiefTypeGetMaxInstances.argtypes = [c_void_p]

library.trapTypeGetId.restype = c_int
library.trapTypeGetId.argtypes = [c_void_p]

library.trapTypeGetName.restype = c_char_p
library.trapTypeGetName.argtypes = [c_void_p]

library.trapTypeGetType.restype = c_int
library.trapTypeGetType.argtypes = [c_void_p]

library.trapTypeGetCost.restype = c_int
library.trapTypeGetCost.argtypes = [c_void_p]

library.trapTypeGetMaxInstances.restype = c_int
library.trapTypeGetMaxInstances.argtypes = [c_void_p]

library.trapTypeGetStartsVisible.restype = c_int
library.trapTypeGetStartsVisible.argtypes = [c_void_p]

library.trapTypeGetHasAction.restype = c_int
library.trapTypeGetHasAction.argtypes = [c_void_p]

library.trapTypeGetDeactivatable.restype = c_int
library.trapTypeGetDeactivatable.argtypes = [c_void_p]

library.trapTypeGetMaxActivations.restype = c_int
library.trapTypeGetMaxActivations.argtypes = [c_void_p]

library.trapTypeGetActivatesOnWalkedThrough.restype = c_int
library.trapTypeGetActivatesOnWalkedThrough.argtypes = [c_void_p]

library.trapTypeGetTurnsToActivateOnTile.restype = c_int
library.trapTypeGetTurnsToActivateOnTile.argtypes = [c_void_p]

library.trapTypeGetCanPlaceOnWalls.restype = c_int
library.trapTypeGetCanPlaceOnWalls.argtypes = [c_void_p]

library.trapTypeGetCanPlaceOnOpenTiles.restype = c_int
library.trapTypeGetCanPlaceOnOpenTiles.argtypes = [c_void_p]

library.trapTypeGetFreezesForTurns.restype = c_int
library.trapTypeGetFreezesForTurns.argtypes = [c_void_p]

library.trapTypeGetKillsOnActivate.restype = c_int
library.trapTypeGetKillsOnActivate.argtypes = [c_void_p]

library.trapTypeGetCooldown.restype = c_int
library.trapTypeGetCooldown.argtypes = [c_void_p]

library.trapTypeGetExplosive.restype = c_int
library.trapTypeGetExplosive.argtypes = [c_void_p]

library.trapTypeGetUnpassable.restype = c_int
library.trapTypeGetUnpassable.argtypes = [c_void_p]


#Properties
