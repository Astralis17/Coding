import pygame

pygame.init()
pygame.font.init()
font2 = pygame.font.SysFont('Comic Sans MS', 25, False, False)
windowwidth = 1365
windowheight = 688
window = pygame.display.set_mode((windowwidth, windowheight),pygame.RESIZABLE)
pygame.display.set_caption("square go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")

#Colors
blue = 45, 86, 153
red = 249, 35, 35
black = 0, 0, 0

#Speed Variables
global speed
speed = 1


#Dash Variables
dash = 3
dashcool = 0
global dashcheck
dashcheck = True
global dashtick
dashtick = 0
dashcoolsec = ""

#Player info
playerwidth = 25
playerheight = 25
playerx = windowwidth/2 - playerwidth/2
playery = windowheight/2 - playerheight/2


def dashcontrol(speed, playerx, playery, dash, dashcool, dashtick):
    
    dashtickright = 0
    dashtickleft = 0
    dashtickup = 0
    dashtickdown = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        dashcheck = True
    if not keys[pygame.K_LSHIFT]:
        dashcheck = False

    if keys[pygame.K_w] and dashcheck == True and dashcool == 0:
        dashtickup = 40* speed
        dashtick = 40* speed
        dashcool = 449
        if speed >= 2:
            dashcool =750
    if keys[pygame.K_s] and dashcheck == True and dashcool == 0:
        dashtickdown = 40* speed
        dashtick = 40* speed
        dashcool = 449
        if speed >= 2:
            dashcool =750
    if keys[pygame.K_a] and dashcheck == True and dashcool == 0:
        dashtickleft = 40* speed
        dashtick = 40* speed
        dashcool = 449
        if speed >= 2:
            dashcool =750
    if keys[pygame.K_d] and dashcheck == True and dashcool == 0:
        dashtickright = 40* speed
        dashtick = 40* speed
        dashcool = 449
        if speed >= 2:
            dashcool =750

    if dashtickright != 0:
        playerx = playerx + dash
        dashtickright -= 1
        dashtick -= 1
    if dashtickleft != 0:
        playerx = playerx - dash
        dashtickleft -= 1
        dashtick -= 1
    if dashtickup != 0:
        playery = playery - dash
        dashtickup -= 1
        dashtick -= 1
    if dashtickdown != 0:
        playery = playery + dash
        dashtickdown -= 1
        dashtick -= 1
    if dashcool != 0:
        dashcool -= 1
    print(dashcool)
    return dashtick, dashcool, dashtickup, dashtickdown, dashtickright, dashtickleft

def handlebasemovement(speed, playerx, playery):


    sprint = 2
    speedbeforesprint = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playery = playery - speed
    if keys[pygame.K_s]:
        playery = playery + speed
    if keys[pygame.K_d]:
        playerx = playerx + speed
    if keys[pygame.K_a]:
        playerx = playerx - speed

    #Sprint
    if keys[pygame.K_LCTRL]:
        speed =speedbeforesprint * sprint
    if not keys[pygame.K_LCTRL]:
        speed = speedbeforesprint
    return speed, playerx, playery

#Main Game Loop
run = True
while run:

    #Background colour and Game Speed
    pygame.time.delay(0)
    window.fill(blue)

    #Quit Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Input
    speed, playerx, playery = handlebasemovement(speed, playerx, playery)
    dashtick, dashcool, dashtickup, dashtickdown, dashtickright, dashtickleft = dashcontrol(speed, playerx, playery, dash, dashcool, dashtick)

#WrapAround 

    #Right to Left
    if playerx >= windowwidth + 1:
        playerx = -playerwidth
    #Left to Right
    if playerx <= -playerwidth - 1:
        playerx = windowwidth
    #Top to Bottom
    if playery >= windowheight + 1:
        playery = -playerheight
    #Top to Bottom
    if playery <= -playerheight-1:
        playery = windowheight


    pygame.draw.rect(window, (red), (playerx, playery, playerwidth, playerheight))#Player drawing
    pygame.draw.rect(window, (black), (playerx + 2, playery + 10, 5, 5))
    pygame.draw.rect(window, (black), (playerx + 18, playery + 10, 5, 5))


    spd = font2.render("Speed: {} ".format(speed) , True, black)
    window.blit(spd, (windowwidth - 285, windowheight - 55))#Speed Counter

    pygame.display.update()
    windowwidth, windowheight = pygame.display.get_surface().get_size()
    
pygame.quit()