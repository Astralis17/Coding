import shutil, os, time,  info

print("Welcome to the Nitrox Server manager")
mode = 0
run = True

def statusCheck():
    print()
    print("Save Slot Status")
    print("Slot     :  In use")
    print("Slot 1   :", os.path.exists(r"C:\Users\gmagu\Desktop\Coding\Personal Projects\Nitrox Server Manager\Worlds\1\world"))
    print("Slot 2   :", os.path.exists(r"C:\Users\gmagu\Desktop\Coding\Personal Projects\Nitrox Server Manager\Worlds\2\world"))
    print("Slot 3   :", os.path.exists(r"C:\Users\gmagu\Desktop\Coding\Personal Projects\Nitrox Server Manager\Worlds\3\world"))
    print("Slot 4   :", os.path.exists(r"C:\Users\gmagu\Desktop\Coding\Personal Projects\Nitrox Server Manager\Worlds\4\world"))
    print("Game Slot:", os.path.exists(r"C:\Users\gmagu\Downloads\Nitrox\world"))

    print()


def load():
    check = input("Do you want to save first (y/n): ")
    if check == "y":
        save()
    elif check == "Y":
        save()
        statusCheck()
        try:
            shutil.rmtree(r"C:\Users\gmagu\Downloads\Nitrox\world")
        except FileNotFoundError:
            slot = 0
        while os.path.exists(r"C:\Users\gmagu\Downloads\Nitrox\world"):
            time.sleep(1)  
        slot = input("Which slot(1-4): ")
        string = "Personal Projects\\Nitrox Server Manager\\Worlds\\" + slot + "\\world"
        shutil.copytree(string, "C:\\Users\\gmagu\\Downloads\\Nitrox\\world")
        print("Slot", slot, "loaded successfully")
    print()


def save():
    statusCheck()
    slot = input("Which slot(1-4): ")
    string = "Personal Projects\\Nitrox Server Manager\\Worlds\\" + slot + "\\world"
    try:
        shutil.rmtree(string)
    except FileNotFoundError:
        slot = slot
    shutil.copytree("C:\\Users\\gmagu\\Downloads\\Nitrox\\world", string)
    print("World saved to Slot", slot, "successfully")
    print()

def wipe():
    statusCheck()
    slot = input("Which slot do you want to wipe(Enter 0 to wipe loaded save): ")
    if slot == "0":
        string = "C:\\Users\\gmagu\\Downloads\\Nitrox\\world"
    else:
        string = "Personal Projects\\Nitrox Server Manager\\Worlds\\" + slot + "\\world"
    print("Are you sure you want to wipe this save slot")
    check = input("Y/n:")
    if check == "n":
        print()
    elif check == "N":
        print()
    else:
        try:
            shutil.rmtree(string)
        except FileNotFoundError:
            return
        print("Data Wiped successful;y")
        print()

def openClient():
    os.startfile(r"C:\Users\gmagu\Downloads\Nitrox\NitroxLauncher.exe")
    print("Client Opened")
    print()

while run:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Input a number based on the desired action")
    print("1 to Load")
    print("2 to Save")
    print("3 to Wipe a Save Slot")
    print("4 to Display Save Slot Status's")
    print("5 to Open Client")
    print("6 to Quit")

    mode = int(input("Mode: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    if mode == 1:
        load()
    if mode == 2:
        save()
    if mode == 3:
        wipe()
    if mode == 4:
        statusCheck()
    if mode == 5:
        print()
        openClient()
    if mode == 6:
        quit()
    