# SORTING LIST IN ALPHABTETIC ORDER USING THE SORT() METHOD
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# SORTING LIST TEPORARILY USING SORT() METHOD
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original List: {cars}")

print(f"1)Sorted List: {sorted(cars)}")

print(f"After Sorted Method: {cars}")

sorted_cars = sorted(cars, reverse=True)

print(f"2) Sorted List: {sorted_cars}")

# PRITING A LIST IN REVERSE ORDER
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original List: {cars}")

cars.reverse()
print(f"Reversed List = {cars}")

# FINDING THE LENGTH OF A LIST
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Length of cars in list = {len(cars)}")