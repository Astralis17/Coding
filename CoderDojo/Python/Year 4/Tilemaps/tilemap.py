import pygame as pg

FLOOR = 0
WALL = 1
WALL_TWO = 2


class room:

    
    def __init__(self, position, myTileMap):
        
        self.tileMap = myTileMap

        self.textures = {
                            FLOOR    :   pg.image.load("CoderDojo/Python/Year 4/Tilemaps/images/floor.png"),
                            WALL     :   pg.image.load("CoderDojo/Python/Year 4/Tilemaps/images/wall.png"),
                            WALL_TWO :  pg.image.load("CoderDojo/Python/Year 4/Tilemaps/images/wall_two.png"),

                        }

        self.mapWidth = len(self.tileMap)     
        self.mapHeight = len(self.tileMap[0]) 
        self.tileSize = 16
        self.pos = position


    def drawRoom(self, window):
        for row in range(self.mapWidth):
            for column in range(self.mapHeight):
                window.blit (
                            self.textures[self.tileMap[row][column]], 
                            (self.pos.x + (column * self.tileSize), self.pos.y + (row * self.tileSize))
                            )