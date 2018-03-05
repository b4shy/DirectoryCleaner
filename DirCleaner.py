import os
import time
import shutil

weeks = 60 * 60 * 24 * 7

def checkPath():
    path = input("Enter Path \n")

    print("Entered Path: \n" + path)
    print("Actual Path: \n" + os.getcwd())
    if os.path.isdir(path):
        os.chdir(path)
        path = os.getcwd()
        return path
    else:
        print("Path does not exist. Leaving program\n")
        return 0


def folderManagement(path):
    print("Manually (0) or Automatically(1)\n")

    decider = int(input("0 or 1\n"))


    #MANUAL VERSION: Decide how many folders you want to create. Remaining files are copied to "Remaining"
    if not decider:
        print("How many folders shall be created?\nAKA How many weeks do you want to go back'")
        folders = int(input())
        print(range(0, folders))

        for i in range(0, folders):
            if not os.path.exists(path + "/" + str(i)):
                os.makedirs(path + "/" + str(i))
            else:
                print("Week folder", i, "already exists .")

    #AUTOMATED VERSION: Automatically creates the folders needed to cover all files
    else:
        files = os.listdir(path)
        folders = []
        for i in files:
            if os.path.isfile(i):
                timer = os.path.getmtime(i)
                passed = time.time() - timer
                passed_week = int(passed/weeks)
                if passed_week not in folders:
                    folders.append(passed_week)

        for i in folders:
            if not os.path.exists(path + "/" + str(i)):
                os.makedirs(path + "/" + str(i))
            else:
                print("Week folder", i, "already exists.")



def copying(path):
    files = os.listdir(path)

    for i in files:
        if os.path.isfile(i):
            timer = os.path.getmtime(i)
            passed = time.time() - timer
            weeks_passed = int(passed / weeks)

            if os.path.exists(path + "/" + str(weeks_passed)):
                shutil.copy(path + "/" + i, path + "/" + str(weeks_passed))
            else:
                if not os.path.isdir(path + "/" + "Remaining"):
                    os.makedirs(path + "/" + "Remaining")
                shutil.copy(path + "/" + i, path + "/" + "Remaining")
    print("DONE")


path = checkPath()

if path:
    folderManagement(path)
    copying(path)

