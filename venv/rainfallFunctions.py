# Name: John Brady
# Student No.: R00155390
# SDH3-A

# imports
import numpy as np
from glob import glob

# dictionary that associates the column index's with a name
column = {"Year": 0, "Month": 1, "Total": 2, "Most": 3, "Rain Days": 4}


# function that returns a numPy array associated with the county chosen
def openFile(county):
    return np.loadtxt("../rainFallData/" + county + "Rainfall.txt")


# function that reads all files from the rainFallData directory that end in Rainfall.txt
# converts files into numPy arrays and places them into a dictionary
# dictionary keys are the county names
def readAllFiles():
    # get files from directory and stores as a tuple
    fnames = glob('../rainFallData/*Rainfall.txt')
    # sort the tuple
    fnames.sort()
    # create empty dictionary
    dic = {}
    # loop through file in tuple
    for f in fnames:
        sep = ''    # blank separator
        county = sep.join(f)    # convert tuple elements into a string with separator
        county = county[16:len(county)-12]  # get county name from known location
        dic[county] = np.loadtxt(f)     # assign numPy arrays to dictionary with the county name as the key
    return dic  # return the dictionary


# function that prints a columns max value and the columns average
def printColumnData(file, columnKey):
    print("Most Rainfall: ", np.amax(file[:, column[columnKey]], axis=0))
    print("Average Rainfall: ", np.mean(file[:, column[columnKey]], axis=0))


# function that prints the total rainfall per county
# also finds which county had the highest rainfall
def totalRainfallStatsAll(dic):
    # set variables initial values
    maxValue = 0.0
    county = ""
    print("\n\n")
    # loop through the dictionary
    for key, value in dic.items():
        # get the total value of specified column and assign it to total variable
        total = np.sum(dic[key][:, column["Total"]], axis=0)
        # compare toatl with the current max value
        if total > maxValue:
            # if total is greater assign maxValue its new value
            # and assign the associated county to the county variable
            maxValue = total
            county = key
        print(key, " : ", total)
    print("Wettest location: ", county, " with ", maxValue, "mm")


# function that asks for user to input some data
def askForThreshold():
    threshold = -1
    while threshold < 0 or threshold > 31:
        try:
            threshold = int(input("Please enter maximum threshold value for number of rain days: "))
        except ValueError:
            threshold = -1
            print("\n\nEnter a number please.")
    return threshold


# function to find the percentage of days it rained given a threshold
def percentageOfRainfall(dic):
    threshold = askForThreshold()  # get the threshold from user
    # loop through the dictionary
    for key, value in dic.items():
        length = len(dic[key])  # get the total length of a column
        # get all non zero elements in column that are less than the threshold
        count = np.count_nonzero(dic[key][:, column["Rain Days"]] <= threshold)
        # get all non zero elements of the array
        totalNonZero = np.count_nonzero(dic[key][:, column["Rain Days"]])
        # calculate the number of zeros in the array
        noOfZeros = length - totalNonZero
        # add the number of zeros to the current count of numbers less than the threshold
        res = count + noOfZeros
        # calculate the percentage
        percentage = length/res*100
        print(key, " : ", percentage, "%")
