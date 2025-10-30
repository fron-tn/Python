# IMPORT SINGLE CLASS FROM MODULE

from car_module import ElectricCar

my_leaf = ElectricCar('nissan', "leaf", 2025)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()