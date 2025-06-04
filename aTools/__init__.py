from . import Pygame


def localPath(filepath:str):
        from os import path
        from inspect import stack
        scriptDirectory = path.dirname(path.abspath(stack()[1].filename))
        localFilepath = path.join(scriptDirectory, filepath)
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

class LIST(list):
        def __toString__(self):
                outString = ""
                for element in self:
                        outString += str(element)
                return outString
list = LIST