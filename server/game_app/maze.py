import random

#directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

#map array states
EMPTY = 0
SPAWN = 1
WALL = 2

class Wall:
  def __init__(self, x, y, wallDir):
    self.x = x
    self.y = y
    self.wallDir = wallDir
    
class BFSTile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.data = -1

#implement breadth-first search. thanks again, wikipedia
def getPathLength(map, startX, startY, endX, endY):
  queue = []
  tiles = [[BFSTile(x,y) for y in range(len(map))] for x in range(len(map))] 
  
  tiles[startX][startY].data = 4
  queue.append(tiles[startX][startY])
  
  while len(queue) != 0:
    v = queue[0]
    del queue[0]
    
    if v.x == endX and v.y == endY:
      break
      
    if v.x > 0 and map[v.x-1][v.y] == EMPTY:
      if tiles[v.x-1][v.y].data == -1:
        queue.append(tiles[v.x-1][v.y])
        tiles[v.x-1][v.y].data = EAST
    if v.y > 0 and map[v.x][v.y-1] == EMPTY:
      if tiles[v.x][v.y-1].data == -1:
        queue.append(tiles[v.x][v.y-1])
        tiles[v.x][v.y-1].data = SOUTH
    if v.x < len(map)-1 and map[v.x+1][v.y] == EMPTY:
      if tiles[v.x+1][v.y].data == -1:
        queue.append(tiles[v.x+1][v.y])
        tiles[v.x+1][v.y].data = WEST
    if v.y < len(map)-1 and map[v.x][v.y+1] == EMPTY:
      if tiles[v.x][v.y+1].data == -1:
        queue.append(tiles[v.x][v.y+1])
        tiles[v.x][v.y+1].data = NORTH
        
  length = 0
  runBack = tiles[endX][endY]
  while runBack.data != 4:
    if runBack.data == NORTH:
      runBack = tiles[runBack.x][runBack.y-1]
    if runBack.data == EAST:
      runBack = tiles[runBack.x+1][runBack.y]
    if runBack.data == SOUTH:
      runBack = tiles[runBack.x][runBack.y+1]
    if runBack.data == WEST:
      runBack = tiles[runBack.x-1][runBack.y]
    
    length += 1
  
  return length
        
#generate maze using prim's algorithm. thanks wikipedia
def generate(size):
  map = [[WALL for y in range(size)] for x in range(size)] 
  walls = []
  
  #choose starting position and add walls
  firstX = random.randint(0,size/2-1)*2+1;
  firstY = random.randint(0,size/2-1)*2+1;
  map[firstX][firstY] = EMPTY
  
  if firstX > 1:
    walls.append(Wall(firstX-1, firstY, WEST))
  if firstY > 1:
    walls.append(Wall(firstX, firstY-1, NORTH))
  if firstX < size-2:
    walls.append(Wall(firstX+1, firstY, EAST))
  if firstY < size-2:
    walls.append(Wall(firstX, firstY+1, SOUTH))    
    
  while len(walls) != 0:
    #randomly choose wall from list
    chosenIndex = random.randint(0,len(walls)-1);
    chosenWall = walls[chosenIndex]
    
    otherSideIsInMaze = False
    otherSideX = chosenWall.x
    otherSideY = chosenWall.y
    
    #get tile on other side of wall
    if chosenWall.wallDir == NORTH:
      otherSideY -= 1
    elif chosenWall.wallDir == EAST:
      otherSideX += 1
    elif chosenWall.wallDir == SOUTH:
      otherSideY += 1
    else:
      otherSideX -= 1
    otherSideIsInMaze = map[otherSideX][otherSideY] == EMPTY
    
    #break down wall to other side
    if not otherSideIsInMaze:
      map[otherSideX][otherSideY] = EMPTY
      map[chosenWall.x][chosenWall.y] = EMPTY
      
      #add surrounding walls to wall list
      if otherSideX > 1 and chosenWall.wallDir != 1 and map[otherSideX-1][otherSideY] == WALL:
        walls.append(Wall(otherSideX-1, otherSideY, WEST))
      if otherSideY > 1 and chosenWall.wallDir != 2 and map[otherSideX][otherSideY-1] == WALL:
        walls.append(Wall(otherSideX, otherSideY-1, NORTH))
      if otherSideX < size-2 and chosenWall.wallDir != 3 and map[otherSideX+1][otherSideY] == WALL:
        walls.append(Wall(otherSideX+1, otherSideY, EAST))
      if otherSideY < size-2 and chosenWall.wallDir != 0 and map[otherSideX][otherSideY+1] == WALL:
        walls.append(Wall(otherSideX, otherSideY+1, SOUTH))
        
    del walls[chosenIndex]
  
  #build list of dead-ends (3+ adjacent walls)
  deadEndList = []
  for x in range(1, size-1):
    for y in range(1, size-1):
      if map[x][y] == WALL:
        continue
        
      adjacentWallCount = 0
      
      if x > 0 and map[x-1][y] == WALL:
        adjacentWallCount += 1
      if y > 0 and map[x][y-1] == WALL:
        adjacentWallCount += 1
      if x < size-1 and map[x+1][y] == WALL:
        adjacentWallCount += 1
      if y < size-1 and map[x][y+1] == WALL:
        adjacentWallCount += 1
        
      if adjacentWallCount >= 3:
        deadEndList.append(Wall(x,y,0))
        
  for tile in deadEndList:
    if tile.x > 2 and getPathLength(map, tile.x, tile.y, tile.x-2, tile.y) >= size:
      map[tile.x-1][tile.y] = EMPTY
    if tile.y > 2 and getPathLength(map, tile.x, tile.y, tile.x, tile.y-2) >= size:
      map[tile.x][tile.y-1] = EMPTY
    if tile.x < size-3 and getPathLength(map, tile.x, tile.y, tile.x+2, tile.y) >= size:
      map[tile.x+1][tile.y] = EMPTY
    if tile.y < size-3 and getPathLength(map, tile.x, tile.y, tile.x, tile.y+2) >= size:
      map[tile.x][tile.y+1] = EMPTY
      
  map[0][size/2+1] = SPAWN
  map[size/2+1][size-1] = SPAWN
  map[size-1][size/2-1] = SPAWN
  map[size/2-1][0] = SPAWN
  
  return map