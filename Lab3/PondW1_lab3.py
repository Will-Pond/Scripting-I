#!/usr/bin/python3

#Will Pond and Will Cuthbert

import os

def exists(path):           # This function checks is a path exists

    if os.path.exists(path):
        return True
    else:
        return False


def renameFile(fileName, newName):    # This function rename a file name

    if os.path.isfile(fileName):
        os.rename(fileName, newName)
    else:
        print("Error: file not found ")

def createDir(name):                         # This function creates a new directory
    if not os.path.isdir(name):
        os.makedirs(name)


def getType(fileOrPath):                        # This function determine if it is a file or a directory

    if os.path.isdir(fileOrPath):
        type = "Directory"
    elif os.path.isfile(fileOrPath):
        type = "File"
    else:
        type = "not a file or directory"
    return type

def displayContents(directoryName):      # This function lists everything in a selected directory via a for loop and print out the content


    if exists(directoryName):
        print('%-25s %-25s' % ('Name', 'Type'))
        print('%-25s %-25s' % ('-----', '-----'))
        contents=os.listdir(directoryName)
        for content in contents:

            print('%-25s %-25s' % (content, getType(content)))     # prints the content but also prints the type
    else:
        print("Error: directory not found")


def createFiles(fileNamePrefix, numOfFiles, ext):    # This function creates multipy files by the user input
    x = 0
    y = 1
    while x < numOfFiles:
        f = open(f'{fileNamePrefix}_{y}.{ext}', 'a')
        x += 1
        y += 1
        f.close
def createSubDirectories(directoryName, numberToCreate):  # This function creates subDirectories by the user input
    x = 0
    y = 1
    while x < numberToCreate:
        os.mkdir(directoryName+str(y))
        x += 1
        y += 1

def renameFiles(targetDirectory, currentExt, newExt):   # This function renameFiles inside the target Directory by changing the extension of the file
    for files in os.listdir(targetDirectory):
        base, ext = os.path.splitext(files)
        if os.path.isfile(files):
            os.rename(files, base + "." + newExt)



def main():
                                               # Gets the Directories
    homeDirectory=os.path.expanduser("~")
    currentDirectory=os.getcwd()
    currentUser=os.getenv('USERNAME')           # change to 'USER' for linux
                                                # prints out the Directories
    print("Your currently directory is:", currentDirectory)
    print("Your home directory is:", homeDirectory)
    print("Your current username is:", currentUser)
                                                          # create and changes the directory to CITSpring2024
    createDir(homeDirectory+"\CITSpring2024"+currentUser) # change slash for linux
    getType(homeDirectory+"\CITSpring2024"+currentUser)
    os.chdir(homeDirectory+"\CITSpring2024"+currentUser)
    newDirectory = os.getcwd()
    print("Your current directory now is", newDirectory)
                                                           # ask the user for input of name and number of the files
    name_file = input("Name the files you want to create: ")
    number_file = int(input("How many files would you like to make: "))
    while number_file <= 0:
        print("You cannot use negative numbers or zero, try again.")            # Keep going until you enter a value input
        number_file = int(input("How many files would you like to make: "))
    ext_file = input("What extension would you like these files to be: ")       # ask the user for input the type of extension for the files to be created
    ext = ["txt", "png", "doc", "dat"]
    while ext_file not in ext:
        print("Invalid extension, please try again.")                               # Keep going until you enter a value input
        ext_file = input("What extension would you like these files to be: ")

    name_dir = input("Name the subdirectories you want to create: ")
    number_dir = int(input("How many subdirectories would you like to make: "))
    while number_dir <= 0:
        print("You cannot use negative numbers or zero, try again.")                             # Keep going until you enter a value input
        number_dir = int(input("How many subdirectories would you like to make?: "))

    createFiles(name_file, number_file, ext_file)     # creates the files
    createSubDirectories(name_dir, number_dir)    # creates the subdirectories
    displayContents(newDirectory)           # display the content inside the directory to the output

    new_ext = input("Enter a new extension for your files: ")       # asks the user for type in a new extension for the files you created
    while new_ext not in ext:
        print("Invalid extension, please try again.")                # Keep going until  enter a value input
        new_ext = input("Enter a new extension for your files: ")
    renameFiles(newDirectory, ext_file, new_ext)                        # renames the files inside the directory
    displayContents(newDirectory)                               # display the content in the directory to the output

main()