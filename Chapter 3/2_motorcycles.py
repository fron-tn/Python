# Modifying Elements In A List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# APPENDING AN ELEMENT TO THE END OF A LIST METHOD
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print("\n")
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("\n")
# INSERTING ELEMENTS INTO A LIST
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.insert(3, "ducati")
print(motorcycles)

# REMOVING AN ITEM USING DEL STATEMENT
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[1]
print(motorcycles)

print("\n")

# REMOVING AN ITEM USING THE POP() METHOD
motorcycles = ["honda", "yamaha", "suzuki"]

popped_motorcycles = motorcycles.pop()
print(f"Popped Motorcycle = {popped_motorcycles}\nNew List = {motorcycles}")

print("\n")

# POPPING ITEMS FROM ANY POSITION IN OUR LIST
motorcycles = ["honda", "yamaha", "suzuki"]

second_owned = motorcycles.pop(1)
print(f"The second motorcycle I owned was a {second_owned.title()}")

# REMOVING AN ITEM BY VALUE
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.\nMy current wish list is now: {motorcycles}")