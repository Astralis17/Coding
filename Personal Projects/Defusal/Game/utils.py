from pygame import font
font.init()
my_font = font.SysFont('Comic Sans MS', 30)

def seedGen(hash, seedInput="NULL"):
        from random import seed, uniform
        if seedInput == "NULL":
                seedInput = input("Seed: ")
        if seedInput == "":
                seedInput = str(uniform(100000, 999999))

        step1 = hash(seedInput.encode("ascii"))
        step2 = step1.digest()
        seed(step2)
        return step2

def initDATA():
        from json import load as JSload
        file = open("Personal Projects/Defusal/Game/data.json", "r")
        DATA = JSload(file)
        return DATA


def weightedChoice(weightsDict):
        from random import randint
        max = 0
        keys = list(weightsDict.keys())
        for option in keys:
                max += weightsDict[option]

        x = randint(0, max)
        i = 0
        y = 0
        for option in keys:
                if i == 0:
                        if x in range(0, weightsDict[option]):
                                break
                else:
                        if x in range(y, weightsDict[option]+y):
                                break
                i += 1
                y += weightsDict[option]
        return option


