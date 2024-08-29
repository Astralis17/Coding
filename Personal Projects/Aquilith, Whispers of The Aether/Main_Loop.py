import pygame
import colours, Player_Stuff, Tiles

pygame.init()

windowwidth = 1150
windowheight = 600
window = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Aquilith: Whispers Of The Aether")
window.fill(colours.purple)

#player
playerx = windowwidth/2
playery = windowheight/2
mousedegrees = 0
mousex, mousey = windowwidth/2, windowheight/2
speed = 3
global keys
sprite = 0
moving = False
run = True
AnimTick = 0
AnimFrame = 0
dashtick = 0
dashcharge = 5
whoosh = 0, 0
while run:
    pygame.time.delay(5)
    mousex, mousey = pygame.mouse.get_pos()
    window.fill(colours.blue)
    keys = pygame.key.get_pressed()

    #Quit Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    moving = False
    target, target = Player_Stuff.aiming(playerx, playery, mousex, mousey)

    playerx, playery, moving, sprite = Player_Stuff.player_movement(playerx, playery, keys, speed, moving, sprite)
    playerx, playery, dashtick, dashcharge = Player_Stuff.playerdash(playerx, playery, keys, speed, dashtick, dashcharge)
    
    AnimTick, AnimFrame = Player_Stuff.AnimationTicker(AnimTick, AnimFrame, moving)

    #Wrapping
    playerx, playery = Player_Stuff.wrap(windowwidth, windowheight, playerx, playery)

    if keys[pygame.K_SPACE]:
        pygame.draw.line(window, colours.purple,(mousex, mousey),(playerx, playery), 3)
        
    if moving == False:
        window.blit(Player_Stuff.playerspritesheet[sprite][1], (playerx -32, playery -32))
    else:
        window.blit(Player_Stuff.playerspritesheet[sprite][AnimFrame], (playerx -32, playery -32))
    print(AnimTick)
    pygame.display.update()

pygame.quit()