# Import math module to use the math.pi function
import math 

print()

# Get the width, diameter and aspect ratio from the user 
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))
 
bracket = width * aspect_ratio + 2540 * diameter # work on the bracket first
numerator = math.pi * width**2 * aspect_ratio * (bracket) # combine the bracket with the remaining top value
denominator = numerator / 10000000000 # divide the numerator with the denominator

volume = denominator 

# print the result
print("\n"f'The approximate volume is {volume:.2f} liters')

print()

# Import the date and time module to use the date and time function
from datetime import datetime

# Use the datetime.now() method to get the current date and time from OS
cur_date_and_time = datetime.now() 

with open("volumes.txt", "at") as volumes_file:

    print(f'{cur_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}', file=volumes_file)


    # Exceed Requirement
    '''After your program prints the tire volume to the terminal window, your program should 
    ask the user if she wants to buy tires with the dimensions that she entered. 
    If the user answers “yes”, your program should ask for her phone number and 
    store her phone number in the volumes.txt file.'''

    buy_tires = input('Would you like to buy tires with the same dimension (Yes/No): ').lower()

    if buy_tires == "yes":

        phone_no = input('Please enter your phone number: ')
        print(f'{phone_no}', file=volumes_file)

        print()

    else:
        print("Thank you! Have a great day.")


print()

