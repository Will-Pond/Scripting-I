#!/usr/bin/python3

# Will Pond CIT 383
# In this program it takes in two file input one to read and to create and write and find suspicious account and print them out to the conolse log

import csv

def read_data(file1):    # The read_data Function read from the input file known as file1

   with open(file1, 'r') as read_file:   # open up the input file and stores it as read_file
    csvFile = csv.reader(read_file)      # read the read_file and stores it as csvFile
    for line in csvFile:                 # looping over the csvFile by line the of file
        print(line)                    # print out the line of the file to the console

    read_file.close()                  # close the file



def create_file(file1, file2):     # The create_file Function takes in the first input file and the file name you want to create
  with open(file1, 'r') as read_file:   #same process in the function above
    reader = csv.reader(read_file)
    next(reader)              # skips the first line of the file

    with open(file2, 'w', newline='') as write_file:     # create the file with the file name given and make it a write file and stores it in write_file
      writer = csv.writer(write_file)                     # write in the file and stores it in writer

      header = ['Name', 'First IP Address', 'Login_Count', 'Login_Count_Excess']   # header for the columns in the writer file
      writer.writerow(header)       # write the header in the writer file

      counter = 0        # count the number of employee with suspicious accounts
      print('    Suspicious Employee Accounts Table:')     # title of the table for the following output to the console
      print("{:<25} {:<25}".format('    Name', 'Login Attempts'))    # headers for the following output to the console
      print("-" * 45)   # dash to separate the header and the account info

      for column in reader:   # loops of the input file and reads it line at a time
        IP_address = column[4].split(';')   # split up the all the IP Address
        first_address = IP_address[0]    # get the first IP Address and stores it in first_address
        last_name = column[1]    # get last name and stores it in last_name
        writer.writerow([column[0]+' '+column[1], first_address, column[3], int(column[3])-199])  # writes the following output to the output file from the first input file

        if ((int(column[3])) >= 200 or last_name.find('e') != -1 or last_name.find('l') != -1):   # checks if the total number login attempts is 200 or above and checks if the last name contains an e or an l in it
            counter += 1   #add one each time the if condition is true
            print("{:<30} {:<35}".format(column[0]+' '+column[1], column[3]))  # prints out the name and total number of login

    print('\ntotal number of employees with suspicious logins attempts:', counter)   # prints total number of employees with suspicious login
    read_file.close()   # closes the read file
    write_file.close()   # closes the write file

def main():  # the Main Function that call the read_data function and the create_file function

    data_log ='employee_logins.csv'  # the first imported file to be read from
    suspicious_log ='PondW1_Lab4.csv'  # the second imported file to be created

    read_data(data_log)         # calling the read_data Function passing the data_log as the parameter for the function
    create_file(data_log, suspicious_log)    # calling the create_data Function passing the data_log and suspicious_log as the parameters for the function

main()