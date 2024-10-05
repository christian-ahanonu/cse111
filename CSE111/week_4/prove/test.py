'''This function iterates over each element in the symbol_quantity_list, 
    retrieves the atomic mass for each element from the periodic_table_dict, 
    multiplies it by the quantity, and accumulates the result into total_molar_mass. 
    Finally, it returns the total molar mass.'''


total_molar_mass = 0.0
    # Iterate through each element in the symbol_quantity_list
    for symbol, quantity in symbol_quantity_list:
        # Get the atomic mass for the symbol from the periodic_table_dict
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        # Multiply the atomic mass by the quantity and add it to the total
        total_molar_mass += atomic_mass * quantity
    
    return total_molar_mass
    
# Example usage:
# symbol_quantity_list = [["H", 2], ["O", 1]]
# periodic_table_dict = {"H": ["Hydrogen", 1.00794], "O": ["Oxygen", 15.9994]}
# print(compute_molar_mass(symbol_quantity_list, periodic_table_dict))

