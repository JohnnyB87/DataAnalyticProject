import numpy as np
from glob import glob
import os

column = {"Year": 0, "Month": 1, "Total": 2, "Most": 3, "Rain Days": 4}

def main():
    while True:
        userInput = 0
        while(userInput < 1 or userInput > 6):
            printMainMenu()
            userInput = int(input("Please select one of the above options: "))
        if userInput != 6:
            runOptionMain(userInput)
        else:
            print("\n\nYou Exited the program")
            break


def testNumpy():
    test = openFile("Cork")
    testAll = importAllFiles()
    print("Total Test: ", np.sum(test[:, column["Most"]], axis=0))
    print("Total TestAll: ", np.sum(testAll[:, column["Most"]], axis=0))


def printMainMenu():
    print("\n\nMain Menu"
          "\n1. Basic Statistics for Total Rainfall (Millimetres)"
          "\n2. Basic Statistics for Most Rainfall in a Day (Millimetres)"
          "\n3. Basic Statistics for Number of Rain days (0.2mm or More)"
          "\n4. Wettest Location"
          "\n5. Percentage of Rain Days"
          "\n6. Exit")


def printSecondaryMenu():
    print("\n\n1. Belfast"
          "\n2. Cork"
          "\n3. Dublin"
          "\n4. Galway"
          "\n5. Limerick")


def runOptionMain(choice):
    if choice > 0 and choice < 4:
        userInput = -1
        while userInput < 0 or userInput > 5:
            printSecondaryMenu()
            userInput = int(input("Please select a location: "))
        county = getCounty(userInput)
        file = openFile(county)
        if choice == 1:
            totalRainfallStats(file)
        elif choice == 2:
            mostRainfallStats(file)
        elif choice == 3:
            rainDayRainfallStats(file)
    else:
        dic = readAllFiles()
        if choice == 4:
            totalRainfallStatsAll(dic)
        else:
            percentageOfRainfall(dic)


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

def readAllFiles():
    fnames = glob('../rainFallData/*.txt')
    fnames.sort()

    dic = {}
    for f in fnames:
        sep = ''
        county = sep.join(f)
        county = county[16:len(county)-12]
        dic[county] = np.loadtxt(f)

    return dic


def totalRainfallStats(file):
    print("Most Rainfall: ", np.amax(file[:, column["Total"]], axis=0))
    print("Average of Most Rainfall: ", np.mean(file[:, column["Total"]], axis=0))


def mostRainfallStats(file):
    print("Most Rainfall: ", np.amax(file[:, column["Most"]], axis=0))
    print("Average of Most Rainfall: ", np.mean(file[:, column["Most"]], axis=0))


def rainDayRainfallStats(file):
    print("Most Rainfall: ", np.amax(file[:, column["Rain Days"]], axis=0))
    print("Average of Most Rainfall: ", np.mean(file[:, column["Rain Days"]], axis=0))


def totalRainfallStatsAll(dic):
    max = 0.0
    county = ""
    for key, value in dic.items():
        total = np.sum(dic[key][:, column["Total"]], axis=0)
        if total > max:
            max = total
            county = key
        print(key, " : ", total)
    print("Wettest location: ", county, " with ", max, "mm")


def percentageOfRainfall(dic):
    threshold = int(input("Please enter maximum threshold value for number of rain days: "))
    for key, value in dic.items():
        res = np.count_nonzero(dic[key][:, column["Rain Days"]] <= threshold)
        tot = np.count_nonzero(dic[key][:, column["Rain Days"]])
        print('TOT: ' , tot, "RES: ", res )
        print(key, " : ", res/tot*100,"%")

main()

