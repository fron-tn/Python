class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   #set default value for attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()
    

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"\nThis car has {self.odometer_reading} miles on it.")


# MODIFYING ATTRIBUTE VALUE THRU A METHOD
    def update_odometer(self, mileage):
        """Set odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

# INCREMENT ATTRIBUTE VALUE THRU METHOD
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# instantiate car object
my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# MODIFYING ATTRIBUTES VALUE DIRECTLY
my_new_car.odometer_reading = 20
my_new_car.read_odometer()


# MODIFY ATTRIBUTE VALUE THRU A METHOD
my_new_car.update_odometer(100)
my_new_car.read_odometer()

print("\n=========================================")
# INCREMENT ATTRIBUTE VALUE THRU METHOD
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

print("\nUpdate Function")
my_used_car.read_odometer()
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


print("\nIncrement Function")
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()