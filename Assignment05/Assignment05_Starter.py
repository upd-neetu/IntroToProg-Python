# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#   NeetuUpadhyay, 05/17/2023, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFileName = "ToDoFile.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, Load from ToDoFile.txt into a python Dictionary.
try:
    objFile = open(objFileName, "r")
    for line in objFile:
        strData = line.split(",")
        dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except FileNotFoundError:
    print("ToDoFile.txt not found. Creating a new file.")

# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5] - ")
    print()  # Add an extra line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("What is the task? - ").strip()
        strPriority = input("What is the priority? [high|low] - ").strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

    # Step 5 - Remove an item from the list/Table
    elif strChoice.strip() == '3':
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if blnItemRemoved:
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

    # Step 6 - Save tasks to the ToDoFile.txt file
    elif strChoice.strip() == '4':
        with open(objFileName, "w") as objFile:
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        print("Data saved to ToDoFile.txt.")
        continue  # to show the menu

        # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # Exit the program
