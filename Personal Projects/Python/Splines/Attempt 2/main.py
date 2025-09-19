import pygame, math
from classes import *
from unix import time as Time
timepoint = Time.time
pygame.init()
display = pygame.display.set_mode((1300, 700))

p1 = point((300, 620))
p2 = point((300, 100))
p3 = point((1000, 100))
p4 = point((1000, 620))
points = [p1, p2, p3, p4]

c1 = BezierCurve(points, display)

run = True

# while run:
frameStart = timepoint()
gameStart = frameStart
while run:
        frameEnd = timepoint()
        frameDifference = abs(frameEnd - frameStart)
        pygame.time.delay(int((0.011-frameDifference)*1000))
        frameStart = timepoint()

        display.fill("black")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                run = False

        c1.t = (c1.t + 0.005) % 1
        c1.findSubPoints()
        c1.draw()
        # print(len(c1.points))

        pygame.display.update()