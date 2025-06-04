import shutil, os
checking = True
drivepaths = ["C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\"]
drivenames = ["C","D","E","F","G","H","I","J"]
drives = []
folders = []
x = 0

while checking:
    if os.path.exists(drivepaths[x]):
        print("Drive", drivenames[x],"is connected")
        drives.append(drivepaths[x])
        x += 1
    else:
        print("Drive", drivenames[x], "is not connected")
        x += 1
    if x == len(drivepaths):
        checking = False

print((len(drives)), "drives are connected")
print(drives)
x = 0

for thing in drives:
    drives[x] += "DnD"
    x += 1
x = 0
print(drives)

for thing in drives:
    if os.path.exists(drives[x]):
        folders.append(drives[x])
    x+=1
x = 0
print(folders)

for thing in folders:
    shutil.rmtree(folders[x])
    shutil.copytree("C:\\Users\\gmagu\\DnD", folders[x])
    print("Files copied to", folders[x])
    x += 1
print("Cloning Complete"); print("Have a nice day")