# INHERITANCE

# Parent Class/Superclass
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
            """Return a neatly formatted descriptive name."""
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()
            
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
        
    def fill_gas_tank(self):
        """Simulate filling up gas tank"""
        print("\nFilling up a gas tank")
        
# ==============================================================================
# ==============================================================================
# ==============================================================================

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nInside Battery class\nThis car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

# ==============================================================================
# ==============================================================================
# ==============================================================================

#Child class/Subclass
class ElectricCar(Car):
    """Represent aspets of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of parent class Car.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40 # Defining attributes and methods for child class
        self.battery = Battery()
    
    # Defining attributes and methods for child class
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nInside ElectricCar class\nThis car has a {self.battery_size}-kWh battery.")
     
        
    # Overriding methods from parent class   
    def fill_gas_tank(self): 
        """Electric cars don't have gas tanks."""
        print("\nThis car doesn't have a gas tank!")
        
        
        
# Create instance of childclass/subclass
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())


# Defining attributes and methods for child class
my_leaf.describe_battery()

# Overiding methods from parent class
my_leaf.fill_gas_tank()

# Instances as attributes
my_leaf.battery.describe_battery()

my_leaf.battery.get_range()


