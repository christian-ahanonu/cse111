# Week 1 Team Activity Solution

# I'll be using if statements at some point 
# deduct sales tax of 6% from subtotal after discount has been removed 

from datetime import datetime

print()

# Ask the user to enter a subtotal amount
subtotal = float(input('Please enter the subtotal: '))

cur_date_and_time = datetime.now()
weekday = cur_date_and_time.weekday()
# day_of_week = 2

disc_rate = 0.10 # Calculate the discount
sales_tax_rate = 0.06 # Calculate the sales tax


# Amount >= 50 and day of week equal Tuesday or wednesday,
# compute discount amount
if subtotal >= 50 and (weekday == 1 or weekday == 2):

    discount = subtotal * disc_rate    
    print(f'Discount amount: {discount:.2f}')
    subtotal -= discount


# Compute sales tax
sales_tax = sales_tax_rate * subtotal
print(f'Sales tax amount: {sales_tax:.2f}')

# Compute total amount
print(f'Total: {sales_tax + subtotal:.2f}') 


print()