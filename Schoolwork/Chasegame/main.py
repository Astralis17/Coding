from time import sleep
import pygame, random
from functions import *

pygame.init()
windowwidth = 1000
windowheight = 588
global windowDim
windowDim = (windowwidth, windowheight)
window = pygame.display.set_mode((windowwidth, windowheight))

class enemy:
        def __init__(self, speed, x=0, y=0, tRange=(), minDistance=200, maxDistance=250, destination=(windowDim[0]/2,windowDim[1]/2)):
                self.x = x
                self.y = y
                self.speed = speed
                self.tRange = tRange
                self.timer = random.randint(tRange[0],tRange[1])
                self.TravTime = self.timer
                self.minDistance = minDistance
                self.maxDistance = maxDistance
                self.destination = destination

        def wander(self, workspace):
                if tuple((self.x, self.y)) == self.destination:
                        self.destination = findPoint(self.x, self.y, self.minDistance, self.maxDistance, workspace)
                        self.TravTime = random.randint(self.tRange[0],self.tRange[1])
                else:
                        if self.TravTime <= 0:
                                self.TravTime += 1
                        self.x, self.y = glide(self.x, self.y, self.TravTime, self.destination)
                        self.TravTime -= 1

#                if self.destination[0] > workspace[0]-50:
#                        self.destination = (self.destination[0]-50, self.destination[1])
#                        self.TravTime -= 1
#                elif self.destination[0] < 50:
#                        self.destination = (self.destination[0]+50, self.destination[1])
#                        self.TravTime -= 1
#                if self.destination[1] > workspace[1]-50:
#                        self.destination = (self.destination[0], self.destination[1]-50)
#                        self.TravTime -= 1
#                elif self.destination[1] < 50:
#                        self.destination = (self.destination[0], self.destination[1]+50)
#                        self.TravTime -= 1
                if self.TravTime <= 0:
                        self.TravTime = 1

class player:

        def __init__(self, x=windowwidth/2, y=windowheight/2, speed = 5):
                self.x = x
                self.y = y
                self.speed = speed
        def move(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        MainPlayer.y = MainPlayer.y - MainPlayer.speed
                if keys[pygame.K_s]:
                        MainPlayer.y = MainPlayer.y + MainPlayer.speed
                if keys[pygame.K_d]:
                        MainPlayer.x = MainPlayer.x + MainPlayer.speed
                if keys[pygame.K_a]:
                        MainPlayer.x = MainPlayer.x - MainPlayer.speed

MainPlayer = player()
count = 100000
enemies = []
while count > 0:
        e = enemy(10, tRange=(3,4), minDistance=200, maxDistance=1000, destination=(windowwidth*0.5,windowheight*0.5))
        count -= 1
        enemies.append(e)


run = True
while run:
        window.fill((0,0,0))
        sleep(0.01)
        for enemy in enemies:
                enemy.wander(windowDim)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        MainPlayer.move()


        pygame.draw.rect(window, (155,55,225), (MainPlayer.x, MainPlayer.y, 15,15))
        for e in enemies:
                pygame.draw.circle(window, (255,255,255), (e.x, e.y), 3)
        pygame.display.flip()