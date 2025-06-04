from aTools import *

def initDATA():
        from json import load as JSload
        file = open(localPath("data.json"), "r")
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


