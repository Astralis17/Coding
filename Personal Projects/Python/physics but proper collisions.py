from __future__ import annotations
import pygame, math, aTools


pygame.init()

display = pygame.display.set_mode((800, 600))
"""
v = -eu
m1*u1 + m2*u2 = m1*v1 + m2*v2
"""
clock = pygame.time.Clock()

idSphereNum = 0
idWallNum = 0
collisionCount = 0
deltaTime = 1
class Sphere:
        colCoolDown = 0
        drawVectors2 = True
        def __init__(self, position, window, size, mass, velocity, elasticity, sphereManager):
                global idSphereNum
                self.id = idSphereNum
                idSphereNum += 1
                
                if velocity:
                        self.velocity:list[float] = velocity
                else:
                        self.velocity:list[float] = [0,0]
                self.position = position
                self.display:pygame.Surface = window
                self.size:float = size
                self.mass:float = mass
                self.elasticity:float = elasticity
                self.sphereManager:SphereManager = sphereManager

                self.colour = aTools.randomRGB()
                self.vectorColour = aTools.randomRGB()
                

        def tick(self):
                self.collisionDetection()
                self.move()
                self.draw()

        def move(self):
                if self.colCoolDown > 0:
                        ...
                        # return
                for index, value in enumerate(self.velocity):
                        self.position[index] += value

        def collisionDetection(self):
                global collisionCount
                if self.colCoolDown > 0:
                        ...
                        self.colCoolDown =0
                else:
                        self.drawTangent=False
                        for otherSphereId in self.sphereManager.occupiedIds:
                                otherSphere:Sphere = self.sphereManager[otherSphereId]
                                if otherSphereId != self.id and math.dist(self.position, otherSphere.position) < self.size+otherSphere.size:
                                        self.drawTangent=True
                                        self.collisionWithSphere(otherSphere)
                                        self.colCoolDown = 2
                                        otherSphere.colCoolDown = 3
                                        collisionCount += 1
                                        print(collisionCount)
                        for wallId in wallManager.occupiedIds:
                                wall:Wall = wallManager[wallId]
                                nearX = max(wall.rect.left, min(self.position[0], wall.rect.right))
                                nearY = max(wall.rect.top, min(self.position[1], wall.rect.bottom))

                                if math.dist((nearX, nearY), self.position) < self.size:
                                        self.collisionWithWall(wall, (nearX, nearY))
                                        self.colCoolDown = 2
                                        collisionCount += 1
                                        print(collisionCount)


        def collisionWithSphere(self, otherSphere:Sphere):
                e = self.restitutionCoefficient(otherSphere)
                vector1 = aTools.Math.Vector2(self.velocity[0], self.velocity[1])
                vector2 = aTools.Math.Vector2(otherSphere.velocity[0], otherSphere.velocity[1])
                dx = self.position[0]-otherSphere.position[0]
                dy = self.position[1]-otherSphere.position[1]
                angleBetween = math.atan2(dy,dx)

                
                tangentAngle = angleBetween
                # print(math.degrees(tangentAngle))

                # print(f"Initial\n{otherSphere.id}: {vector2}")
                # print(f"{self.id}: {vector1}")

                vector1.rotate(tangentAngle)
                vector2.rotate(tangentAngle)

                # print(f"\nPost Rotation\n{otherSphere.id}: {vector2}")
                # print(f"{self.id}: {vector1}")

                for dimension in [0,1]:
                        u1 = vector1.xy[dimension]
                        u2 = vector2.xy[dimension]
                        p1 = u1*self.mass
                        p2 = u2*otherSphere.mass

                        v1 = (p1+p2-otherSphere.mass*e*(u1-u2))/(self.mass+otherSphere.mass)
                        v2 = (p1+p2-self.mass*-e*(u1-u2))/(self.mass+otherSphere.mass)

                        vector1.xy[dimension] = v1
                        vector2.xy[dimension] = v2
                        vector1.x, vector1.y = vector1.xy
                        vector2.x, vector2.y = vector2.xy
                vector1.polar()
                vector2.polar()

                # print(f"\nPost Collision\n{otherSphere.id}: {vector2}")
                # print(f"{self.id}: {vector1}")

                vector1.rotate(-tangentAngle)
                vector2.rotate(-tangentAngle)

                
                # print(f"\nPost Reverse Rotation\n{otherSphere.id}: {vector2}")
                # print(f"{self.id}: {vector1}")
                self.velocity = vector1.numerical()
                otherSphere.velocity = vector2.numerical()

        def collisionWithWall(self, wall, nearestPoint):
                e = self.restitutionCoefficient(wall)
                print("Click")

                if abs(self.position[0] - nearestPoint[0]) < abs(self.position[1]-nearestPoint[1]):
                        dimension = 1
                else:
                        dimension = 0
                        

                self.velocity[dimension] = -self.velocity[dimension]

        def draw(self):
        
                pygame.draw.circle(self.display, self.colour, self.position, self.size)


                if self.drawVectors2:
                        endPos = (
                                self.position[0] + 10*self.velocity[0],
                                self.position[1] + 10*self.velocity[1]
                        )
                        pygame.draw.line(self.display, self.vectorColour, self.position, endPos, 3)
                        # pygame.draw.line()

        def restitutionCoefficient(self, collidingObj:Sphere)->float:
                if type(collidingObj) == type(int):
                        return self.elasticity * sphereManager[collidingObj].elasticity
                else:
                        return self.elasticity*collidingObj.elasticity

                
