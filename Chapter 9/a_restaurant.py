# 9.1 RESTAURANT

class Restaurant:
    """A class that models different Restaurant types"""

# CONSTRUCTOR
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes an instance of Restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


# METHODS
    def describe_restaurant(self):
        """Print description of restaurant incl. name & cuisine type"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} delicacies!")


    def open_restaurant(self):
        """Indicates that restaurant is now open."""
        print(f"{self.restaurant_name} is now open for business.")

# INSTANTIATE INSTANCE OF CLASS
restaurant_1 = Restaurant("Chicken Licken", "Chicken")

print(" --- Accessing Attributes ---")
print(f"The restaurant name is: {restaurant_1.restaurant_name}")
print(f"They serve: {restaurant_1.cuisine_type}")

print("\n --- Method Calls ---")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# ------------------------------------------------------------------------------

# 9.3 THREE RESTAURANTS
restaurant_2 = Restaurant("Saints", "Continental")
restaurant_3 = Restaurant("Gemelli", "Italian")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
