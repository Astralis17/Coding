import aTools, utils, datetime, time
from aTools import *
from unix import time as Time
from random import randint
import pygame
def deltaTimeCalc(frame, frames, delayTick = 10):

        currentFrame = frames[frame]
        previousFrame = frames[(frame+1)%2]
        print(currentFrame/previousFrame)
        return 1
timepoint = Time.time
pygame.init()

frame = 0
frameTimes = [timepoint()]
time.sleep(0.001)

frameTimes.append(timepoint())
print("1:",frameTimes[0])
print("2:",frameTimes[1])
print(frameTimes[1]-frameTimes[0])
deltaTime = 1
timerMilSec = 40000
gametime = 0
delayClock = 0


run = True
frameStart = timepoint()
while run:
        frameEnd = timepoint()
        frameDifference = abs(frameEnd - frameStart)
        print((0.02-frameDifference)*1000)
        pygame.time.delay(int((0.02-frameDifference)*1000))
        frameStart = timepoint()
        gametime += 20

