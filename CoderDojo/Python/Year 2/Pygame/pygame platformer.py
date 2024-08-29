import pygame

pygame.init()

windowwidth = 1000
windowheight = 588
window = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("square go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")

#Colors
blue = 45, 86, 153
red = 249, 35, 35
green = 35, 249 , 86
purple = 153, 20, 153
white = 255, 255, 255
black = 0, 0, 0

#Player info
playerwidth = 25
playerheight = 25
playerx = windowwidth/2 - playerwidth/2
playery = windowheight/2 - playerheight/2

#Speed Variables
speed = 1
sprint = 2
speedbeforesprint = 1
speedbuff = 1.00

#Dash Variables
dash = 3
dashcool = 0
dashcheck = True
dashtick = 0
dashtickright = 0
dashtickleft = 0
dashtickup = 0
dashtickdown = 0
dashcolor = 0, 0, 0
dashcoolsec = ""


run = True
while run:
    pygame.time.delay(5)
    window.fill(blue)

    #Quit Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


#General player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playery = playery - speed
    if keys[pygame.K_s]:
        playery = playery + speed
    if keys[pygame.K_d]:
        playerx = playerx + speed
    if keys[pygame.K_a]:
        playerx = playerx - speed




    pygame.draw.rect(window, (red), (playerx, playery, playerwidth, playerheight))#Player drawing
    pygame.draw.rect(window, (black), (playerx + 2, playery + 10, 5, 5))
    pygame.draw.rect(window, (black), (playerx + 18, playery + 10, 5, 5))
    pygame.display.update()
pygame.quit()