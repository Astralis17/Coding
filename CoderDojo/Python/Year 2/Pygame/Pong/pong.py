import pygame


#Initialisation
pygame.init()

#Screen
windowwidth = 1365
windowheight = 688
window = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Pong")

#Clock
clock = pygame.time.Clock()

#Ball Stuff
ballwidth = 30
ballheight = 30
ballxspeed = 8
ballyspeed = 8
ballhit = False
ball = pygame.Rect(windowwidth/2 - ballwidth/2, windowheight/2 - ballwidth/2, ballwidth, ballwidth)
player = pygame.Rect(10, windowheight/2 - 70, 10 , 140)
enemy = pygame.Rect(windowwidth - 20, windowheight/2 - 70, 10 , 140)

playerscore = 0
enemyscore = 0
#Colours
BackgroundColor = pygame.Color('grey12')
White = (255, 255, 255)
Black = (0, 0, 0)
Blue =  ()
Grey = (200, 200, 200)

#Ball Movement Function
def BallMove():
    global ballxspeed, ballyspeed, ballhit
    #Ball Movement
    ball.x = ball.x + ballxspeed
    ball.y = ball.y + ballyspeed

    #Ball Colision
    if ball.top <= 0 or ball.bottom >= windowheight:
        ballyspeed *= -1
        ballhit = True
#    if ball.left <= 0 or ball.right >= windowwidth:
#        ballxspeed *= -1
    if ball.colliderect(player) or ball.colliderect(enemy):
        ballxspeed *= -1
        ballhit = True
        
#Player Movement Function
def PlayerMove():
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.top > 5:
        player.y -= 5
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.bottom < windowheight - 5:
        player.y += 5

#Enemy Movement Function
def EnemyMove():

    if ball.top < enemy.top:
        enemy.top -= 7
    if ball.bottom > enemy.bottom:
        enemy.bottom += 7

def BallScoring(playerscore, enemyscore):
    global windowwidth, windowheight, ball
    if ball.y <= windowwidth :
        playerscore += 1
        ball.x = windowwidth/2 - ballwidth/2
        ball.y = windowheight/2 - ballwidth/2
    if ball.left <= 0:
        enemyscore += 1
        ball = pygame.Rect(windowwidth/2 - ballwidth/2, windowheight/2 - ballwidth/2, ballwidth, ballwidth)
run = True
while  run:
    
    window.fill(BackgroundColor)
    clock.tick(60)
    #Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Player, Ball and Enemy Movement
    PlayerMove()
    BallMove()
    EnemyMove()

    BallScoring(playerscore,enemyscore)
    #Drawing
    pygame.draw.rect(window, Grey, player)
    pygame.draw.rect(window, Grey, enemy)
    pygame.draw.ellipse(window, Grey, ball)
    pygame.draw.aaline(window, Grey, (windowwidth/2, 0), (windowwidth/2, windowheight))


    pygame.display.flip()

    if ballhit == False:
        ballxspeed = 8
        ballyspeed = 8
    print(ballxspeed)
pygame.quit