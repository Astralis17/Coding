class Vector2:
        def __init__(self, x:int|float=0, y:int|float=0, angle=0, amplitude=0):
                if angle or amplitude:
                        self.angle = angle
                        self.amplitude = amplitude
                        self.x, self.y = numericalForm(angle, amplitude)
                else:
                        self.x = x
                        self.y = y
                        self.angle, self.amplitude = self.polar()
                self.xy = [self.x,self.y]
        
        def polar(self):
                self.angle, self.amplitude = polarForm(self.x,self.y)
                return self.angle, self.amplitude

        def numerical(self):
                self.xy = list(numericalForm(self.angle, self.amplitude))
                self.x, self.y = self.xy
                return self.xy

        def rotate(self, x:float):
                """Rotates vector by x radians and returns the numerical form"""
                self.angle += x
                self.numerical()
                return self.xy
        def __str__(self):
                return f"{self.xy}"

        def __sub__(self, otherVector):
                pass
                

def rangeLimit(x, floor= 0, roof=1, loop=False):
        if not loop:
                if x < floor:
                        x = floor
                elif x > roof:
                        x = roof
        else:
                if x < floor:
                        x = roof
                elif x > roof:
                        x = floor
        return x

def fRange(start:float|int, stop:float|int, step:float|int):
        r = [start]
        while r[-1] < stop:
                r.append(r[-1]+step)
        return r



class number:
        def __init__(self, inputString = "", power = 1, mult = 1):
                if inputString != "":
                        power = inputString.split("^")[-1]
                        mult = inputString.split("x")[0]
                try:
                        self.mult = float(mult)
                except ValueError:
                        self.mult = 1

                try:
                        self.power = float(power)
                except ValueError:
                        self.power = 1

        def __call__(self, input):
                x = input**self.power
                x *= self.mult
                return x

        def integrate(self):
                integral = number(power=self.power+1, mult=self.mult/(self.power+1))
                return integral

        def __str__(self):
                return f"{self.mult}x^{self.power}"

def polarForm(x,y):
        """Returns the polar form of a given numerical vector in the format (radians, amplitude)"""
        import math
        angle = math.atan2(y,x)
        amplitude = math.dist([0,0],[x,y])
        return (angle, amplitude)
def numericalForm(angle, amplitude):
        """Returns the numerical form of a given polar vector in the format (x, y)"""
        import math
        y = math.sin(angle)*amplitude
        x = math.cos(angle)*amplitude
        return (x,y)

if __name__ == "__main__":
        import math
        v1 = [5,4]
        v1Polar = polarForm(v1[0], v1[1])
        print("v1\n",v1Polar)
        v1Numerical = numericalForm(v1Polar[0]+math.radians(45),v1Polar[1])
        print(v1Numerical)

        v1Polar = polarForm(v1Numerical[0], v1Numerical[1])
        print(v1Polar, f"rad dif: {+math.radians(45)}\n\nv2")


        v2 = [2.5,5]
        v2Polar = polarForm(v2[0], v2[1])
        print(v2Polar)
        v2Numerical = numericalForm(v2Polar[0]+math.radians(45),v2Polar[1])
        print(v2Numerical)

        v2Polar = polarForm(v2Numerical[0], v2Numerical[1])
        print(v2Polar, f"rad dif: {+math.radians(45)}")
