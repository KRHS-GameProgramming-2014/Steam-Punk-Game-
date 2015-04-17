import pygame, math, sys, time, os
from Block import Block

class Level():
    def __init__(self, level, names, screenSize):
        self.screenSize = screenSize
        self.names = names
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.hardBlocks = []
        
        self.players = []
        
        self.blockSize = 50
        self.level = level
        self.load(level)

    def killOldLevels(self, timeInSeconds):
        for f in os.listdir("RS/Maps/"):
            if f[-5:] == ".tngs":
                print f, time.time() - os.path.getmtime("RS/Maps/"+f), timeInSeconds
                if (time.time() - os.path.getmtime("RS/Maps/"+f)) > timeInSeconds:
                    print f
                    os.remove("RS/Maps/"+f)
            
    def unload(self):
        things = []
        line = []
        for y in range(14):
            for x in range(20):
                line += [" "]
            things += [line]
            line = []
        #print len(things), len(things[0])
        
        for ghost in self.ghosts:
            things[ghost.rect.center[1]/50][ghost.rect.center[0]/50] = "G"

        thingString = ""
        for line in things:
            for c in line:
                thingString += c
            thingString += "\n"
        #print thingString
        
        thingMap="RS/Maps/"+ self.level +".tngs"
        savedThingfile = open(thingMap, "w")
        savedThingfile.write(thingString)
        savedThingfile.close()
            
        while len(self.blocks) > 0:
            self.blocks.remove(self.blocks[0])

    def load(self, level, source=None):  
        if source != None:
            self.unload()    
        self.killOldLevels(30)
        self.level = level
        print self.level
        geoMap="RS/Maps/"+ level +".lvl"
        thingMap="RS/Maps/"+ level +".tng"
        savedThingMap="RS/Maps/"+ level +".tngs"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        
        if source != None:
            if source.upper() != "O":
                if source.upper() == "N":
                    plpos = [self.players[0].rect.center[0], self.screenHeight-75]
        

        #Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    world = int(self.level[6])
                    self.hardBlocks += [Block((self.blockSize,self.blockSize) ,"RS/Block/block.png", 
                                    "RS/Block/block.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    )]


        #----Done with file---
        try:
            thingfile = open(savedThingMap, "r")
        except (OSError, IOError) as e:
            thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close()

        newlines = []

        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]

        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
#-------Blocks  
                if c == "@":
                    if len(self.players) == 0:
                        if len(self.names) > 0:
                            daName = self.names.pop()
                            self.players += [Player(daName,  [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                
                if c == "N":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])
                    levy = int(self.level[8])-1
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RS/Block/block.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize, self.blockSize),
                                                                newlev, c)]

                if c == "G":
                    self.ghosts += [Ghost(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "D":
                    self.demons += [Demon(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
