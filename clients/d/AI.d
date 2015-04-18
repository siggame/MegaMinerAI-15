import BaseAI, Thief, Trap, ThiefType, TrapType, Tile, structures;
import std.algorithm, std.array, std.stdio, std.typecons, std.random;

///The class implementing gameplay logic.
class AI : BaseAI {
  Player me = null;
  
  public override string username() const {
    return "Shell AI";
  }
  public override string password() const {
    return "password";
  }

  //This function is called each time it is your turn
  //Return true to end your turn, return false to ask the server for updated information
  public override bool run() {
    //Lists storing the sarcophagi
    Trap[] mySarcophagi;
    Trap[] enemySarcophagi;
    
    //If it's time to place traps...
    if (roundTurnNumber() == 0 || roundTurnNumber() == 1) {
      //find my sarcophagi
      foreach (trap; traps) {
        if (trap.getOwner() == playerID() && trap.getTrapType() == TrapType.SARCOPHAGUS) {
          mySarcophagi ~= trap;
        }  
      }
      
      //find the first open tiles and place the sarcophagi there
      int sarcophagusCount = cast(int)mySarcophagi.length;
      foreach (tile; tiles) {
        //if the tile is on my side and is empty
        if (onMySide(tile.getX()) && tile.getType() == Tile.EMPTY) {
          //move my sarcophagus to that location
          me.placeTrap(tile.getX(), tile.getY(), TrapType.SARCOPHAGUS);
          sarcophagusCount--;
          if (sarcophagusCount == 0) {
            break;
          }
        }
      }
      
      //make sure there aren't too many traps spawned
      int[] trapCount = new int[trapTypes.length];
      
      //continue spawning traps until there isn't enough money to spend
      foreach (tile; tiles) {
        //if the tile is on my side
        if (onMySide(tile.getX())) {
          //make sure there isn't a trap on that tile
          if (getTrap(tile.getX(), tile.getY()) !is null) {
            continue;  
          }
          
          //select a random trap type (make sure it isn't a sarcophagus)
          int trapType = uniform(0, cast(int)trapTypes.length-1) + 1;
          
          //make sure another can be spawned
          if (trapCount[trapType] >= trapTypes[trapType].getMaxInstances()) {
            continue;
          }
          
          //if there are enough scarabs...
          if (me.getScarabs() >= trapTypes[trapType].getCost()) {
            //check if the tile is the right type (wall or empty)
            if (trapTypes[trapType].canPlaceOnWalls() == 1 && tile.getType() == Tile.WALL) {
              me.placeTrap(tile.getX(), tile.getY(), trapType);
              trapCount[trapType]++;
            }
            else if (trapTypes[trapType].canPlaceOnWalls() == 0 && tile.getType() == Tile.EMPTY) {
              me.placeTrap(tile.getX(), tile.getY(), trapType);
              trapCount[trapType]++;
            }
          }
          else {
            break;
          }
          
          
        }
      }
    }
    //otherwise it's time to move and purchase thieves and activate traps
    else {
      //find my sarcophagi and the enemy sarcophagi
      foreach (trap; traps) {
        if (trap.getTrapType() == TrapType.SARCOPHAGUS) {
          if (trap.getOwner() != playerID()) {
            enemySarcophagi ~= trap;
          }
          else {
            mySarcophagi ~= trap;
          }
        }
      }
      
      //find my spawn tiles
      Tile[] spawnTiles = getMySpawns();
      
      //select a random thief type
      int thiefNo = uniform(0, cast(int)thiefTypes.length);
      
      //if you can afford the thief
      if (me.getScarabs() >= thiefTypes[thiefNo].getCost()) {
        //make sure another can be spawned
        int max = thiefTypes[thiefNo].getMaxInstances();
        int count = 0;
        Thief[] myThieves = getMyThieves();
        foreach (thief; myThieves) {
          if (thief.getThiefType() == thiefNo) {
            count++;
          }
        }
        
        //only spawn if there aren't too many
        if (count < max) {
          //select a random spawn location
          int spawnLoc = uniform(0, cast(int)spawnTiles.length);
          
          //spawn a thief there
          Tile spawnTile = spawnTiles[spawnLoc];
          me.purchaseThief(spawnTile.getX(), spawnTile.getY(), thiefNo);
        }
      }
      
      //move my thieves
      Thief[] myThieves = getMyThieves();
      foreach (thief; myThieves) {
        //if the thief is alive and not frozen
        if (thief.isAlive() == 1 && thief.getFrozenTurnsLeft() == 0) {
          const int[] xChange = [-1, 1, 0, 0];
          const int[] yChange = [0, 0, -1, 1];
          
          //try to dig or use a bomb before moving
          if (thief.getThiefType() == ThiefType.DIGGER && thief.getSpecialsLeft() > 0) {
            foreach (j; 0..4) {
              //if there is a wall adjacent and an empty space on the other side
              int checkX = thief.getX() + xChange[j];
              int checkY = thief.getY() + yChange[j];
              Tile wallTile = getTile(checkX, checkY);
              Tile emptyTile = getTile(checkX + xChange[j], checkY + yChange[j]);
              
              //must be on the map, and not trying to dig to the other side
              if (wallTile !is null && emptyTile !is null && !onMySide(checkX + xChange[j])) {
                //if there is a wall with an empty tile on the other side
                if (wallTile.getType() == Tile.WALL && emptyTile.getType() == Tile.EMPTY) {
                  //dig through the wall
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
              }
            }
          }
          else if (thief.getThiefType() == ThiefType.BOMBER && thief.getSpecialsLeft() > 0) {
            foreach (j; 0..4) {
              //the place to chceck for things to blow up
              int checkX = thief.getX() + xChange[j];
              int checkY = thief.getY() + yChange[j];
            
              //make sure that the spot isn't on the other side
              if (!onMySide(checkX)) {
                //if there is a wall tile there, blow it up
                Tile checkTile = getTile(checkX, checkY);
                if (checkTile !is null && checkTile.getType() == Tile.WALL) {
                  //blow up the wall
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
                
                //otherwise check if there is a trap there
                Trap checkTrap = getTrap(checkX, checkY);
                
                //don't want to blow up the sarcophagus!
                if (checkTrap !is null && checkTrap.getTrapType() != TrapType.SARCOPHAGUS) {
                  //blow up the trap
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
              }
            }
          }
          
          //if the thief has any movement left
          if (thief.getMovementLeft() > 0) {
            //find a path from the thief's location to the enemy sarcophagus
            int endX = enemySarcophagi[0].getX();
            int endY = enemySarcophagi[0].getY();
            point path = findPath(point(thief.getX(), thief.getY()), point(endX, endY));
            
            //if a path exists then move forward on the path
            if (path.x != -1) {
              thief.move(path.x, path.y);
            }
          }
        }
      }
      
      //do things with traps now
      Trap[] myTraps = getMyTraps();
      foreach (trap; myTraps) {
        const int[] xChange = [-1, 1, 0, 0];  
        const int[] yChange = [0, 0, -1, 1];
        
        //make sure trap can be used
        if (trap.isActive() == 1) {
          //if trap is a boulder
          if (trap.getTrapType() == TrapType.BOULDER) {
            //if there is an enemy thief adjacent
            foreach (j; 0..4) {
              Thief enemyThief = getThief(trap.getX() + xChange[j], trap.getY() + yChange[j]);
              
              //roll over the thief
              if (enemyThief !is null) {
                trap.act(xChange[j], yChange[j]);
                break;
              }
            }
          }
          else if (trap.getTrapType() == TrapType.MUMMY) {
            //move around randomly if a mummy
            int dir = uniform(0, 4);
            int checkX = trap.getX() + xChange[dir];
            int checkY = trap.getY() + yChange[dir];
            Tile checkTile = getTile(checkX, checkY);
            Trap checkTrap = getTrap(checkX, checkY);
            
            //if the tile is empty, and there isn't a sarcophagus there
            if (checkTrap is null || checkTrap.getTrapType() != TrapType.SARCOPHAGUS) {
              if (checkTile !is null && checkTile.getType() == Tile.EMPTY) {
                //move on that tile
                trap.act(checkX, checkY);
              }
            }
          }
        }
        
      }
    }
    
    return true;
  }


  //This function is called once, before your first turn
  public override void init() {
    //Find the player that I am
    me = players[playerID()];
  }
  
  private Thief[] getMyThieves() {
    Thief[] thiefList = [];  
    
    foreach (thief; thieves) {
      if (thief.getOwner() == playerID()) {
        thiefList ~= thief;
      }
    }
    
    return thiefList;
  }
  
  private Thief[] getEnemyThieves() {
    Thief[] thiefList = [];  
    
    foreach (thief; thieves) {
      if (thief.getOwner() != playerID()) {
        thiefList ~= thief;
      }
    }
    
    return thiefList;
  }
  
  private Trap[] getMyTraps() {
    Trap[] trapList = [];  
    
    foreach (trap; traps) {
      if (trap.getOwner() == playerID()) {
        trapList ~= trap;
      }
    }
    
    return trapList;
  }
  
  private Trap[] getEnemyTraps() {
    Trap[] trapList = [];  
    
    foreach (trap; traps) {
      if (trap.getOwner() != playerID()) {
        trapList ~= trap;
      }
    }
    
    return trapList;
  }
  
  private Tile[] getMySpawns() {
    Tile[] tileList = [];
    
    int mapSize = mapHeight();
    tileList ~= getTile(mapSize/2-1 + (1-playerID())*mapSize, 0);
    tileList ~= getTile(mapSize-1 + (1-playerID())*mapSize, mapSize/2-1);
    tileList ~= getTile(mapSize/2+1 + (1-playerID())*mapSize, mapSize-1 );
    tileList ~= getTile((1-playerID())*mapSize, mapSize/2+1);
    
    return tileList;  
  }
  
  private Tile getTile(int x, int y) {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight()) {
      return null;
    }
    return tiles[y + x*mapHeight()];
  }
  
  private Trap getTrap(int x, int y) {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight()) {
      return null;
    }
    
    foreach (trap; traps) {
      if (trap.getX() == x && trap.getY() == y) {
        return trap;
      }
    }
    
    return null;
  }
  
  private Thief getThief(int x, int y) {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight()) {
      return null;
    }
    
    foreach (thief; thieves) {
      if (thief.getX() == x && thief.getY() == y) {
        return thief;
      }
    }
    
    return null;
  }
  
