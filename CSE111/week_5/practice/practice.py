print()

import csv

dictionary_info = {}

with open(".\week_5\content.csv", 'rt') as info_file:

    reader = csv.reader(info_file)

    next(reader)

    for row_list in reader:
        
        if len(row_list) != 0:
            
            key = row_list[2]
            dictionary_info[key] = row_list
            # print(row_list)





print(dictionary_info)

print()