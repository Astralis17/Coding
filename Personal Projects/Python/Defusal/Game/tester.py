import aTools, utils, datetime, time
from aTools import *
from random import randint
def deltaTimeCalc(frame, frames):

        currentFrame = frames[frame]
        previousFrame = frames[(frame+1)%2]
        print(currentFrame/previousFrame)
        return 1

frame = 0
frameTimes = [datetime.datetime.now().timestamp(),0]
deltaTime = 1
timerMilSec = 40000
gametime = 0
delayClock =0

run = True
while run:
        frame += 1
        frame %= 2
        delayClock += 1
        delayClock %= 2

        frameTimes[frame] = datetime.datetime.now().timestamp()
        deltaTime = deltaTimeCalc(frame, frameTimes)
        timerMilSec -= 20 * deltaTime
        gametime += 20 * deltaTime
        time.sleep((0.1)*delayClock)