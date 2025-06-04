import GV, math, functions as f
class obj1:
        def __init__(self, mass, size, velocity:list, position:list, id, colour=(255,255,255)):
                self.mass = mass
                self.velocity = velocity
                self.size = size
                self.position = position
                self.id = id
                self.colour = colour
                self.displayColour = colour

        def moveFrame(self):
                if self.position[0] > GV.windowDim[0]:
                        self.velocity[0] *= -1
                elif self.position[0] < 0:
                        self.velocity[0] *= -1
                elif self.position[1] > GV.windowDim[1]:
                        self.velocity[1] *= -1
                elif self.position[1] < 0:
                        self.velocity[1] *= -1

                self.position[0] += self.velocity[0]
                self.position[1] += self.velocity[1]
                #print(str(self.id) + ":",self.position)

                return


        def impulse(self, force=1, impulsePos=(0,0), impulseRadius=50):
                a = math.dist((self.position[0],0), (impulsePos[0],0))
                o = math.dist((0,self.position[1]), (0,impulsePos[1]))
                x = math.atan2(o,a)
                return math.degrees(x)