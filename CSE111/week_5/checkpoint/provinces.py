print()

provinces_list = []

with open('.\week_5\checkpoint\provinces.txt', 'rt') as provinces_file:

    # Read the contents of the file into a list where each 
    # line of text in the file is stored in a separate element 
    # in the list.
    for item in provinces_file:

        provinces_list.append(item.strip())

# remove first and last element in the list 
provinces_list = provinces_list[1:-1]

# replace 'AB' with 'Alberta'
for i in range(len(provinces_list)):
    provinces_list[i] = provinces_list[i].replace('AB', 'Alberta')

# count how many times 'Alberta' appear in the list 
count_alberta = provinces_list.count('Alberta')

print(f'Alberta occurs {count_alberta} times in the modified list')
# print(provinces_list)
































print()