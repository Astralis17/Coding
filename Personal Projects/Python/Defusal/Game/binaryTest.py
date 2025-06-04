import random
conditions = [
        ((2, True),  (7, False)),#2
        ((1, True),  (2, True)),#3
        ((1, False), (7, False)),#4
        ((1, True),  (2, True), (3, True)),#5
        ((1, True),  (2, True), (3, True), (4, True)),#6
]

barLights = [random.choice([True,False]) for i in range(7)]
print(barLights)


i = 1
winCondition = 0
for condition in conditions:
        conditionFound = False
        if True not in barLights:
                winCondition = i
        else:
                for condition in conditions:
                        i += 1
                        conditionFound = True
                        for req in condition:
                                if barLights[req[0]-1] == req[1]:
                                        conditionFound = bool(conditionFound and True)
                                else:
                                        conditionFound=False
                        if conditionFound:
                                winCondition = i
                                break
                if not conditionFound:
                        if barLights.count(False) > 3:
                                winCondition = 7
                                conditionFound = True
                        elif barLights.count(True) > 5:
                                winCondition = 8
                                conditionFound = True
                        elif False not in barLights:
                                winCondition = 9
                                conditionFound = True
                        else:
                                winCondition = 10
                                conditionFound = True
                if conditionFound:
                        break
print(winCondition)

