from random import choice, randint

def glide(x,y, timer, destination=(0,0)):
        difX = destination[0] - x
        difY = destination[1] - y

        x += difX/timer
        y += difY/timer

        return x,y

def findPoint(x,y, minDistance, maxDistance, workspace, direction=(0,0)):
        option = False
        if option:
                if direction[0] != 0:
                        dir = direction[0]
                else:
                        dir = choice([-1,1])
                if minDistance*dir > maxDistance*dir:
                        temp = maxDistance
                        maxDistance = minDistance
                        minDistance = temp
                destinationX = randint((x+minDistance*dir), (x+maxDistance*dir))

                if direction[0] != 0:
                        dir = direction[0]
                else:
                        dir = choice([-1,1])
                if minDistance*dir > maxDistance*dir:
                        temp = maxDistance
                        maxDistance = minDistance
                        minDistance = temp
                destinationY = randint((y+minDistance*dir), (y+maxDistance*dir))
        else:
                destinationX = randint(0, workspace[0])
                destinationY = randint(0, workspace[1])
        destination = tuple((destinationX, destinationY))
        return destination


#d = findPoint(600, 500, 20, 100)