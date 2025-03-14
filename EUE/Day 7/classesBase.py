import pygame, random
windowDim = (1920, 1080)
gravity = -1

class Player:
    def __init__(self, x, y, isJumping=False, isGrounded=False, jumpHeight=5, speed=0.5, direction = 1):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.yVelocity = 0
        self.isJumping = isJumping
        self.isGrounded = isGrounded
        self.jumpHeight = jumpHeight
        self.moveSpeed = speed
        self.direction = direction

    def movement(self):
        self.y += self.yVelocity
        if self.isJumping and self.isGrounded:
            self.yVelocity += self.jumpHeight

        if self.y <= 0:
            self.isGrounded = True
            self.y = 0
            self.yVelocity *= -0.6
        else:
            self.isGrounded = False
            self.yVelocity += gravity
        if self.y > windowDim[1]:
            self.y = windowDim[1]
            self.yVelocity *= -1


        self.x += self.xVelocity
        self.xVelocity *= 0.95
        if abs(self.xVelocity) < 0.1:
            self.xVelocity = 0

    def move(self):
        self.xVelocity += self.moveSpeed * self.direction

    def draw(self, surface):
        pygame.draw.circle(surface, (20, 20, 20), (self.x, windowDim[1] - self.y), 10)

    def AutoBounce(self):
        if self.moveSpeed == 0.5:
            self.moveSpeed *= random.randint(4, 10) *0.1
        self.isJumping = True
        if self.isGrounded:
            self.yVelocity += self.jumpHeight * random.random() * 0.6
        self.move()
        if self.x < 0:
            self.direction = 1
            self.x = 0
            self.xVelocity *= -1
        elif self.x > windowDim[0]:
            self.direction = -1
            self.xVelocity *= -1
            self.x = windowDim[0]



pygame.init()
display = pygame.display.set_mode(windowDim)
pygame.display.set_caption("Game")
display.fill((120, 20, 200))

players = []
for x in range(20):
    players.append(Player(
        windowDim[0] * random.random(),
        windowDim[1]* random.random(),
        direction=random.choice([1,-1])
        ))


run = True
while run:
    pygame.time.delay(10)
    display.fill((120, 20, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for player in players:
        player.AutoBounce()
        player.movement()
        player.draw(display)
        if keys[pygame.K_RIGHT]:
            player.direction = 1
            player.move()
        if keys[pygame.K_LEFT]:
            player.direction = -1
            player.move()
        #if keys[pygame.K_SPACE] and player.isGrounded:
        if True and player.isGrounded:
            player.isJumping = True
            player.yVelocity += player.jumpHeight
        else:
            player.isJumping = False
    pygame.display.flip()
pygame.quit()
