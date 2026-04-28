from PIL import Image
from shutil import copyfile
from filecmp import cmp
import aTools, os, tqdm



files = {}
fileNames = {}
DirEntries = {}
def scanDir(path):
    contents = os.scandir(path)
    for item in contents:
        if os.path.isfile(item.path):
            fileComponents = str(item.name).split(".")
            key = "." + fileComponents[-1]
            filename = item.name
            filepath = item.path
            if key in files.keys():
                files[key].append(filepath)
            else:
                files.update({key:[filepath]})
            fileNames.update({filepath:filename})
            DirEntries.update({item.path:item})
        else:
            scanDir(item)

def viewFiles(mode):
    if mode == "a":
        for type in filetypes:
            print(f"\n{type} Files:") #  ({len(files[type])})
            for file in files[type]:
                print(f"\t{fileNames[file]}")
    else:
        print(f"\n{mode} Files:")
        for file in files[mode]:
            print(f"\t{fileNames[file]}")

# dirPath = aTools.localPath("./images")
dirPath = aTools.localPath("../../../WTAOW/C&C")
scanDir(dirPath)
filetypes = files.keys()


ready = False

print(f"\nIMAGE FORMATTER \nFile Location: {dirPath} \nFile Types:")
for type in filetypes:
    print(f"\t{type} ({len(files[type])})")

while not ready:
    mode = ""
    while not mode in filetypes and mode != ".v":
        print("\nList Files (v)\n\tOR \nBegin Conversion (initial filetype)")
        mode = input("Option: ")
        mode = "." + mode.replace(".", "")
        if not mode in filetypes and mode != ".v":
            print("Error, enter a valid option")

    if mode == ".v":
        subMode = ""
        while not subMode in filetypes and subMode != "a":
            subMode = input("\nList Files\nAll (a) \n\tOR \nList Specific File(filetype) \nMode: ")
            if subMode != "a":
                subMode = "." + subMode.replace(".", "")
        viewFiles(subMode)
    else:
        inputType = mode
        outputType = input("\nOutput File Type: ")
        outputType = "." + outputType.replace(".", "")

        safeCache = False
        cacheMode = input("Use Cache? (y/n/s) \ny (Yes) \nn (No) \ns (Safe) \nOption: ").lower()
        if cacheMode == "y": useCache = True
        elif cacheMode == "n": useCache = False
        elif cacheMode == "s": useCache = True; safeCache = True
        ready = True

print(f"Converting {inputType} files to {outputType} files")

filesToConvert = [DirEntries[file] for file in files[inputType]]
print(f"{useCache=}")
for i in tqdm.trange(len(filesToConvert)):
    file = filesToConvert[i]
    inCache = False

    fileLocation = str(file.path).replace(file.name, "")
    newFilename = str(file.name).split(".")[0] + outputType
    # print(f"{newFilename=}")
    totalFilePath = fileLocation + newFilename

    cachedPath = aTools.localPath(f"./cache/{newFilename}")
    inCache = os.path.exists(cachedPath)
    # print(f"{inCache=}")
    # print(f"{totalFilePath=}\n")

    destPath = cachedPath if useCache else totalFilePath
    if not safeCache:
        if not inCache:
            img = Image.open(file.path)

            try:
                img.save(destPath)
            except OSError:
                img = img.convert("RGB")
                img.save(destPath)
        if useCache: copyfile(cachedPath, totalFilePath)
    else:
        if not inCache:
            img = Image.open(file.path)

            try:
                img.save(destPath)
            except OSError:
                img = img.convert("RGB")
                img.save(destPath)
        