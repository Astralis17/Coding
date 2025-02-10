from GV import *; from time import sleep
import functions as f, classes as c
import pygame, random

pygame.init()
window = pygame.display.set_mode(windowDim)

selectedOBJ = 0

objList = []


def CreateOBJ(x):
    velocity1 = random.randint(5, 10)
    if random.random() > 0.5:
            velocity1 *= -1
    velocity2 = random.randint(5, 10)
    if random.random() > 0.5:
            velocity2 *= -1
    obj = c.obj1(10, random.randint(5, 5), [velocity1,velocity2], [random.random()*windowDim[0],random.random()*windowDim[1]], x)
    return obj

for x in range(0, 15):
    objList.append(CreateOBJ(len(objList)))


run = True
while run:
        window.fill((0, 0, 0))
        sleep(0.01)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                objList[selectedOBJ].displayColour = objList[selectedOBJ].colour
                                selectedOBJ = (selectedOBJ + 1) % len(objList)
                        elif event.key == pygame.K_LEFT:
                                objList[selectedOBJ].displayColour = objList[selectedOBJ].colour
                                selectedOBJ = (selectedOBJ - 1) % len(objList)
                        elif event.key == pygame.K_KP_PLUS:
                                objList.append(CreateOBJ(len(objList)))

                        elif event.key == pygame.K_MINUS:
                                objList.pop()
                                selectedOBJ = (selectedOBJ) % len(objList)

        print(len(objList), ":", selectedOBJ)
        objList[selectedOBJ].displayColour = (255,10,10)







        for obj in objList:
                obj.moveFrame()
                collide = f.collsions(obj, objList)
                if collide:
                        break

        for obj in objList:
                pygame.draw.circle(window, obj.displayColour, obj.position, obj.size)
        pygame.display.flip()

