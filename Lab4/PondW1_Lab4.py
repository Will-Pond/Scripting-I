#!/usr/bin/python3

# Will Pond CIT 383
# In this program it takes in two file input one to read and to create and write and find suspicious account and print them out to the conolse log

import csv

def read_data(file1, list1, list2):    # The read_data Function read from the input file known as file1 and breaks up into two list. List1 and List2

  with open(file1, 'r') as read_file:   # open up the input file and stores it as read_file
    csvFile = csv.reader(read_file)      # read the read_file and stores it as csvFile
    next(csvFile)                          # skips the first line of the file
    for column in csvFile:                 # looping over the csvFile by line the of file
        IP_address = column[4].split(';')  # split up the all the IP Address
        first_address = IP_address[0]  # get the first IP Address and stores it in first_address
        last_name = column[1]  # get last name and stores it in last_name
        line = ([column[0]+' '+column[1], first_address, column[3], int(column[3])-199]) # gets the line of the file

        if ((int(column[3])) >= 200 or last_name.find('e') != -1 or last_name.find('l') != -1):  #decids which list to put the information in
            list1.append(line)  # puts in the list1 containing suspicous activity
        else:
            list2.append(line)  # puts in the list2 containing not suspicous activity

    read_file.close()                  # close the file

    return list1, list2    #return the two list


def create_file(file2, list1, list2):     # The create_file Function takes in the file name you want to create and writes in the suspicous list

    with open(file2, 'w', newline='') as write_file:     # create the file with the file name given and make it a write file and stores it in write_file
      writer = csv.writer(write_file)                     # write in the file and stores it in writer

      header = ['Name', 'First IP Address', 'Login_Count', 'Login_Count_Excess']   # header for the columns in the writer file
      writer.writerow(header)       # write the header in the writer file

      counter = 0        # count the number of employee with suspicious accounts
      print('    Suspicious Employee Accounts Table:')     # title of the table for the following output to the console
      print("{:<25} {:<25}".format('    Name', 'Login Attempts'))    # headers for the following output to the console
      print("-" * 45)   # dash to separate the header and the account info

      for column in list1:   # loops of the input file and reads it line at a time
        writer.writerow(list1[counter])  # writes the following output to the output file from the first input file
        counter = counter +1  #increments hte counter
        print("{:<30} {:<35}".format(column[0], column[2])) # prints the name and logins

    print("-" * 45); # separate the table of list and the total number of employee outputted
    print('\ntotal number of employees with suspicious logins attempts:', counter)   # prints total number of employees with suspicious login
    print('total number of employees with not suspicious logins attempts:', len(list2)) #prints the total number of employees with less suspicious logins
    write_file.close()   # closes the write file

def main():  # the Main Function that call the read_data function and the create_file function
    list1 = [] #empty list to store the suspicious logins
    list2 = [] # empty list to store the less suspicious logins
    data_log ='employee_logins.csv'  # the first imported file to be read from
    suspicious_log ='PondW1_Lab4.csv'  # the second imported file to be created

    read_data(data_log, list1, list2)         # calling the read_data Function passing the data_log as the parameter for the function
    create_file(suspicious_log, list1, list2)     # calling the create_data Function passing the data_log and suspicious_log as the parameters for the function

main()