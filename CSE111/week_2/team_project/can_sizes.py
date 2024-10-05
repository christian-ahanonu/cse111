# team project
'''Program must compute the volume of all 12 can sizes.
Program must compute the surface area of all 12 can sizes.
Program must compute and print the storage efficiency of all 12 can sizes. '''
#Global Variables Here--V
import math


def main(): # main area of storing code
    # name = input("Can Name: ")
    # radius = float(input("radius of the can (cm): ")) 
    # height = float(input("height of the can (cm): "))
    # price = float(input("Cost per can (USD): "))
    can_info = {
        '#1 Picnic':{'radius':6.83,'height':10.16,'cost':0.28},
        '#1 Tall':{'radius':7.78,'height':11.91,'cost':0.43},
        '#2':{'radius': 8.73, 'height' : 11.59, 'cost':0.45},
        '#2.5':{'radius':10.32,'height':11.91,'cost':0.61},
        '#3 Cylinder':{'radius':10.79,'height':17.78,'cost':0.86},
        '#5':{'radius':13.02,'height':14.29,'cost':0.83},
        '#6Z':{'radius':5.40,'height':8.89,'cost':0.22},
        '#8Z short':{'radius':6.83,'height':7.62,'cost':0.26},
        '#10':{'radius':15.72,'height':17.78,'cost':1.53},
        '#211':{'radius':6.83,'height':12.38,'cost':0.34},
        '#300':{'radius':7.62,'height':11.27,'cost':0.38}, 
        '#303':{ 'radius':8.10,'height':11.11,'cost':0.42},
    }

    length = len(can_info)
    keys = list(can_info.keys())
    best_storage = 0.0
    best_cost = 0.0

    for i in range(0,length):
        volume = compute_volume(can_info[keys[i]]['radius'],can_info[keys[i]]['height'])

        surface_area = compute_surface_area(can_info[keys[i]]['radius'],can_info[keys[i]]['height'])

        storage_efficiency = compute_storage_efficiency(volume= volume,surface_area = surface_area)

        if storage_efficiency > best_storage:
            best_storage = storage_efficiency
            
        cost_efficiency = compute_cost_efficienty(volume= volume,cost= can_info[keys[i]]['cost'])
        if cost_efficiency > best_cost:
            best_cost = cost_efficiency
        print(f"{keys[i]} {storage_efficiency:.2f}")

    
    
def compute_volume(radius,height): # Calculate the volume
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height): # calculate the surface area
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_eff = volume / surface_area
    return storage_eff

def compute_cost_efficienty(volume,cost):
    return volume/cost

# Call the main function so that
# this program will start executing.
main()




## ***sample code***
# import math


# def main():
#     # Four parallel lists, one list for each attribute of the cans.
#     can_names = [
#         "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
#         "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
#     ]
#     can_radiuses = [
#         6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
#         5.4, 6.83, 15.72, 6.83, 7.62, 8.1
#     ]
#     can_heights = [
#         10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
#         8.89, 7.62, 17.78, 12.38, 11.27, 11.11
#     ]
#     can_costs = [
#         0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
#         0.22, 0.26, 1.53, 0.34, 0.38, 0.42
#     ]

#     best_store = None
#     best_cost = None
#     max_store_eff = -1
#     max_cost_eff = -1

#     # For each can in the parallel lists, unpack the values
#     # into the variables name, radius, height, and cost.
#     for i in range(len(can_names)):
#         name = can_names[i]
#         radius = can_radiuses[i]
#         height = can_heights[i]
#         cost = can_costs[i]

#         # Call the compute_storage_efficiency and
#         # compute_cost_efficiency functions.
#         store_eff = compute_storage_efficiency(radius, height)
#         cost_eff  = compute_cost_efficiency(radius, height, cost)

#         # Print the can size name, storage
#         # efficiency, and cost efficiency.
#         print(f"{name} {store_eff:.2f} {cost_eff:.0f}")

#         # If the storage efficiency of the current can size is
#         # greater than the maximum storage efficiency, save then
#         # the current can size name and its storage efficiency.
#         if store_eff > max_store_eff:
#             best_store = name
#             max_store_eff = store_eff

#         # If the cost efficiency of the current can size is
#         # greater than the maximum cost efficiency, then save
#         # the current can size name and its cost efficiency.
#         if cost_eff > max_cost_eff:
#             best_cost = name
#             max_cost_eff = cost_eff

#     # Print the best storage and cost efficiencies.
#     print()
#     print("Best can size in storage efficiency:", best_store)
#     print("Best can size in cost efficiency:", best_cost)


# """Here is another solution. This solution organizes the data about
# the cans in a compound list. A compound list is a list that contains
# lists. CSE 111 students study lists and compound lists in lesson 7.

# def main():
#     # A compound list (a list that contains lists).
#     can_sizes = [
#         ["#1 Picnic", 6.83, 10.16, 0.28],
#         ["#1 Tall", 7.78, 11.91, 0.43],
#         ["#2", 8.73, 11.59, 0.45],
#         ["#2.5", 10.32, 11.91, 0.61],
#         ["#3 Cylinder", 10.79, 17.78, 0.86],
#         ["#5", 13.02, 14.29, 0.83],
#         ["#6Z", 5.4, 8.89, 0.22],
#         ["#8Z short", 6.83, 7.62, 0.26],
#         ["#10", 15.72, 17.78, 1.53],
#         ["#211", 6.83, 12.38, 0.34],
#         ["#300", 7.62, 11.27, 0.38],
#         ["#303", 8.1, 11.11, 0.42]
#     ]

#     best_store = None
#     best_cost = None
#     max_store_eff = -1
#     max_cost_eff = -1

#     # For each can in the can_sizes list, unpack the values
#     # into the variables name, radius, height, and cost.
#     for name, radius, height, cost in can_sizes:
#         .
#         .
#         .
# """


# def compute_storage_efficiency(radius, height):
#     """Compute and return the storage efficiency of a steel can size.
#     The storage efficiency is the volume of the can divided by its
#     surface area.

#     Parameters
#         radius: the radius of the steel can
#         height: the height of the steel can
#     Return: the storage efficiency of the steel can
#     """
#     volume = compute_volume(radius, height)
#     surf_area = compute_surface_area(radius, height)
#     efficiency = volume / surf_area
#     return efficiency


# def compute_cost_efficiency(radius, height, cost):
#     """Compute and return the cost efficiency of a steel can size.
#     The cost efficiency is the volume of the can divided by its cost.

#     Parameters
#         radius: the radius of the steel can
#         height: the height of the steel can
#         cost: the cost of the steel can
#     Return: the cost efficiency of the steel can
#     """
#     volume = compute_volume(radius, height)
#     efficiency = volume / cost
#     return efficiency


# def compute_volume(radius, height):
#     """Compute and return the volume of a cylinder.

#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: the volume of the cylinder
#     """
#     volume = math.pi * radius**2 * height
#     return volume


# def compute_surface_area(radius, height):
#     """Compute and return the surface area of a cylinder.

#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: the surface area of the cylinder
#     """
#     surf_area = 2 * math.pi * radius * (radius + height)
#     return surf_area


# # Start this program by
# # calling the main function.
# main()