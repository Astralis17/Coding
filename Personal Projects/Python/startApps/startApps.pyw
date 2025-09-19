import os
from aTools import localPath

verbose = False

checking = True
drivepaths = ["C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\"]
drivenames = ["C","D","E","F","G","H","I","J"]
drives = []
folders = []
"""while checking:
        if os.path.exists(drivepaths[x]):
                print("Drive", drivenames[x],"is connected")
                drives.append(drivepaths[x])
                x += 1
        else:
                print("Drive", drivenames[x], "is not connected")
                x += 1
        if x == len(drivepaths):
                checking = False"""
for drivenum, drivepath in enumerate(drivepaths):
        if os.path.exists(drivepath):
                if verbose: print(f"Drive {drivenames[drivenum]} is connected")
                drives.append(drivepath)
        else:
                if verbose: print(f"Drive {drivenames[drivenum]} is disconnected")


print((len(drives)), "drives are connected")
print(drives)
x = 0
for drive in drives:
        if os.path.exists(drive + "startApps"):
                folders.append(drive + "startApps")
print(folders)
launched = False
for folder in folders:
        for file in os.listdir(folder):
                if file.endswith(".lnk"):
                        try: os.startfile(f"{folder}/{file}"); launched = True
                        except FileNotFoundError: pass
if launched == False:
        os.startfile(localPath("../startApps/error.vbs"))