  private bool onMySide(int x) {
    if (playerID() == 0) {
      return (x < mapWidth()/2);
    }
    else {
      return (x >= mapWidth()/2);
    }
  }
  
  alias point = Tuple!(int, "x", int, "y");
  
  private point findPath(point start, point end) {
    point[] toReturn;
    //the set of open tiles to look at
    Tile[] openSet;
    //points back to parent tile
    Tile[Tile] parent;
    
    //push back the starting tile
    openSet ~= getTile(start.x, start.y);
    //the start tile has no parent
    parent[getTile(start.x, start.y)] = null;
    //the end tile
    Tile endTile = getTile(end.x, end.y);
    
    //as long as the end tile has no parent...
    while (count(parent, endTile) == 0) {
      //if there are no tiles in the openSet then there is no path
      if (openSet.length == 0) {
        return point(-1,-1);
      }
      
      //check tiles form the front
      Tile curTile = openSet.front;
      //and remove it
      openSet.remove(0);
      const int xChange[] = [0, 0, -1, 1];
      const int yChange[] = [-1, 1, 0, 0];
      
      //look in all directions
      foreach (i; 0..4) {
        point loc = point(curTile.getX() + xChange[i], curTile.getY() + yChange[i]);
        Tile toAdd = getTile(loc.x, loc.y);
        //if a tile exists there
        if (toAdd !is null) {
          if (toAdd.getType() == Tile.EMPTY && count(parent, toAdd) == 0) {
            openSet ~= toAdd;
            parent[toAdd] = curTile;
          }
        }
      }
    }
    
    //find the path back
    for (Tile tile = endTile; parent[tile] !is null; tile = parent[tile]) {
      toReturn.insertInPlace(0, point(tile.getX(), tile.getY()));
    }
    
    if (toReturn.length != 0) return toReturn.front;
    
    return point(-1,-1);
  }
  
  private int count(ref Tile[Tile] points, Tile tile) {
    int result = 0;
    
    foreach (t; points.values()) {
      if (t !is null && t == tile) {
        result++;
      }
    } 
    
    return result;
  }

  //This function is called once, after your last turn
  public void end() {}
  
  
  this(Connection* c) {
    super(c);
  }
}
