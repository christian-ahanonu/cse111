
# Import the math function to use the math.ceil function
import math

print()

# Ask the user for the number of items and the number of items per box
items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

# Divide the number of items by the number of items per box
num_boxes = items / items_per_box

# Use import math to find the ceiling factor
ceil_factor = math.ceil(num_boxes) 


print(f'For {items} items, packing {items_per_box} items in each box, you will need {ceil_factor} boxes.')

print()