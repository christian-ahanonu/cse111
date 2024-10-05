import math

def main():

    radius = 6.83
    height = 10.16
    
    storage_efficiency = compute_volume (radius, height) / compute_surface_area (radius, height)
    print(storage_efficiency)


def compute_volume (radius, height):
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area (radius, height):
    s_area = 2 * math.pi * radius * (radius + height)
    return s_area

main ()

