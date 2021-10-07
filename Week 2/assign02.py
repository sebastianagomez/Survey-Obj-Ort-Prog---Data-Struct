# 02 Prove : Assignment

# Stuent : Sebastian Gomez

# Instructor : Vaughn Poulson

# Write a Python 3 program to read from a .csv file containing rates from power companies. Your program should determine the average commercial rate, 
# and also display the information for the highest and lowest rates found.

import math

promt_filename = input("Please enter the data file: ")

# c:/Sebi/BYU/Fall 2021/CS241/home/cs241/assign02/rates.csv

with open(promt_filename) as f:                 # Open the .csv file and stored it in a variable "f"

    next(f)                                     # Read the first line for headers and do nothing

    # Set the values of the variables that are used to calculate the commercial rate and average
    highest_comercial_rate = -1
    lowest_comercial_rate = math.inf
    commercial_count = 0
    commercial_total = 0

    highest_utility_name = ""
    highest_zip = 0
    highest_state = ""

    lowest_utility_name = ""
    lowest_zip = 0
    lowest_state = ""

    for line in f:                               # Loop to read the whole file

        data = line.strip().split(",")           # Strip and Split the current line into its parts (comma "," is the separator)

        comm_rate = float(data[6])
        utility_name = data[2]
        zip = int(data[0])
        state = data[3]

        if comm_rate > highest_comercial_rate:   # If the current number is greater than the maximum that we already have
            highest_comercial_rate = comm_rate   # replace the maximum with the new data
            highest_utility_name = utility_name
            highest_zip = zip
            highest_state = state

        if comm_rate < lowest_comercial_rate:    # If the current number is less than the minimum that we already have 
            lowest_comercial_rate = comm_rate    # replace the minimum with the new data
            lowest_utility_name = utility_name
            lowest_zip = zip
            lowest_state = state

        commercial_count += 1                    
        commercial_total += comm_rate

commercial_average = commercial_total / commercial_count    # Formula for the comercial average 

print()
print(f"The average commercial rate is: {commercial_average}")
print()
print("The highest rate is:")
print(f"{highest_utility_name} {highest_zip, highest_state} - ${highest_comercial_rate}")
print()
print("The lowest rate is:")
print(f"{lowest_utility_name} {lowest_zip, lowest_state} - ${lowest_comercial_rate}")