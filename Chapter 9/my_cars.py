# IMPORTING MULTIPLE CLASSES FROM A MODULE

# from car_module import Car, ElectricCar

# my_mustang = Car("ford", "mustang", 2025)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar("nissan", "volvo", 2025)
# print(my_leaf.get_descriptive_name())

# ------------------------------------------------------------------------------------------

# Importing an entire module

# import car_module

# my_mustang = car_module.Car("ford", "mustang", 2025)
# print(my_mustang.get_descriptive_name())

# my_leaf = car_module.ElectricCar("nissan", "volvo", 2025)
# print(my_leaf.get_descriptive_name())


# =======================================================================================

# Importing all class from a module

from car_module import *