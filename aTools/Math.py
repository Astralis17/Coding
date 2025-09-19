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

if __name__ == "__main__":
        x = number("3x^2")
        print(x(2))
        xIntegral = x.integrate()
        print(xIntegral(2))