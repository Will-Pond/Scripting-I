#!/usr/bin/python3


# Will Pond
# In this program it list the contents of a directory through the command line using command line arguments.
import os, argparse as ap


def list_dir_contents(dir_name, log_file="",
                      dirs_only=False) -> None:  # The list_dir_contents gets the contents of the direct and list it

    addir = os.listdir(dir_name)  # list the contents in the addir array and get it from the directory path
    list = []  # list of the contents in the directory
    count = 0  # count the number of entries

    if dirs_only:  # if true
        # go through the list and puts dirs it in list
        for dir in addir:
            if os.path.isdir(dir_name + "\\" + dir):
                list.append(dir)
        print(addir)

    else:  # if false
        # get all the contents and put it in list
        for dir in addir:
            list.append(dir)
        print(list)

    # check if this needs to be written to a log file
    if log_file != "":
        #  Save the contents to a log file
        f = open(log_file, "w")  # open the file and then writes in it
        f.write("-" * 8)
        f.write("\n{:<30} {:<35}".format("File/Dir#", "Name"))
        f.write("\n{:<30} {:<35}".format("*" * 9, "*" * 25))

        for i in list:  # writes all the entires
            count += 1
            f.write("\n{:<30} {:<35}".format(count, i))
        f.close()

    else:  # if not in the logfile then print to the console
        # Display the contents to the screen
        print("-" * 8)
        print("{:<30} {:<35}".format("File/Dir#", "Name"))
        print("{:<30} {:<35}".format("*" * 9, "*" * 25))

        for i in list:
            count += 1
            print("{:<30} {:<35}".format(count, i))


# parser container for arguments and option down below also and explanation about it too
parser = ap.ArgumentParser(prog="DISPLAY_DIR_CONTENTS", add_help=True, usage="./PondW1_Lab7.py [-i, -h, -d] [DIR_PATH]",
                           description="This programs list the contents of a directory base on the options")

# option i
parser.add_argument("-i", "--logfile", action="store", dest="logFile", help="Get the logfile")
# option d
parser.add_argument("-d", "--dir", action="store_true", dest="dirOnly", help="Check directory for directory")
# DIR_PATH argument
parser.add_argument("DIR_PATH", action="store",
                    help="Gets the path of the directory from which files needed to be listed")

try:  # try and catch block to catch any error that may occur when enter from the command line
    result = parser.parse_args()  # runs the parser and extracts data and puts into result

    logFileName = ""  # declare logFileName
    dirOnlyFlag = False  # declare dirOnlyFlag
    if result.logFile is not None:
        logFileName = result.logFile  # replace logFileName with result.logFile
    if result.dirOnly is not False:
        dirOnlyFlag = True

    list_dir_contents(result.DIR_PATH, logFileName, dirOnlyFlag)  # calls the list_dir_contents method

except Exception as e:  # catch the error
    print(e)  # print exception