#!/usr/bin/python3


def get_and_validate_talk_time():  # function that get data from the user

    # get the plan type
    plan_type = input("Enter the plan type [s, S, r, R, c, C]:\n")
    correct_types = {"s", "S", "r", "R", "c", "C"}

    while plan_type not in correct_types:
        # ask for the correct plan type
        plan_type = input("Enter the plan type [s, S, r, R, c, C]:\n")

    while True:  # get the minutes from the user
        user_input = input("Enter the number of minutes talked this week between 0 and 10080 minutes\n")
        try:
            minutes = int(user_input)
            while not 0 <= minutes <= 10080:  # validate the minutes
                minutes = input("Enter the number of minutes talked this week between 0 and 10080 minutes\n")
            break  # Exit the loop if the input is a valid number
        except ValueError:
                print("Invalid input. Please enter an integer")

    return minutes, plan_type

def calculate_talk_time(plan_type, minutes):      #Function to calculate the blance

    amount = 0   # declare variable

    if plan_type == "s" or plan_type == "S":  # plan_type Student calculation
        amount = minutes * 0.15 - 25.00
    elif plan_type == "c" or plan_type == "C":  # plan_type Commercial calculation
        if minutes <= 300:
            amount = minutes * 0.20 - 25.00
        else:
            amt_1 = (300 * 0.20) - 25.00
            amt_2 = (minutes - 300) * 0.10
            amount = amt_1 + amt_2

    elif plan_type == "r" or plan_type == "R":  # plan_type Residential calculation
        if minutes <= 120:
            amount = minutes * 0.10 - 25.00
        else:
            amt_1 = 120 * 0.10
            amt_2 = (minutes - 120) * 0.05
            amount = amt_1 + amt_2 - 25.00

    return amount

def main():   # The main function that uses the get_and_validate_talk_time() and the calculate_talk_time(plan_type, minutes) to print the customer info

    customers = []   #array created
    customer_id = 0
    next_customer = input("Would you like to enter customer information yes/no:\n")

    while next_customer == "yes":  # a while loop that uses the fuction above to get the information and store it in the array

        customer_id = customer_id + 1
        minutes, plan_type = get_and_validate_talk_time()
        amount = calculate_talk_time(plan_type, minutes)
        customer_info = {"ID": customer_id, "Minutes used": minutes, "Plan type": plan_type, "Amount": amount}

        customers.append(customer_info)
        next_customer = input("Would you like to enter customer information yes/no:\n")
        if next_customer != "yes":  # break out of the while loop when user doesn't type yes
            break

    print("                    Customer Data Table:")   # table title
    print("{:<15} {:<15} {:<15} {:<15}".format("Customer ID", "Plan Type", "# minutes", "Amount Due/Credit"))  # print format and labels for each column
    print("-" * 65)


    for customer_dictionary in customers:  # created a dictionary to store the customer info

        customer_id = customer_dictionary["ID"]
        plan_type = customer_dictionary["Plan type"]
        minutes_used = customer_dictionary["Minutes used"]
        amount = customer_dictionary["Amount"]

        print("{:^12} {:^15} {:^15} {:^21.2f}".format(customer_id, plan_type, minutes_used, amount))  # print format and displaying output for each customer


main()   # calling the main fuction to execute and run it