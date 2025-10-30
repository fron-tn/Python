# importing classes

# importing a single class
from car_module import Car

my_new_car = Car("audi", "bmw", 2025)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()