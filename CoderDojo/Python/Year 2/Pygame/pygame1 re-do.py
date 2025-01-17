import pygame

pygame.init()
pygame.font.init()

#Screen Width, Height and Caption
windowwidth = 1365
windowheight = 688
window = pygame.display.set_mode((windowwidth, windowheight),pygame.RESIZABLE)
pygame.display.set_caption("square go brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")

#Player height, width and position
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

#Colors
blue = 45, 86, 153
red = 249, 35, 35
green = 35, 249 , 86
purple = 153, 20, 153
white = 255, 255, 255
black = 0, 0, 0

#Bullet Variables
bulletW = 10
bulletH = 10
bulletx =  9000
bullety = 9000
bulletxspeed = 0
bulletyspeed = 0
bulletspeed = 4


#Text Display
SysFont = pygame.font.get_default_font()
font1 = pygame.font.SysFont('Comic Sans MS', 30, False, False)
font2 = pygame.font.SysFont('Comic Sans MS', 25, False, False)


#Main Game Loop
run = True
while run:

    #Background colour and Game Speed
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

    #Sprint
    if keys[pygame.K_LCTRL]:
        speed =speedbeforesprint * sprint
    else:
        speed = speedbeforesprint

#All dash movement and logic
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

    #Speed Counter
    if dashtick != 0:
        if speed == speedbeforesprint:
            spd = font2.render("Speed: {} ".format(dash) , True, white)
        else:
            spd = font2.render("Speed: {} ".format(dash*2) , True, white)
    else:
        spd = font2.render("Speed: {} ".format(speed) , True, white)

    #Check if dash is active
    if keys[pygame.K_LSHIFT]:
        dashcheck = True
    if not keys[pygame.K_LSHIFT]:
        dashcheck = False
    #Dash movement
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

    #Dash Cooldown Indicator
    if dashcool == 0:
        dashcolor = green
    elif dashcool != 0:
        dashcolor = red
    if dashcool == 0:
        dashcoolsec = ""
    if dashcool == 10:
        dashcoolsec = "0"
    if dashcool == 159:
        dashcoolsec = "1"
    if dashcool == 319:
        dashcoolsec = "2"
    if dashcool == 449:
        dashcoolsec = "3"
    if dashcool == 539:
        dashcoolsec = "4"
    if dashcool == 749:
        dashcoolsec = "5"
    if dashcool == 909:
        dashcoolsec = "6"
    if dashcool == 1069:
        dashcoolsec = "7"
    if dashcool == 1229:
        dashcoolsec = "8"
    #Actual text countdown
    dashcooldown = font1.render(dashcoolsec, True, black)
    if dashcool != 0 :
        dashcool = dashcool - 1


#WrapAround

    #Right to Left
    if playerx >= windowwidth + 1:
        playerx = -playerwidth
    #Left to Right
    if playerx <= -playerwidth-1:
        playerx = windowwidth
    #Top to Bottom
    if playery >= windowheight-49:
        playery = -playerheight
    #Top to Bottom
    if playery <= -playerheight-1:
        playery = windowheight-50

#All Game Object Drawing
    pygame.draw.rect(window, (green), (bulletx , bullety, bulletW, bulletH))#Bullet

    #Player
    if dashtick != 0:
        pygame.draw.rect(window, (purple), (playerx, playery, playerwidth, playerheight))#Player during dash
    else:
        pygame.draw.rect(window, (red), (playerx, playery, playerwidth, playerheight))#Player not during dash

    #Info Bar
    pygame.draw.rect(window, (black), (0, windowheight - 50, 1370, 50))#Info Bar
    pygame.draw.rect(window, (dashcolor), (windowwidth - 125, windowheight- 44, 100, 30))#Dash Counter Color
    window.blit(dashcooldown, (windowwidth - 85, windowheight - 52))#Dash counter number
    window.blit(spd, (windowwidth - 285, windowheight - 55))#Speed Counter

    pygame.display.update()
    windowwidth, windowheight = pygame.display.get_surface().get_size()

pygame.quit