// -*-c++-*-

#include "structures.h"

#include <iostream>

namespace parser
{


std::ostream& operator<<(std::ostream& stream, Player ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "playerName: " << ob.playerName  <<'\n';
  stream << "time: " << ob.time  <<'\n';
  stream << "scarabs: " << ob.scarabs  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, Mappable ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, Tile ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  stream << "type: " << ob.type  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, Trap ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  stream << "owner: " << ob.owner  <<'\n';
  stream << "trapType: " << ob.trapType  <<'\n';
  stream << "visible: " << ob.visible  <<'\n';
  stream << "active: " << ob.active  <<'\n';
  stream << "bodyCount: " << ob.bodyCount  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, Thief ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  stream << "owner: " << ob.owner  <<'\n';
  stream << "thiefType: " << ob.thiefType  <<'\n';
  stream << "alive: " << ob.alive  <<'\n';
  stream << "actionsLeft: " << ob.actionsLeft  <<'\n';
  stream << "maxActions: " << ob.maxActions  <<'\n';
  stream << "movementLeft: " << ob.movementLeft  <<'\n';
  stream << "maxMovement: " << ob.maxMovement  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, ThiefType ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "name: " << ob.name  <<'\n';
  stream << "type: " << ob.type  <<'\n';
  stream << "cost: " << ob.cost  <<'\n';
  stream << "maxActions: " << ob.maxActions  <<'\n';
  stream << "maxMovement: " << ob.maxMovement  <<'\n';
  stream << "maxInstances: " << ob.maxInstances  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, TrapType ob)
{
  stream << "id: " << ob.id  <<'\n';
  stream << "name: " << ob.name  <<'\n';
  stream << "type: " << ob.type  <<'\n';
  stream << "cost: " << ob.cost  <<'\n';
  stream << "startsVisible: " << ob.startsVisible  <<'\n';
  stream << "hasAction: " << ob.hasAction  <<'\n';
  return stream;
}



std::ostream& operator<<(std::ostream& stream, spawn ob)
{
  stream << "spawn" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, move ob)
{
  stream << "move" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "fromX: " << ob.fromX  <<'\n';
  stream << "fromY: " << ob.fromY  <<'\n';
  stream << "toX: " << ob.toX  <<'\n';
  stream << "toY: " << ob.toY  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, kill ob)
{
  stream << "kill" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "targetID: " << ob.targetID  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, pharaohTalk ob)
{
  stream << "pharaohTalk" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "message: " << ob.message  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, thiefTalk ob)
{
  stream << "thiefTalk" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "message: " << ob.message  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, activate ob)
{
  stream << "activate" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, bomb ob)
{
  stream << "bomb" << "\n";
  stream << "actingID: " << ob.actingID  <<'\n';
  stream << "x: " << ob.x  <<'\n';
  stream << "y: " << ob.y  <<'\n';
  return stream;
}


std::ostream& operator<<(std::ostream& stream, GameState ob)
{
  stream << "mapWidth: " << ob.mapWidth  <<'\n';
  stream << "mapHeight: " << ob.mapHeight  <<'\n';
  stream << "turnNumber: " << ob.turnNumber  <<'\n';
  stream << "maxThieves: " << ob.maxThieves  <<'\n';
  stream << "maxTraps: " << ob.maxTraps  <<'\n';
  stream << "playerID: " << ob.playerID  <<'\n';
  stream << "gameNumber: " << ob.gameNumber  <<'\n';
  stream << "roundNumber: " << ob.roundNumber  <<'\n';
  stream << "scarabsForTraps: " << ob.scarabsForTraps  <<'\n';
  stream << "scarabsForThieves: " << ob.scarabsForThieves  <<'\n';
  stream << "maxStack: " << ob.maxStack  <<'\n';

  stream << "\n\nPlayers:\n";
  for(std::map<int,Player>::iterator i = ob.players.begin(); i != ob.players.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nMappables:\n";
  for(std::map<int,Mappable>::iterator i = ob.mappables.begin(); i != ob.mappables.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nTiles:\n";
  for(std::map<int,Tile>::iterator i = ob.tiles.begin(); i != ob.tiles.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nTraps:\n";
  for(std::map<int,Trap>::iterator i = ob.traps.begin(); i != ob.traps.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nThiefs:\n";
  for(std::map<int,Thief>::iterator i = ob.thiefs.begin(); i != ob.thiefs.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nThiefTypes:\n";
  for(std::map<int,ThiefType>::iterator i = ob.thiefTypes.begin(); i != ob.thiefTypes.end(); i++)
    stream << i->second << '\n';
  stream << "\n\nTrapTypes:\n";
  for(std::map<int,TrapType>::iterator i = ob.trapTypes.begin(); i != ob.trapTypes.end(); i++)
    stream << i->second << '\n';
  stream << "\nAnimation\n";
  for
    (
    std::map< int, std::vector< SmartPointer< Animation > > >::iterator j = ob.animations.begin(); 
    j != ob.animations.end(); 
    j++ 
    )
  {
  for(std::vector< SmartPointer< Animation > >::iterator i = j->second.begin(); i != j->second.end(); i++)
  {
//    if((*(*i)).type == SPAWN)
//      stream << *((spawn*)*i) << "\n";
//    if((*(*i)).type == MOVE)
//      stream << *((move*)*i) << "\n";
//    if((*(*i)).type == KILL)
//      stream << *((kill*)*i) << "\n";
//    if((*(*i)).type == PHARAOHTALK)
//      stream << *((pharaohTalk*)*i) << "\n";
//    if((*(*i)).type == THIEFTALK)
//      stream << *((thiefTalk*)*i) << "\n";
//    if((*(*i)).type == ACTIVATE)
//      stream << *((activate*)*i) << "\n";
//    if((*(*i)).type == BOMB)
//      stream << *((bomb*)*i) << "\n";
  }
  

  }
  return stream;
}

Game::Game()
{
  winner = -1;
}

} // parser
