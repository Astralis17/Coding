try: from . import Math, Pygame
except ImportError: import Math, Pygame # type: ignore

class LerpInvalidPointsError(Exception):

        def __init__(self, message="The two points have different dimensions and are incompatible"):
                super().__init__(message)
def localPath(filepath:str) -> str:
        """Generates a local filepath for use.\n
        ../ can be used to go up a directory level"""
        from os import path
        from inspect import stack

        backs = filepath.count("../")
        filepath = filepath.replace("../", "")
        filepath = filepath.replace("/", "\\")

        scriptDirectory = path.dirname(path.abspath(stack()[1].filename))
        pathList = scriptDirectory.split('\\')
        for x in enumerate(pathList):
                pathList[x[0]] += "\\"

        scriptDir = ""
        for x in pathList[:-backs]:
                scriptDir += x
        localFilepath = path.join(scriptDir, filepath)
        return localFilepath

def seedGen(hash=None, seedInput="NULL"):
        from random import seed, uniform
        if hash is None:
                import hashlib
                hash = hashlib.md5
        if seedInput == "NULL":
                seedInput = input("Seed: ")
        if seedInput == "":
                seedInput = str(uniform(100000, 999999))

        step1 = hash(seedInput.encode("ascii"))
        step2 = step1.digest()
        seed(step2)
        return step2

def midpoint(p1,p2):
        mx = (p1[0] + p2[0]) /2
        my = (p1[1] + p2[1]) /2
        return (mx, my)


def lerp(p1,p2, t):
        """LERP, short for Linear Interpolation, gets the point between two points with the t value measuring the percentage of the new point from"""
        if len(p1) != len(p2):
                raise LerpInvalidPointsError()
        dimensions = len(p1)
        point = []
        for i in range(dimensions):
                p = p1[i] + (p2[i]*t) - (p1[i]*t)
                point.append(p)
        return point



def randomiseList(list):
        from random import randint
        newList = []
        while list != []:
                ran = randint(0, len(list) - 1)
                newList.append(list.pop(ran))
        return newList


def randomRGB():
        from random import random
        colour = 400
        rgb = [0,0,0]
        for i in range(0,3):
                ran = random()
                val = Math.rangeLimit(colour * ran, 0, 255)
                rgb[i] = val
                colour -= val
        rgb = randomiseList(rgb)
        return tuple(rgb)
class LIST(list):
        def __toString__(self):
                outString = ""
                for element in self:
                        outString += str(element)
                return outString
list = LIST

