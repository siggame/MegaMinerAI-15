#include "parser.h"
#include "sexp/sexp.h"
#include "sexp/parser.h"
#include "sexp/sfcompat.h"

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>

using namespace std;

namespace parser
{

char *ToLower( char *str )
{
  for( int i = 0; i < strlen( str ); i++ )
  {
    str[ i ] = tolower( str[ i ] );
  }
  return str;
}


static bool parsePlayer(Player& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parsePlayer.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parsePlayer.\n Parsing: " << *expression << endl;
    return false;
  }

  object.playerName = new char[strlen(sub->val)+1];
  strncpy(object.playerName, sub->val, strlen(sub->val));
  object.playerName[strlen(sub->val)] = 0;
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parsePlayer.\n Parsing: " << *expression << endl;
    return false;
  }

  object.time = atof(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parsePlayer.\n Parsing: " << *expression << endl;
    return false;
  }

  object.scarabs = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parsePlayer.\n Parsing: " << *expression << endl;
    return false;
  }

  object.roundsWon = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseMappable(Mappable& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseMappable.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseMappable.\n Parsing: " << *expression << endl;
    return false;
  }

  object.x = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseMappable.\n Parsing: " << *expression << endl;
    return false;
  }

  object.y = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseTile(Tile& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseTile.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTile.\n Parsing: " << *expression << endl;
    return false;
  }

  object.x = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTile.\n Parsing: " << *expression << endl;
    return false;
  }

  object.y = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTile.\n Parsing: " << *expression << endl;
    return false;
  }

  object.type = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseTrap(Trap& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.x = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.y = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.owner = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.trapType = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.visible = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.active = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrap.\n Parsing: " << *expression << endl;
    return false;
  }

  object.bodyCount = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseThief(Thief& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.x = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.y = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.owner = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.thiefType = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.alive = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.ninjaReflexesLeft = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxNinjaReflexes = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.movementLeft = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxMovement = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThief.\n Parsing: " << *expression << endl;
    return false;
  }

  object.frozenTurnsLeft = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseThiefType(ThiefType& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.name = new char[strlen(sub->val)+1];
  strncpy(object.name, sub->val, strlen(sub->val));
  object.name[strlen(sub->val)] = 0;
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.type = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.cost = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxMovement = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxNinjaReflexes = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseThiefType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxInstances = atoi(sub->val);
  sub = sub->next;

  return true;

}
static bool parseTrapType(TrapType& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  sub = expression->list;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.id = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.name = new char[strlen(sub->val)+1];
  strncpy(object.name, sub->val, strlen(sub->val));
  object.name[strlen(sub->val)] = 0;
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.type = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.cost = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.startsVisible = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.hasAction = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.activatable = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxBodyCount = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.maxInstances = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.killsOnWalkThrough = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.turnsToKillOnTile = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.canPlaceInWalls = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.canPlaceInEmptyTiles = atoi(sub->val);
  sub = sub->next;

  if ( !sub ) 
  {
    cerr << "Error in parseTrapType.\n Parsing: " << *expression << endl;
    return false;
  }

  object.freezesForTurns = atoi(sub->val);
  sub = sub->next;

  return true;

}

static bool parseSpawn(spawn& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = SPAWN;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsespawn.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsespawn.\n Parsing: " << *expression << endl;
    return false;
  }
  object.x = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsespawn.\n Parsing: " << *expression << endl;
    return false;
  }
  object.y = atoi(sub->val);
  sub = sub->next;
  return true;

}
static bool parseMove(move& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = MOVE;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsemove.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsemove.\n Parsing: " << *expression << endl;
    return false;
  }
  object.fromX = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsemove.\n Parsing: " << *expression << endl;
    return false;
  }
  object.fromY = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsemove.\n Parsing: " << *expression << endl;
    return false;
  }
  object.toX = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsemove.\n Parsing: " << *expression << endl;
    return false;
  }
  object.toY = atoi(sub->val);
  sub = sub->next;
  return true;

}
static bool parseKill(kill& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = KILL;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsekill.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsekill.\n Parsing: " << *expression << endl;
    return false;
  }
  object.targetID = atoi(sub->val);
  sub = sub->next;
  return true;

}
static bool parsePharaohTalk(pharaohTalk& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = PHARAOHTALK;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsepharaohTalk.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsepharaohTalk.\n Parsing: " << *expression << endl;
    return false;
  }
  object.message = new char[strlen(sub->val)+1];
  strncpy(object.message, sub->val, strlen(sub->val));
  object.message[strlen(sub->val)] = 0;
  sub = sub->next;
  return true;

}
static bool parseThiefTalk(thiefTalk& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = THIEFTALK;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsethiefTalk.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsethiefTalk.\n Parsing: " << *expression << endl;
    return false;
  }
  object.message = new char[strlen(sub->val)+1];
  strncpy(object.message, sub->val, strlen(sub->val));
  object.message[strlen(sub->val)] = 0;
  sub = sub->next;
  return true;

}
static bool parseActivate(activate& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = ACTIVATE;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parseactivate.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  return true;

}
static bool parseBomb(bomb& object, sexp_t* expression)
{
  sexp_t* sub;
  if ( !expression ) return false;
  object.type = BOMB;
  sub = expression->list->next;
  if( !sub ) 
  {
    cerr << "Error in parsebomb.\n Parsing: " << *expression << endl;
    return false;
  }
  object.actingID = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsebomb.\n Parsing: " << *expression << endl;
    return false;
  }
  object.x = atoi(sub->val);
  sub = sub->next;
  if( !sub ) 
  {
    cerr << "Error in parsebomb.\n Parsing: " << *expression << endl;
    return false;
  }
  object.y = atoi(sub->val);
  sub = sub->next;
  return true;

}

