import numpy as np
import random
import csv
import webbrowser

cleanup = 1
y_in = 25 #Height of the Map
x_in = y_in*4 #Width of the Map
terrain_list = ["Water", "Land"]
I = True

#Symbole List
water_sym = "~"
land_sym = "#"

class Map():
    def __init__(self):
        self.age = ""   #Which age the world is in; List of Ages: Age of Myth, Age of Legend, Age of Heros, etc
        self.Map_rows = []
        self.Map3 = ""
        self.Map2 = ""
        self.Map = []
        self.map_gen()
    def map_gen(self):
        global I
        global Tile
        for y in range(y_in):
            Row = Map_row()
            Row.pos_y = y
            for x in range(x_in):
                
                New_Tile = Tile()
                New_Tile.pos_y = y
                New_Tile.pos_x = x
                New_Tile.highed = random.randint(0, 10)
                #New_Tile.terrain = random.choice(terrain_list)
                if New_Tile.highed >= 5:
                    New_Tile.terrain = "Land"
                    New_Tile.symbole = land_sym
                else:
                    New_Tile.terrain = "Water"
                    New_Tile.symbole = water_sym
                Row.Tiles.append(New_Tile)
            self.Map_rows.append(Row)
        #At more detail to the map
        while I == True:
            for y in range(y_in):
                Row = self.Map_rows[y]
                for x in range(x_in):
                    Tile = Row.Tiles[x]
                    #Fills in small water gaps, but not all of them
                    for c in range(cleanup):
                        #Removes small inland lakes and cleans up the coast
                        if Tile.terrain == "Water":
                            Landbors = 0
                            for i in range(1):
                                if Tile.pos_x == x_in-1 or Tile.pos_x == 0:
                                    if Tile.pos_x == x_in-1:
                                        NeighborL = Row.Tiles[x-1] #Left
                                        if NeighborL.terrain == "Land":
                                            Landbors = Landbors+1
                                    else:
                                        NeighborR = Row.Tiles[x+1] #Right
                                        if NeighborR.terrain == "Land":
                                            Landbors = Landbors+1
                                else:
                                    NeighborL = Row.Tiles[x-1] #Left
                                    if NeighborL.terrain == "Land":
                                        Landbors = Landbors+1
                                    NeighborR = Row.Tiles[x+1] #Right
                                    if NeighborR.terrain == "Land":
                                        Landbors = Landbors+1
                            for i in range(1):
                                if Tile.pos_y == 0 or Tile.pos_y == y_in-1: #Checks above and below
                                    if Tile.pos_y == 0:
                                        RowN = self.Map_rows[y+1]
                                        NeighborU = RowN.Tiles[x]
                                        if NeighborU.terrain == "Land":
                                            Landbors = Landbors+1
                                    else:
                                        RowN = self.Map_rows[y-1]
                                        NeighborD = RowN.Tiles[x]
                                        if NeighborU.terrain == "Land":
                                            Landbors = Landbors+1
                                else:
                                    RowN = self.Map_rows[y-1]
                                    NeighborD = RowN.Tiles[x]
                                    if NeighborU.terrain == "Land":
                                            Landbors = Landbors+1
                                    RowN = self.Map_rows[y+1]
                                    NeighborU = RowN.Tiles[x]
                                    if NeighborU.terrain == "Land":
                                            Landbors = Landbors+1
                            if 3 <= Landbors:
                                Tile.terrain = "Land"
                                Tile.symbole = land_sym
                    for c in range(cleanup):
                        #Removes some land tiles
                        if Tile.terrain == "Land":
                            Landbors = 0
                            for i in range(1):
                                if Tile.pos_x == x_in-1 or Tile.pos_x == 0:
                                    if Tile.pos_x == x_in-1:
                                        NeighborL = Row.Tiles[x-1] #Left
                                        if NeighborL.terrain == "Water":
                                            Landbors = Landbors+1
                                    else:
                                        NeighborR = Row.Tiles[x+1] #Right
                                        if NeighborR.terrain == "Water":
                                            Landbors = Landbors+1
                                else:
                                    NeighborL = Row.Tiles[x-1] #Left
                                    if NeighborL.terrain == "Water":
                                        Landbors = Landbors+1
                                    NeighborR = Row.Tiles[x+1] #Right
                                    if NeighborR.terrain == "Water":
                                        Landbors = Landbors+1
                            for i in range(1):
                                if Tile.pos_y == 0 or Tile.pos_y == y_in-1: #Checks above and below
                                    if Tile.pos_y == 0:
                                        RowN = self.Map_rows[y+1]
                                        NeighborU = RowN.Tiles[x]
                                        if NeighborU.terrain == "Water":
                                            Landbors = Landbors+1
                                    else:
                                        RowN = self.Map_rows[y-1]
                                        NeighborD = RowN.Tiles[x]
                                        if NeighborU.terrain == "Water":
                                            Landbors = Landbors+1
                                else:
                                    RowN = self.Map_rows[y-1]
                                    NeighborD = RowN.Tiles[x]
                                    if NeighborU.terrain == "Water":
                                            Landbors = Landbors+1
                                    RowN = self.Map_rows[y+1]
                                    NeighborU = RowN.Tiles[x]
                                    if NeighborU.terrain == "Water":
                                            Landbors = Landbors+1
                            if 3 <= Landbors:
                                Tile.terrain = "Water"
                                Tile.symbole = water_sym
            I = False
    def print_map(self):
        #Print Map
        self.Map2 = "" #Clears String
        for i in range(len(self.Map_rows)):
            Read = self.Map_rows[i]
            self.Map2 = self.Map2+"|"
            for j in range(len(Read.Tiles)):
                Tile = Read.Tiles[j]
                self.Map2 = self.Map2+str(Tile.symbole)
                #Map2 = Map2+"("+str(Tile.pos_y)+"|"+str(Tile.pos_x)+")"
            self.Map2 = self.Map2+"|"+"\n"
        print(self.Map2)
class Map_row():
    def __init__(self):
        self.pos_y = ""
        self.Tiles = []

class Tile():
    def __init__(self):
        self.pos_y = ""
        self.pos_x = ""
        self.highed = ""
        self.terrain = ""
        self.biom = ""
        self.symbole = ""
#Generate Map
#Map = Map() #Create the map object
