import com.sun.jna.Pointer;
import java.util.Random;
import java.util.ArrayList;
import java.util.Deque;

///The class implementing gameplay logic.
public class AI extends BaseAI
{
  Player me = null;
  Random rand;
  
  public String username()
  {
    return "Shell AI";
  }
  public String password()
  {
    return "password";
  }

  //This function is called each time it is your turn
  //Return true to end your turn, return false to ask the server for updated information
  public boolean run()
  {
    //Lists storing the sarcophagi
    ArrayList<Trap> mySarcophagi = new ArrayList<Trap>();
    ArrayList<Trap> enemySarcophagi = new ArrayList<Trap>();
    
    //If it's time to place traps...
    if (roundTurnNumber() == 0 || roundTurNumber() == 1)
    {
      //find my sarcophagi
      for (int i = 0; i < traps.size(); i++)
      {
        Trap trap = traps[i];
        if (trap.getOwner() == playerID() && trap.trapType() == TrapType.SARCOPHAGUS)
        {
          mySarcophagi.add(trap);
        }  
      }
      
      //find the first open tiles and place the sarcophagi there
      int sarcophagusCount = mySarcophagi.size();
      for (int i = 0; i < tiles.size(); i++)
      {
        //if the tile is on my side and is empty
        Tile tile = tiles[i];
        if (onMySide(tile.x()) && tile.type() == Tile.EMPTY)
        {
          //move my sarcophagus to that location
          me.placeTrap(tile.getX(), tile.getY(), TrapType.SARCOPHAGUS);
          sarcophagusCount--;
          if (sarcophagusCount == 0)
          {
            break;
          }
        }
      }
      
      //make sure there aren't too many traps spawned
      int[] trapCount = new int[trapTypes.length];
      
      //continue spawning traps until there isn't enough money to spend
      for (int i = 0; i < tiles.size(); i++)
      {
        //if the tile is on my side
        Tile tile = tiles[i];
        if (onMySide(tile.getX()))
        {
          //make sure there isn't a trap on that tile
          if (getTrap(tile.getX(), tile.getY()) != null)
          {
            continue;  
          }
          
          //select a random trap type (make sure it isn't a sarcophagus)
          int trapType = rand.nextInt(trapTypes.size()-1) + 1;
          
          //make sure another can be spawned
          if (trapCount[trapType] < trapTypes[trapType].getMaxInstances())
          {
            continue;
          }
          
          //if there are enough scarabs...
          if (me.getScarabs() >= trapTypes[trapType].getCost())
          {
            //check if the tile is the right type (wall or empty)
            if (trapTypes[trapType].canPlaceOnWalls() && tile.type() == Tile.WALL)
            {
              me.placeTrap(tile.getX(), tile.getY(), trapType);
              trapCount[trapType]++;
            }
            else if (!trapTypes[trapType].canPlaceOnWalls() && tile.type() == Tile.EMPTY)
            {
              me.placeTrap(tile.getX(), tile.getY(), trapType);
              trapCount[trapType]++;
            }
          }
          else 
          {
            break;
          }
          
          
        }
      }
    }
    //otherwise it's time to move and purchase thieves and activate traps
    else
    {
      //find my sarcophagi and the enemy sarcophagi
      for (int i = 0; i < traps.size(); i++)
      {
        Trap trap = traps[i];
        if (trap.getTrapType() == TrapType.SARCOPHAGUS)
        {
          if (trap.getOwner() != playerID())
          {
            enemySarcophagi.add(trap);
          }
          else
          {
            mySarcophagi.add(trap);
          }
        }
      }
      
      //find my spawn tiles
      ArrayList<Tile> spawnTiles = new getMySpawns();
      
      //select a random thief type
      int thiefNo = rand.nextInt(thiefTypes.length);
      
      //if you can afford the thief
      if (me.getScarabs() >= thiefTypes[thiefNo].cost())
      {
        //make sure another can be spawned
        int max = thiefTypes[thiefNo].getMaxInstances();
        int count = 0;
        ArrayList<Thief> myThieves = getMyThieves();
        for (int i = 0; i < myThieves.size(); i++)
        {
          if (myThieves.get(i).getThiefType() == thiefNo)
          {
            count++;
          }
        }
        
        //only spawn if there aren't too many
        if (count < max)
        {
          //select a random spawn location
          int spawnLoc = rand.nextInt(spawnTiles.size());
          
          //spawn a thief there
          Tile spawnTile = spawnTiles.get(spawnLoc);
          me.purchaseThief(spawnTile.getX(), spawnTile.getY(), thiefNo);
        }
      }
      
      //move my thieves
      ArrayList<Thief> myThieves = getMyThieves();
      for (int i = 0; i < myThieves.size(); i++)
      {
        Thief thief = myThieves.get(i);
        
        //if the thief is alive and not frozen
        if (thief.isAlive() && thief.getFrozenTurnsLeft() == 0)
        {
          final int[] xChange = new int[]{-1, 1, 0, 0};
          final int[] yChange = new int[]{0, 0, -1, -1};
          
          //try to dig or use a bomb before moving
          if (thief.getThiefType() == ThiefType.DIGGER && thief.getSpecialsLeft() > 0)
          {
            for (int i = 0; i < 4; i++)
            {
              //if there is a wall adjacent and an empty space on the other side
              int checkX = thief.getX() + xChange[i];
              int checkY = thief.getY() + yChange[i];
              Tile wallTile = getTile(checkX, checkY);
              Tile emptyTile = getTile(checkX + xChange[i], checkY + yChange[i]);
              
              //must be on the map, and not trying to dig to the other side
              if (wallTile != null && emptyTile != null && !onMySide(checkX + xChange[i]))
              {
                //if there is a wall with an empty tile on the other side
                if (wallTile.getType() == Tile.WALL && emptyTile.getType() == Tile.EMPTY)
                {
                  //dig through the wall
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
              }
            }
          }
          else if thief.getType() == ThiefType.BOMBER && thief.getSpecialsLeft() > 0)
          {
            for (int i = 0; i < 4; i++)
            {
              //the place to chceck for things to blow up
              int checkX = thief.getX() + xChange[i];
              int checkY = thief.getY() + yChange[i];
            
              //make sure that the spot isn't on the other side
              if (!onMySide(checkX))
              {
                //if there is a wall tile there, blow it up
                Tile checkTile = getTile(checkX, checkY);
                if (checkTile != null && checkTile.getType() == Tile.WALL)
                {
                  //blow up the wall
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
                
                //otherwise check if there is a trap there
                Trap checkTrap = getTrap(checkX, checkY);
                
                //don't want to blow up the sarcophagus!
                if (checkTrap != null && checkTrap.getTrapType() != TrapType.SARCOPHAGUS)
                {
                  //blow up the trap
                  thief.useSpecial(checkX, checkY);
                  
                  //break out of the loop
                  break;
                }
              }
            }
          }
          
          //if the thief has any movement left
          if (thief.getMovementLeft() > 0)
          {
            //find a path from the thief's location to the enemy sarcophagus
            Deque<Point> path = new Deque<Point>();
            int endX = enemySarcophagi.get(0).getX();
            int endY = enemySarcophagi.get(0).getY();
            path = findPath(new Point(thief.getX(), thief.getY()), new Point(endX, endY));
            
            //if a path exists then move forward on the path
            if (path.size() > 0)
            {
              thief.move(path.getFirst().x, path.getFirst());
            }
          }
        }
      }
      
      //do things with traps now
      ArrayList<Trap> myTraps = getMyTraps();
      for (int i = 0; i < myTraps.size(); i++)
      {
        final int[] xChange = new int[]{-1, 1, 0, 0};  
        final int[] yChange = new int[]{0, 0, -1, -1};  
        Trap trap = myTraps.get(i);
        
        //make sure trap can be used
        if (trap.isActive())
        {
          //if trap is a boulder
          if (trap.getTrapType() == TrapType.BOULDER)
          {
            //if there is an enemy thief adjacent
            for (int i = 0; i < 4; i++)
            {
              Thief enemyThief = getThief(trap.getX() + xChange[i], trap.getY() + yChange[i]);
              
              //roll over the thief
              if (enemyThief != null)
              {
                trap.act(xChange[i], yChange[i]);
                break;
              }
            }
          }
          else if (trap.getTrapType() == TrapType.MUMMY)
          {
            //move around randomly if a mummy
            int dir = rand.nextInt(4);
            int checkX = trap.getX() + xChange[dir];
            int checkY = trap.getY() + yChange[dir];
            
            //if the tile is empty, and there isn't a sarcophagus there
            if (checkTrap == null || checkTrap.getTrapType() != TrapType.SARCOPHAGUS)
            {
              if (checkTile != null && checkTile.getType() == Tile.EMPTY)
              {
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
  public void init()
  {
    //itialize RNG
    rand = new Random();
    
    //Find the player that I am
    me = players[playerID()];
  }
  
  private ArrayList<Thief> getMyThieves()
  {
    ArrayList<Thief> thiefList = new ArrayList<Thief>();  
    
    for (int i = 0; i < thieves.length; i++)
    {
      Thief thief = thieves[i];
      if (thief.getOwner() == playerID())
      {
        thiefList.add(thief);
      }
    }
    
    return thiefList;
  }
  
  private ArrayList<Thief> getEnemyThieves()
  {
    ArrayList<Thief> thiefList = new ArrayList<Thief>();  
    
    for (int i = 0; i < thieves.length; i++)
    {
      Thief thief = thieves[i];
      if (thief.getOwner() != playerID())
      {
        thiefList.add(thief);
      }
    }
    
    return thiefList;
  }
  
  private ArrayList<Thief> getMyTraps()
  {
    ArrayList<Trap> trapList = new ArrayList<Trap>();  
    
    for (int i = 0; i < traps.length; i++)
    {
      Trap trap = traps[i];
      if (trap.getOwner() == playerID())
      {
        trapList.add(trap);
      }
    }
    
    return trapList;
  }
  
  private ArrayList<Thief> getEnemyTraps()
  {
    ArrayList<Trap> trapList = new ArrayList<Trap>();  
    
    for (int i = 0; i < traps.length; i++)
    {
      Trap trap = traps[i];
      if (trap.getOwner() != playerID())
      {
        trapList.add(trap);
      }
    }
    
    return trapList;
  }
  
  private ArrayList<Tile> getMySpawns()
  {
    ArrayList<Tile> tileList = new ArrayList<Tile>();
    
    int mapSize = mapHeight();
    tileList.add( getTile(mapSize/2-1, (1-playerID())*mapSize, 0) );
    tileList.add( getTile(mapSize-1 + (1-playerID())*mapSize, mapSize/2-1) );
    tileList.add( getTile(mapSize/2+1 + (1-playerID())*mapSize, mapSize-1 ) );
    tileList.add( getTile((1-playerID())*mapSize, mapSize/2+1) );
    
    return tileList;  
  }
  
  private Tile getTile(int x, int y) 
  {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight())
    {
      return null;
    }
    return tiles[y + x*mapHeight()];
  }
  
  private Trap getTrap(int x, int y)
  {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight())
    {
      return null;
    }
    
    for (int i = 0; i < traps.length; i++)
    {
      if (traps[i].getX() == x && traps[i].getY() == y)
      {
        return traps[i];
      }
    }
    
    return null;
  }
  
  private Thief getThief(int x, int y)
  {
    if (x < 0 || x >= mapWidth() || y < 0 || y >= mapHeight())
    {
      return null;
    }
    
    for (int i = 0; i < thieves.length; i++)
    {
      if (thieves[i].getX() == x && thieves[i].getY() == y)
      {
        return thieves[i];
      }
    }
    
    return null;
  }
  
  private boolean onMySide(int x)
  {
    if (playerID() == 0)
    {
      return (x < mapWidth()/2);
    }
    else
    {
      return (x >= mapWidth()/2);
    }
  }
  
  
  private static class Point {
    int x, y;
    Point(int x, int y) { this.x = x; this.y = y; }
  }
  
  
  Deque<Point> findPath(Point start, Point end)
  {
    Deque<Point> toReturn = new Deque<Point>;
    //the set of open tiles to look at
    Deque<Tile> openSet = new Deque<Tile>;
    //points back to parent tile
    HashMap<Tile, Tile> parent = new HashMap<Tile, Tile>();
    
    //push back the starting tile
    openSet.add(getTile(start.x, start.y));
    //the start tile has no parent
    parent.put(getTile(start.x, start.y), null);
    //the end tile
    Tile endTile = getTile(end.x, end.y);
    
    //as long as the end tile has no parent...
    while (parent.count(endTile) == 0)
    {
      //if there are no tiles in the openSet then there is no path
      if (openSet.isEmpty())
      {
        return toReturn;
      }
      
      //check tiles form the front
      Tile curTile = openSet.getFirst();
      //and remove it
      openSet.pop();
      final int xChange[] = {0, 0, -1, -1};
      final int yChange[] = {1, 1, 0, 0};
      
      //look in all directions
      for (int i = 0; i < 4; i++)
      {
        Point loc = new Point(curTile.x + xChange[i], curTile.y + yChange[i]);
        Tile toAdd = getTile(loc.x, loc.y);
        //if a tile exists there
        if (toAdd != null)
        {
          if (toAdd.getType() == Tile.EMPTY && parent.count(toAdd) == 0)
          {
            openSet.addLast(toAdd);
            parent.put(toAdd, curTile);
          }
        }
      }
    }
    
    //find the path back
    for (Tile tile = endTile; parent.get(Tile) != null; tile = parent.get(tile))
    {
      toReturn.addFirst(new Point(tile.x, tile.y));
    }
    
    return toReturn;
  }

  //This function is called once, after your last turn
  public void end() {}
  
  
  public AI(Pointer c)
  {
    super(c);
  }
}
