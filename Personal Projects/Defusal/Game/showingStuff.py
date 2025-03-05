import utils, hashlib

DATA = utils.initDATA()

utils.seedGen(hashlib.md5)#

for key in DATA.keys():
        print("\nData Set for ", key[0].capitalize() + key[1:], " difficulty")
        for obj in DATA[key].keys():
                print(obj[0].capitalize() + obj[1:], ":", DATA[key][obj])

options = [x for x in DATA["difficulties"]["hard"]["weights"].keys()]
weights = []
for option in options:
        weights.append(DATA["difficulties"]["hard"]["weights"][option])
print("\n\nOptions : ", options)
print("\nWeights : ", weights)

utils.weightedChoice(options, weights)