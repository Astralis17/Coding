import pygame, math
pygame.init()

windowDimensions = [800, 600]
display = pygame.display.set_mode(windowDimensions)

def lerp(current, target, velocity, dt, p_gain, d_gain):
        for i in [0,1]:
                if pygame.mouse.get_pressed()[0]:
                        acceleration[i] = (target[i] - current[i]) * p_gain - velocity[i] * d_gain
                else:
                        acceleration[i] = 0
                        velocity [i]*= 0.98

                velocity[i] += acceleration[i] * dt
                current[i] += velocity[i] * dt
        
        return current, velocity


cubePos = [0, windowDimensions[1]/2]
cubeVelocity = [0,0]
acceleration = [0,1]
p = 15
d = 1




clock = pygame.time.Clock()
FPS = 60  # Target frame rate


running = True
while running:
        display.fill("black")
        deltaTime = clock.tick(FPS) / 1000.0 
        mousePos = list(pygame.mouse.get_pos())

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False


        cubePos, cubeVelocity = lerp(cubePos, mousePos, cubeVelocity, deltaTime, p, d)



        pygame.draw.rect(display, "white", [*cubePos, 10,10])

        pygame.display.update()