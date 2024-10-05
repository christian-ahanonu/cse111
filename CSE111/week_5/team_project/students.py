print()

CSV_NAME = './week_5/team_project/students.csv'
from csv import reader

def main():
    students = read_dictionary(CSV_NAME)
    i_number = input("Enter an I-Number: ")
    dash = '-'

    if dash in i_number:
        dash.replace('-', '').strip()
    else:
        pass

    if len(i_number) < 9 or len(i_number) > 9:
        print("invalid number: must have the 9 digits")
    else:
        if i_number not in students:  
            print("No such Sudent.")
        else:
            print(f"Student Name: {students[i_number]}")

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    students = {}
    with open(filename,'rt') as file:
        students_list = reader(file)
        next(students_list)
        for i in students_list:
            students[i[0]] = i[1]
    return students

if __name__ == '__main__':
    main()













print()