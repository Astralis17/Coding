from math import atan2, degrees, pi
import pygame

#Calculates the angle between the cursor and the player
def aiming(playerx, playery, mousex, mousey):

    dx = mousex - playerx
    dy = playery - mousey
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)
    degs += 90
    degs %= 360

    if   degs <  22.5  or  degs >= 337.5:
        target = 0
    elif degs <  67.5  and degs >= 22.5:
        target = 1
    elif degs <  112.5 and degs >= 67.5:
        target = 2
    elif degs <  157.5 and degs >= 112.5:
        target = 3
    elif degs <  202.5 and degs >= 157.5:
        target = 4
    elif degs <  247.5 and degs >= 202.5:
        target = 5
    elif degs <  292.5 and degs >= 247.5:
        target = 6
    elif degs <  337.5 and degs > 292.5:
        target = 7

    return degs, target

#Basic Player Movement
def player_movement(playerx, playery, keys,speed, moving, sprite):
    if keys[pygame.K_LEFT]:
        playerx -= speed
        moving = True
        sprite = 3

    if keys[pygame.K_RIGHT]:
        playerx += speed
        moving = True
        sprite = 1

    if keys[pygame.K_UP]:
        playery -= speed
        moving = True
        sprite = 0

    if keys[pygame.K_DOWN]:
        playery += speed
        moving = True
        sprite = 2
    return playerx, playery, moving, sprite,
#Dashing


def playerdash(playerx, playery, keys, speed, dashtick, dashcharge):
    if keys[pygame.K_RIGHT] and dashcharge != 0 and keys[pygame.K_LSHIFT]:
        playerx -= speed * 5
        dashtick = 140
        dashcharge -=1

    if keys[pygame.K_LEFT] and dashcharge != 0 and keys[pygame.K_LSHIFT]:
        playerx += speed * 5
        dashtick = 140
        dashcharge -=1

    if keys[pygame.K_UP] and dashcharge != 0 and keys[pygame.K_LSHIFT]:
        playery -= speed * 5
        dashtick = 140
        dashcharge -=1

    if keys[pygame.K_DOWN] and dashcharge != 0 and keys[pygame.K_LSHIFT]:
        playery += 10 * 5
        dashtick = 140
        dashcharge -=1

    if dashtick > 0 and dashcharge < 6:
        dashtick -= 1
    if dashtick == 0:
        dashcharge = 6
    return playerx, playery, dashtick, dashcharge

#Calculates which player sprite is being used based on the angle at which the cursor is at
def spritedirection(target):
    if target == 0:
        sprite = 0
    elif target == 1:
        sprite = 1
    elif target == 2:
        sprite = 1
    elif target == 3:
        sprite = 2
    elif target == 4:
        sprite = 2
    elif target == 5:
        sprite = 2
    elif target == 6:
        sprite = 3
    elif target == 7:
        sprite = 3
    else:
        sprite = 2
    return sprite

#Animation Controller
def AnimationTicker(AnimTick,AnimFrame,moving):

    if AnimTick >= 50:
        AnimTick = 0
        if AnimFrame >= 3:
            AnimFrame = 0
        else:
            AnimFrame += 1
    else:
        if moving == True:
            AnimTick += 1

    return AnimTick, AnimFrame

#Causes the Player to wrap around the edge of the screen when passing the boundries
def wrap(windowwidth, windowheight, playerx, playery):
    if playerx >= windowwidth + 10:
        playerx = -79
    if playerx <=  -80:
        playerx = windowwidth + 9
    if playery >= windowheight + 20:
        playery = -79
    if playery <=  -80:
        playery = windowheight + 9
    return playerx,playery

#Loads Animation frames and Idle frame for Upwards
playersprite1A = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite0A.png")
playersprite1B = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite0B.png")
playersprite1C = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite0C.png")
#Loads Animation frames and Idle frame for Rightwards
playersprite2A = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite1A.png")
playersprite2B = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite1B.png")
playersprite2C = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite1C.png")
#Loads Animation frames and Idle frame for Downwards
playersprite3A = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite2A.png")
playersprite3B = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite2B.png")
playersprite3C = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite2C.png")
#Loads Animation frames and Idle frame for Leftwards
playersprite4A = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite3A.png")
playersprite4B = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite3B.png")
playersprite4C = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\PlayerSprites\playersprite3C.png")

playerspritesheet1 = (playersprite1A, playersprite1B, playersprite1C, playersprite1B)
playerspritesheet2 = (playersprite2A, playersprite2B, playersprite2C, playersprite2B)
playerspritesheet3 = (playersprite3A, playersprite3B, playersprite3C, playersprite3B)
playerspritesheet4 = (playersprite4A, playersprite4B, playersprite4C, playersprite4B)
playerspritesheet = (playerspritesheet1, playerspritesheet2, playerspritesheet3, playerspritesheet4)

whoosh = pygame.image.load("Personal Projects\Aquilith, Whispers of The Aether\Sprites\Whoosh.png")
