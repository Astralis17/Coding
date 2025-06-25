import aTools
import os

directoryPath = "C:\\Users\\gmagu\\Documents\\GitHub\\Multiverse"#aTools.localPath("../Defusal/Game")

directories = []
filePaths = {}
files = []
filesByType = {
        "types":[]
}
def findDirectories(path):
        dirs = os.listdir(path)
        for x in dirs:
                if x.count(".") == 0:
                        findDirectories(os.path.join(path, x))
                else:
                        files.append(x)
                        filePaths.update({x:os.path.join(path, x)})
                        type = x.split(".")[-1]
                        if f".{type}" not in filesByType["types"]:
                                filesByType.update({f".{type}":[x]})
                                filesByType["types"].append(f".{type}")
                        else:
                                filesByType[f".{type}"].append(x)

findDirectories(directoryPath)
while len(directories) > 0:
        findDirectories(directories.pop(0))


'''for file in files:
        print(filePaths[file])
'''
print(f"{type}: {filesByType[".md"]}")
print(f"File Count: {len(filesByType[".md"])}\n")

unpublished = 0
unmarkedFiles = []
for path in filesByType[".md"]:
        file = open(filePaths[path], "r")
        lines = file.readlines()
        firstLine = lines[0]
        if firstLine != "---\n":
                unpublished += 1
                unmarkedFiles.append(path)
                '''
                fileW = open(filePaths["Home.md"], "w")
                fileW.write("---\ndg-publish: true\n---\n" + lines)
                fileW.close()
                '''
print(unpublished)
print(unmarkedFiles)