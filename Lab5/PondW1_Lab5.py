# Will Pond
# In this program it asks user for choices on how they want to proceed with program. The choices with the program are implemented with function for each one.
# The choices are to Backup a Directory, Archiving a Directory, View Contents of a Zipped folder and Checking recently modified files in a Directory
# The fifth option to the quit the program.

import os, shutil, subprocess as sub, time, zipfile as zip  #imported fuctions and renaming them

def backup_directory(source, destination):   # The backup directory function where the user imports two directories and backup them to a target directory
    if os.path.exists(source) and os.path.exists(destination): # check if both directory exist
        print("Directory exists")
        print("Backing up file...")
        backup_code = sub.call(["rsync", "-av", source, destination])  #call the function returns executed code of the program
        if backup_code == 0:      # if backup code is zero then backup has created and if then the backup was not created
            print("The backup has been created")
        else:
            print("The backup has failed")
    else:
        print("Directory does not exist")


def archive_directory(source, archive_type, archive_name):  #archive directory is where user inputs a direcotry the type archive and the name of the archive
    types = ["zip", "tar", "gztar", "bztar", "xztar"]
    if archive_type in types and os.path.exists(source):  #checks if the archive type is one of the archive types above if not it prints out invaild Entry and if the direcotry does not exist then it will print out also "Make sure to check you Directory
        shutil.make_archive(archive_name, archive_type, source)  #Make the archive
    else:
        print("Invalid Entry Type")
        print("Make Sure Your Directory Exist")


def read_zip(filename, threshold):  #reading the zip file and getting the size of the file depending on the threshold for user enter also known what system type the file was created
    with zip.ZipFile(filename) as z: #gets the zip file
        for info in z.infolist():  # reading all the files in the zip
            if (info.file_size / 1024) > int(threshold): #if the file size is greater than the threshold user entered
                if info.create_system == 0: #if the create_system method is zero than it is Windows
                    systemType = "Windows"
                elif info.create_system == 3:  #if the create_system equals 3 then it is Unix
                    systemType = "Unix"
                else:   # else is a the systemType is Unknown
                    systemType = "Unknown"
                print("Created System is", systemType, "File Name is", filename, "File Size is", (info.file_size / 1024))  # prints out the system, the file and the file size


def directory_checker(directory): # directory_checker function check the a directory and see if any file were modified in the last month and if so print it out
    if os.path.isdir(directory): # checks if it is a directory or not
        os.chdir(directory) # change it to that current working directory
        iterdir = os.listdir(directory) # return all the list files in that directory
        one_month = time.time() - 30 * 24 * 60 * 60  # gets the one month
        print("The Following Files In The Directory Have Been Modified In The Last Month:")
        print("-" * 50)
        for file in iterdir: # gets all the file that were modified in the last month and prints it out
            if os.path.isfile(file):
                my_time = os.path.getmtime(file)
                if(my_time >= one_month):
                    print(file)
        print("-" * 50)
    else: # else get the current working directory call the function again
        cwd = os.getcwd()
        directory_checker(cwd)

def display_menu(): # Menu display function to display all the options
    print("Text Based Menu System")
    print("Press 1 for Backing up a Directory")
    print("Press 2 for Archiving a Directory")
    print("Press 3 for View Contents for a Zipped folder")
    print("Press 4 for Checking recently modified files in a Directory")
    print("Press 5 to Exit")


def main():  # The main function that call all the other function
    while True:  # while true
        display_menu() # call the display_menu function
        input_choice = input("Enter Your Choice:\n") # gets the user choice

        if(input_choice == "1"):  # 1 equals the backup directory
            source = input("Enter Current Directory:\n") # gets a Directory from the user

            while not os.path.exists(source): #keep asking to get the directory until a directory is correctly entered
                print("Not a directory, Please Try Again.")
                source = input("Enter Current Directory:\n")

            destination = input("Enter Desire Directory:\n") # gets another directory from the user

            while not os.path.exists(destination): # keep asking to get the direcotry until a directory is correctly entered
                print("Not a directory, Please Try Again.")
                destination = input("Enter Desire Directory:\n")

            backup_directory(source, destination)  #calls the backup_directory method to back it up

        elif(input_choice == "2"):  # 2 is archiving a directory
            source = input("Enter Current Directory:\n") # get a directory from the user

            while not os.path.exists(source): # keep asking for the use until the use enter a correct directory
                print("Not a Directory, Please Try Again.")
                source = input("Enter Current Directory:\n")

            archive_type = input("Enter an Archive Type:\n")  #ask for a archive type for use to input
            types = ["zip", "tar", "gztar", "bztar", "xztar"]

            while archive_type not in types:   # keep asking the use until a correct archive type is entered
                print("Invalid type, Please try again.")
                archive_type = input("Enter an Archive Type:\n")

            archive_name = input("Enter Archive Name:\n")   # ask the user to enter a name the archive
            archive_directory(source, archive_type, archive_name) # calls the archive_directory method to archive it

        elif(input_choice == "3"): # 3 read the zips file
            filename = input("Enter File Name:\n")  # gets the zip file from the user

            while not os.path.exists(filename): # keep asking until a correct zip file is entered
                print("File Does Not Exist, Please Try Again.")
                filename = input("Enter File Name:\n")

            threshold = input("Enter threshold:\n") # get a threshold number to check
            read_zip(filename, threshold)  # calls the read_zip function to read the zip file and gets the file size

        elif(input_choice == "4"):  # 4 checks the directory if any files were modified in the last month
            directory = input("Enter a Directory:\n") # get the directory from the user

            while not os.path.exists(directory): # keep ask the user for directory until a corrected directory is entered
                print("Directory Does Not Exist, Please Try Again.")

            directory_checker(directory) # calls the directory_checker method

        elif(input_choice == "5"): # 5 quits the program
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please try again") # else the user enter an Invaild choice and will keep asking until the user enter a corrected choice
main()




