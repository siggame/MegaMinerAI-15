# -*- coding: iso-8859-1 -*-
from structures import *

aspects = ['timer']

gameName = "Pharaoh"

constants = [
  ]

modelOrder = ['Player', 'Mappable', 'Tile', 'Trap', 'Thief', 'ThiefType', 'TrapType']

globals = [
  Variable('mapWidth', int, 'The width of the total map.'),
  Variable('mapHeight', int, 'The height of the total map.'),
  Variable('turnNumber', int, 'The current turn number.'),
  Variable('maxThieves', int, 'The maximum number of Thieves allowed per player.'),
  Variable('maxTraps', int, 'The maximum number of Traps allowed per player.'),
  Variable('playerID', int, 'The id of the current player.'),
  Variable('gameNumber', int, 'What number game this is for the server.'),
  Variable('roundNumber', int, 'What round of the game this is.'),
  Variable('scarabsForTraps', int, 'The scarabs given to a player to purchase traps per round.'),
  Variable('scarabsForThieves', int, 'The scarabs given to a player to purchase thieves per round.'),
  Variable('maxStack', int, 'The maximum number of thieves per tile.'),
]

playerData = [
  Variable('scarabs', int, 'The number of scarabs this player has to purchase traps or thieves.'),
  ]

playerFunctions = [
  Function('placeTrap', [Variable('x', int), Variable('y', int), Variable('trapType', int)],
  doc='Place the specified trap type at the given location.'),
  Function('purchaseThief', [Variable('x', int), Variable('y', int), Variable('thiefType', int)],
  doc='Place the specified thief type at the given location.'),
  Function('pharaohTalk', [Variable('message', str)], doc='Display a message on the screen.'),
]

#MAPPABLE
Mappable = Model('Mappable',
  data=[
    Variable('x', int, 'X position of the object'),
    Variable('y', int, 'Y position of the object')
  ],
  doc='A mappable object!',
)

#THIEF
Thief = Model('Thief',
  parent = Mappable,
  data = [
    Variable('owner', int, 'The owner of this thief.'),
    Variable('thiefType', int, 'The type of this thief. This type refers to list of thiefTypes.'),

    Variable('alive', int, 'Whether the thief is alive or not.'),

    Variable('actionsLeft', int, 'The remaining number of times the thief can act.'),
    Variable('maxActions', int, 'The maximum number of times the thief can act.'),

    Variable('movementLeft', int, 'The remaining number of times this thief can move.'),
    Variable('maxMovement', int, 'The maximum number of times this thief can move.'),
    ],
  doc='Represents a single thief on the map.',
  functions=[
    Function('thiefTalk', [Variable('message', str)],
    doc='Allows a thief to display messages on the screen'),

    Function('move', [Variable('x', int), Variable('y', int)],
    doc='Commands a thief to move to a new location.'),

    Function('act', [Variable('x', int), Variable('y', int)],
    doc='Commands a thief to act on a location.'),
  ],
)

#THIEFTYPE
ThiefType = Model('ThiefType',
  data = [
    Variable('name', str, 'The name of this type of thief.'),
    Variable('type', int, 'The type of this thief. This value is unique for all types.'),
    Variable('cost', int, 'The number of scarabs required to purchase this thief.'),

    Variable('maxActions', int, 'The maximum number of times the thief can act.'),
    Variable('maxMovement', int, 'The maximum number of times this thief can move.'),

    Variable('maxInstances', int, 'The maximum number of this type thief that can be purchased each round.'),
    ],
  doc='Represents a type of thief.',
  functions=[],
  permanent = True,
  )


#TRAP
Trap = Model('Trap',
  parent = Mappable,
  data = [
    Variable('owner', int, 'The owner of this trap.'),
    Variable('trapType', int, 'The type of this trap. This type refers to list of trapTypes.'),

    Variable('visible', int, 'Whether the trap is visible to the enemy player.'),
    Variable('active', int, 'Whether the trap is active.'),

    Variable('bodyCount', int, 'How many thieves this trap has killed.'),
    ],
  doc='Represents a single trap on the map.',
  functions=[
    Function('act', [Variable('x', int), Variable('y', int)],
    doc='Commands a trap to act on a location.'),

    Function('toggle', [],
    doc='Commands a trap to toggle between being activated or not.'),
  ],
)

#TRAPTYPE
TrapType = Model('TrapType',
  data = [
    Variable('name', str, 'The name of this type of trap.'),
    Variable('type', int, 'The type of this trap. This value is unique for all types.'),
    Variable('cost', int, 'The number of scarabs required to purchase this trap.'),

    Variable('startsVisible', int, 'Whether the trap starts visible to the enemy player.'),
    Variable('hasAction', int, 'Whether the trap is able to act().'),
    ],
  doc='Represents a type of trap.',
  functions=[],
  permanent = True,
  )

#TILE
Tile = Model('Tile',
  parent = Mappable,
  data = [
    Variable('type', int, 'What type of tile this is. 0: empty, 1: wall: 2: spawn.'),
    ],
  doc='Represents a tile.',
  functions=[],
  permanent = True,
  )

move = Animation('move',
  data=[
    Variable('actingID', int),
    Variable('fromX', int),
    Variable('fromY', int),
    Variable('toX', int),
    Variable('toY', int)
  ],
  )

bomb = Animation('bomb',
  data=[
    Variable('actingID', int),
    Variable('x', int),
    Variable('y', int)
  ],
  )

activate = Animation('activate',
  data=[
    Variable('actingID', int)
  ],
  )

kill = Animation('kill',
  data=[
    Variable('actingID', int),
    Variable('targetID', int)
  ],
  )

spawn = Animation('spawn',
  data=[
    Variable('actingID', int),
    Variable('x', int),
    Variable('y', int)
  ],
  )

thiefTalk = Animation('thiefTalk',
  data=[
    Variable('actingID', int),
    Variable('message', str)
  ],
  )

pharaohTalk = Animation('pharaohTalk',
  data=[
    Variable('actingID', int),
    Variable('message', str)
  ],
  )