static bool parseSexp(Game& game, sexp_t* expression)
{
  sexp_t* sub, *subsub;
  if( !expression ) return false;
  expression = expression->list;
  if( !expression ) return false;
  if(expression->val != NULL && strcmp(expression->val, "status") == 0)
  {
    GameState gs;
    while(expression->next != NULL)
    {
      expression = expression->next;
      sub = expression->list;
      if ( !sub ) return false;
      if(string(sub->val) == "game")
      {
          sub = sub->next;
          if ( !sub ) return false;
          gs.mapWidth = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.mapHeight = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.turnNumber = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.roundTurnNumber = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.maxThieves = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.maxTraps = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.playerID = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.gameNumber = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.roundNumber = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.scarabsForTraps = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.scarabsForThieves = atoi(sub->val);
          sub = sub->next;
          if ( !sub ) return false;
          gs.maxStack = atoi(sub->val);
          sub = sub->next;
      }
      else if(string(sub->val) == "Player")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          Player object;
          flag = parsePlayer(object, sub);
          gs.players[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "Mappable")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          Mappable object;
          flag = parseMappable(object, sub);
          gs.mappables[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "Tile")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          Tile object;
          flag = parseTile(object, sub);
          gs.tiles[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "Trap")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          Trap object;
          flag = parseTrap(object, sub);
          gs.traps[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "Thief")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          Thief object;
          flag = parseThief(object, sub);
          gs.thiefs[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "ThiefType")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          ThiefType object;
          flag = parseThiefType(object, sub);
          gs.thiefTypes[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
      else if(string(sub->val) == "TrapType")
      {
        sub = sub->next;
        bool flag = true;
        while(sub && flag)
        {
          TrapType object;
          flag = parseTrapType(object, sub);
          gs.trapTypes[object.id] = object;
          sub = sub->next;
        }
        if ( !flag ) return false;
      }
    }
    game.states.push_back(gs);
  }
  else if(string(expression->val) == "animations")
  {
    std::map< int, std::vector< SmartPointer< Animation > > > animations;
    while(expression->next)
    {
      expression = expression->next;
      sub = expression->list;
      if ( !sub ) return false;
      if(string(ToLower( sub->val ) ) == "spawn")
      {
        SmartPointer<spawn> animation = new spawn;
        if ( !parseSpawn(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "move")
      {
        SmartPointer<move> animation = new move;
        if ( !parseMove(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "kill")
      {
        SmartPointer<kill> animation = new kill;
        if ( !parseKill(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "pharaoh-talk")
      {
        SmartPointer<pharaohTalk> animation = new pharaohTalk;
        if ( !parsePharaohTalk(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "thief-talk")
      {
        SmartPointer<thiefTalk> animation = new thiefTalk;
        if ( !parseThiefTalk(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "activate")
      {
        SmartPointer<activate> animation = new activate;
        if ( !parseActivate(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
      if(string(ToLower( sub->val ) ) == "bomb")
      {
        SmartPointer<bomb> animation = new bomb;
        if ( !parseBomb(*animation, expression) )
          return false;

        animations[ ((AnimOwner*)&*animation)->owner ].push_back( animation );
      }
    }
    game.states[game.states.size()-1].animations = animations;
  }
  else if(string(expression->val) == "ident")
  {
    expression = expression->next;
    if ( !expression ) return false;
    sub = expression->list;
    while(sub)
    {
      subsub = sub->list;
      if ( !subsub ) return false;
      int number = atoi(subsub->val);
      if(number >= 0)
      {
        subsub = subsub->next;
        if ( !subsub ) return false;
        subsub = subsub->next;
        if ( !subsub ) return false;
        game.players[number] = subsub->val;
      }
      sub = sub->next;
    }
  }
  else if(string(expression->val) == "game-winner")
  {
    expression = expression->next;
    if ( !expression ) return false;
    expression = expression->next;
    if ( !expression ) return false;
    expression = expression->next;
    if ( !expression ) return false;
    game.winner = atoi(expression->val);
		expression = expression->next;
		if( !expression ) return false;
		game.winReason = expression->val;
  }

  return true;
}


bool parseFile(Game& game, const char* filename)
{
  //bool value;
  FILE* in = fopen(filename, "r");
  //int size;
  if(!in)
    return false;

  parseFile(in);

  sexp_t* st = NULL;

  while((st = parse()))
  {
    if( !parseSexp(game, st) )
    {
      while(parse()); //empty the file, keep Lex happy.
      fclose(in);
      return false;
    }
    destroy_sexp(st);
  }

  fclose(in);

  return true;
}


bool parseGameFromString(Game& game, const char* string)
{

  parseString( string );

  sexp_t* st = NULL;

  while((st = parse()))
  {
    if( !parseSexp(game, st) )
    {
      while(parse()); //empty the file, keep Lex happy.
      return false;
    }
    destroy_sexp(st);
  }

  return true;
}

} // parser
