import numpy as np
from glob import glob

column = {"Year": 0, "Month": 1, "Total": 2, "Most": 3, "Rain Days": 4}

def main():
    userInput = 0
    while(userInput < 1 or userInput > 6):
        printMainMenu()
        userInput = int(input("Please select one of the above options: "))
    runOptionMain(userInput)
    # print(getCounty(userInput))




def testNumpy():
    test = openFile("Cork")
    testAll = importAllFiles()
    print("Total Test: ", np.sum(test[:, column["Most"]], axis=0))
    print("Total TestAll: ", np.sum(testAll[:, column["Most"]], axis=0))


def printMainMenu():
    print("Main Menu"
          "\n1. Basic Statistics for Total Rainfall (Millimetres)"
          "\n2. Basic Statistics for Most Rainfall in a Day (Millimetres)"
          "\n3. Basic Statistics for Number of Rain days (0.2mm or More)"
          "\n4. Wettest Location"
          "\n5. Percentage of Rain Days"
          "\n6. Exit")


def printSecondaryMenu():
    print("1. Cork"
          "\n2. Belfast"
          "\n3. Dublin"
          "\n4. Galway"
          "\n5. Limerick"
          "\nPlease select a location: 1")


def runOptionMain(choice):
    if choice > 0 and choice < 4:
        userInput = -1
        while userInput < 0 or userInput > 5:
            printSecondaryMenu()
            userInput = int(input("Please select one of the above options: "))
        county = getCounty(userInput)
        file = openFile(county)
        if choice == 1:
            totalRainfallStats(file)


def getCounty(choice):
    switcher = {
        1: "Belfast",
        2: "Cork",
        3: "Dublin",
        4: "Galway",
        5: "Limerick",
    }
    return switcher.get(choice, "Invalid option")


def openFile(county):
    return np.loadtxt("../rainFallData/" + county + "Rainfall.txt")

def importAllFiles():
    fnames = glob('../rainFallData/*.txt')
    fnames.sort()
    arrays = [np.loadtxt(f) for f in fnames]
    return np.concatenate(arrays)


def totalRainfallStats(file):
    print("Most Rainfall: ", np.amax(file[:, column["Most"]], axis=0))
    print("Average of Most Rainfall: ", np.mean(file[:, column["Most"]], axis=0))



main()

