#from . import Pygame


def localPath(filepath:str):
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
        mx = abs(p1[0] - p2[0])
        my = abs(p1[1] - p2[1])
        return (mx, my)

def rangeLimit(x, floor= 0, roof=1):
        if x < floor:
                x = floor
        elif x > roof:
                x = roof
        return x

class LIST(list):
        def __toString__(self):
                outString = ""
                for element in self:
                        outString += str(element)
                return outString
list = LIST
