import random as r
import math

class Map:
  def __init__(self, width, height, min_size = 10, max_size = 40, generate = True):

    if(min_size>max_size):
      raise OverflowError("Map minimum size cannot be greater than maximum size")

    self.width = width
    self.height = height
    self.rooms = []
    self.min_size = min_size
    self.min_room_width = math.ceil(math.sqrt(min_size))
    self.min_room_height = math.ceil(math.sqrt(min_size))
    self.max_size = max_size
    self.max_room_width = math.ceil(math.sqrt(max_size))
    self.max_room_height = math.ceil(math.sqrt(max_size))
    self.room_map_str = ""
    self.wall_map = []

    if(generate):
      self.generate(Point(0,0),Point(self.width,0),Point(0,self.height),Point(self.width,self.height))

    self.generate_wall_map();
    self.generate_room_map_str();

  '''
  Creates an array of characters that define the walls of the map
  '''
  def generate_wall_map(self):

    #Create a blank width x height array 
    y=0
    while(y<=self.height):
      x=0;
      arry = []
      while(x<=self.width):
        arry.append(".")
        x+=1
      self.wall_map.append(arry)
      y+=1
    #print(len(self.wall_map))

    for room in self.rooms:
      p1x = room.p1.x
      p2x = room.p2.x
      p3x = room.p3.x
      p4x = room.p4.x

      p1y = room.p1.y
      p2y = room.p2.y
      p3y = room.p3.y
      p4y = room.p4.y

      #print(str(room));

      #draw upper wall
      i=p1x 
      while(i<=p2x):
        self.wall_map[i][p1y]="#"
        i+=1

      #draw bottom wall
      i=p3x
      while(i<=p4x):
        self.wall_map[i][p3y]="#"
        i+=1

      #draw right wall
      i=p1y
      while(i<=p3y):
        self.wall_map[p1x][i]="#"
        i+=1

      #draw right wall
      i=p2y
      while(i<=p4y):
        self.wall_map[p2x][i]="#"
        i+=1

  '''
  Creates a string of characters that can be displayed using the print command
  '''
  def generate_room_map_str(self):
    string = ""
    y=0
    while(y<self.height+1):
      x=0;
      while(x<self.width+1):
        string+=" "
        string+=self.wall_map[x][y]

        x+=1
      string+="\n"
      y+=1
    self.room_map_str = string
    return string
    
  '''
  Recursively creates a set of rooms defined by the min and max parameters
  defined in the Map object
  '''
  def generate(self,p1,p2,p3,p4):
    room = Room(p1,p2,p3,p4)
    if(room.width<=self.min_room_width):
      vertical = 0
    elif(room.height<=self.min_room_height):
      vertical = 1
    else:
      vertical = r.randint(0,1)

    if(room.size<=self.max_size):
      self.rooms.append(room)
      return
  
    if(vertical):
      if(p1.x+self.min_room_width<p2.x-self.min_room_width):
        rand = r.randint(p1.x+self.min_room_width,p2.x-self.min_room_width)
        v1 = Point(rand,p1.y)
        v2 = Point(rand,p3.y)
        self.generate(p1,v1,p3,v2)
        self.generate(v1,p2,v2,p4)
      else:
        self.rooms.append(room)
    else:
      if(p1.y+self.min_room_height<p3.y-self.min_room_height):
        rand = r.randint(p1.y+self.min_room_height,p3.y-self.min_room_height)
        h1 = Point(p1.x,rand)
        h2 = Point(p2.x,rand)
        self.generate(p1,p2,h1,h2)
        self.generate(h1,h2,p3,p4)
      else:
        self.rooms.append(room)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return"("+str(self.x)+", "+str(self.y)+")"

class Room:
  def __init__(self,p1,p2,p3,p4):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
    self.p4 = p4
    self.width = p2.x-p1.x
    self.height = p3.y-p1.y
    self.size = self.width*self.height

  def self_string(self):
    string = ""
    y=0
    while(y<self.height):
      x=0;
      while(x<self.width):
        #Print Top Wall
        if(x==0 or x==self.width-1 or y==0 or y==self.height-1):
          string+="#"
        else:
          string+=" "
        x+=1
      string+="\n"
      y+=1
    return string
    
  def __str__(self):
    return str(self.p1)+" "+str(self.p2)+" "+str(self.p3)+" "+str(self.p4)

from os import system, name

while(True):

  map = Map(30, 30, 40, 50)

  print(map.room_map_str)

  input("Press enter to generate a new room\n")
  system('clear')
