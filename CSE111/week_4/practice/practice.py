print()

# DICTIONARIES 
bad_guys = {
    'daredevil' : 'kingpin',
    'x-men' : 'apocalypse',
    'batman' : 'bane'
}

# first_line = bad_guys['x-men']
# print(first_line)

bad_guys['deadpool'] = 'evil pool' # add to the dictionary
bad_guys['x-men'] = 'x-woman' # replace apocalypse with x-men
del bad_guys['batman'] # delete batman from the dictionary


# print(bad_guys)




# LIST 
shopping = ['books', 'rice', 'beans', 'cornflakes', 'garri']

shopping.append('Cway water') # add Cway water to the end of the list
shopping.insert(0, 'Jenga') # add Jenga at the beginning of the list

# replace 'rice' with 'sugar cane'
rice_ind = shopping.index('rice')
shopping[rice_ind] = 'sugar cane'

shopping.pop(0)
shopping.remove('books')

# print(shopping)


# LIST CONT'D
randoms = ['office', 'crayon', 'decision', 'officer']
cheta = []

randoms[0] = 'air conditioner' # change 'office' to 'air conditioner'
length =  len(randoms) # find the length of a list 

for item in randoms:

    randoms.insert(0, 'gabriel')

    # print(randoms)
    # print(item)
    break


# number = range(0, 10)
# print(number)


# print(random)
# print(length)


compound = [
    ['sugar', 'tomato', 'gas', 'beans', 12],
    ['light bulb', 'chainsaw', 'solar light', 'mop', 37],
    ['cane', 'crane', 'stick', 'bottle', 87],
    ['stone', 'morrow', 'coffin', 'show', 98]
]

# first_line = compound[0]
# toma = first_line[1]
# print(toma)

column = 4
total = 0

for i in compound:

    all_line = i[column]

    total += all_line

print(f'The total is: {total}')

















print()