class SphereManager(dict):
        def __init__(self):
                self = {0:0}

        def addSphere(self, position, window=display, size=15, mass=2, velocity=None, elasticity=1):
                s = Sphere(position, window, size, mass, velocity, elasticity, self)
                self.update({s.id: s})
                self.occupiedIds = range(s.id+1)

        def tick(self):
                for id in self.keys():
                        self[id].tick()

        def restitutionCoefficient(self, id1, id2):
                return self[id1].restitutionCoefficient(id2)

class WallManager(dict):
        def __init__(self):
                self = {0:0}

        def addWall(self, rect, window=display, drawing=False, elasticity=1):
                w = Wall(rect, window, elasticity, drawing, self)
                self.update({w.id: w})
                self.occupiedIds = range(w.id+1)

        def tick(self):
                for id in self.keys():
                        self[id].tick()

class Wall():
        def __init__(self, rect, window, elasticity, drawing, wallManager):
                global idWallNum
                self.id = idWallNum
                idWallNum += 1
                self.rect = pygame.Rect(rect)
                self.display:pygame.Surface = window
                self.elasticity = elasticity
                self.drawing = drawing
                self.wallManager = wallManager

        def tick(self):
                if self.drawing:
                        self.draw()

        def draw(self):
                pygame.draw.rect(self.display, "grey", self.rect)

class Cursor():
        position = [0,0]
        def __init__(self):
                ...
        def tick(self):
                self.position = list(pygame.mouse.get_pos())
                self.pressed = pygame.mouse.get_pressed()


sphereManager = SphereManager()
wallManager = WallManager()
sphereManager.addSphere([50, 500], mass = 100, velocity=[1, -2])
sphereManager.addSphere([100, 500], mass = 1, velocity=[0, 3])
sphereManager.addSphere([750, 100], mass = 2, velocity=[-6, 13])

wallManager.addWall((0,0,-50,600), drawing=True)  # Left
wallManager.addWall((0,0,800,-50), drawing=True)  # Top
wallManager.addWall((0,600,800,650), drawing=True)# Right
wallManager.addWall((800,0,850,600), drawing=True)# Bottom


run = True
while run:
        deltaTime = clock.tick(60) / 1000
        pygame.time.delay(20)
        display.fill("black")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        sphereManager.tick()
        wallManager.tick()


        pygame.display.update()

# print(f"{sphereManager=}")
# print(f"{wallManager=}")