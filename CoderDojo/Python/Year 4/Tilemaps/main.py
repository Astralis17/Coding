# Example file showing a basic pygame "game loop"
import pygame
from tilemap import *

# pygame setup
pygame.init()

myFirstRoom =[
            [WALL,  WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  WALL,   WALL,   WALL,   FLOOR,   WALL,   WALL,   WALL,   WALL],
        ]

mySecondRoom =[
            [WALL,  WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  WALL_TWO,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  WALL_TWO,  WALL_TWO,  WALL_TWO,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  WALL_TWO,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  WALL,   WALL,   WALL,   FLOOR,   WALL,   WALL,   WALL,   WALL],
        ]

screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
FirstRoom = room(pygame.math.Vector2(100,100), myFirstRoom)
SecondRoom = room(pygame.math.Vector2(400,400), mySecondRoom)



# Initializing RGB GB Color
BGColor = (0, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Changing BG color
    screen.fill(BGColor)

    # RENDER YOUR GAME HERE
    FirstRoom.drawRoom(screen)
    SecondRoom.drawRoom(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()