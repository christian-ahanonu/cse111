'''For the exceed requirement portion I wrote a code 
at the bottom of the receipt inviting customers to complete
an online survey'''

print()

from csv import reader
from datetime import datetime

def main():
    try:    
        products_dict = read_dictionary('.\week_5\prove\products.csv', 0)
        # print(products_dict)
        

        with open ('./week_5/prove/request.csv', 'rt') as request_file:
            request_list = reader(request_file)
            next(request_list) # skip the header in the request_list csv file 
            
            print('German Outlet\n')
            
            No_of_items = 0
            subtotal = 0
            qty_x_price = 0

            # read the request.csv file 
            for row in request_list:

                product_no = row[0]
                quantity = int(row[1])

                if product_no in products_dict:

                    pro_info = products_dict[product_no]
                    pro_name = pro_info[1]
                    pro_price = float(pro_info[2])

                    print(f'{pro_name}: {quantity} @ {pro_price}')
                else:
                    print(f'Product: {product_no} not found.')

            No_of_items += quantity

            qty_x_price = quantity * pro_price

            subtotal += qty_x_price
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax
        
        print()

        print(f'Number of Items: {No_of_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}') 

        print()

        print('Thank you for shopping at German Outlet!')

        # Exceed Requirement
        print('We value your feedback. Kindly take our survey.\n')

        current_date_and_time = datetime.now()

        print(f'{current_date_and_time:%a %b %d %Y, %I:%M %p}')
        print()

    except KeyError as key_error:
        print(type(key_error).__name__, key_error, sep=": ")
        print(f'Error: unknown product ID in the request.csv file'
              ' "R002"')

    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"Error: missing file {'./week_5/prove/products.csv'}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"Error: cannot read from {'./week_5/prove/product.csv',}"
                " because you don't have permission.")


            

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as pro_file:

        product_dict = reader(pro_file)
        next(product_dict)


        for row_list in product_dict:
            
            if len(row_list) != 0:
                
                key = row_list[key_column_index]

                dictionary[key] = row_list
    
    return dictionary




if __name__ == '__main__':
    main()

print()