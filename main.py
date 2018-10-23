# Name: John Brady
# Student No.: R00155390
# SDH3-A

# imports
import rainfallFunctions as rf


# main function
def main():
    while True:     # infinite loop
        userInput = 0   # set initial value for userInput variable
        while userInput < 1 or userInput > 6:   # loop until a valid number is entered
            printMainMenu()     # calls function that prints out the main menu
            try:    # try except to handle wrong input types
                # gets user input and assigns it to userInput variable
                # try's to convert input to an integer
                userInput = int(input("Please select one of the above options: "))
            except ValueError:  # if conversion fails
                # assign userInput the value -1 to continue the while loop
                userInput = -1
                print("Enter a number.")
        # if userInput is not 6 call the runOptionMain function
        if userInput != 6:
            runOptionMain(userInput)
        else:
            print("\n\nYou Exited the program")
            break


# function to print the main menu
def printMainMenu():
    print("\n\nMain Menu"
          "\n1. Basic Statistics for Total Rainfall (Millimetres)"
          "\n2. Basic Statistics for Most Rainfall in a Day (Millimetres)"
          "\n3. Basic Statistics for Number of Rain days (0.2mm or More)"
          "\n4. Wettest Location"
          "\n5. Percentage of Rain Days"
          "\n6. Exit")


# function to print the secondary menu
def printSecondaryMenu():
    print("\n\n1. Belfast"
          "\n2. Cork"
          "\n3. Dublin"
          "\n4. Galway"
          "\n5. Limerick")


# switch statement to get the county associated with the users input
def getCounty(choice):
    switcher = {
        1: "Belfast",
        2: "Cork",
        3: "Dublin",
        4: "Galway",
        5: "Limerick",
    }
    return switcher.get(choice, "Invalid option")


# function that takes the users choice and runs the necessary functions associated with that choice
def runOptionMain(choice):
    if 0 < choice < 4:  # if choice is between the values 0 and 4 exclusive
        userInput = -1  # set initial value for userInput variable
        while userInput < 0 or userInput > 5:   # loops until a valid choice is entered
            printSecondaryMenu()    # function to print the secondary menu
            try:    # try except to handle wrong input types
                # gets user input and assigns it to userInput variable
                # try's to convert input to an integer
                userInput = int(input("Please select a location: "))
            except ValueError:  # if conversion fails
                # assign userInput the value -1 to continue the while loop
                userInput = -1
                print("Enter a number")
        county = getCounty(userInput)   # get the county associated with userInput and assign it to a variable
        file = rf.openFile(county)  # get the text file associated with the county chosen
        print("\n\n", county)
        # if else statement to call the function associated with the users input
        if choice == 1:
            rf.printColumnData(file, "Total")
        elif choice == 2:
            rf.printColumnData(file, "Most")
        elif choice == 3:
            rf.printColumnData(file, "Rain Days")
    else:
        dic = rf.readAllFiles()
        if choice == 4:
            rf.totalRainfallStatsAll(dic)
        else:
            rf.percentageOfRainfall(dic)


# call main function
main()

