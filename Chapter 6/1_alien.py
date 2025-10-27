# SIMPLE DICTIONARY
alien_0 = {'color': 'green', 'points': 5}

print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"\nYou just earned {new_points} points!")

# CHATGPT SUMMARY

# This Python code demonstrates how to access and use values stored in a dictionary.

# Here’s a breakdown of what it does:

# A dictionary named alien_0 is created with two key–value pairs:

# 'color': 'green'

# 'points': 5

# The first two print() statements access and display the values for 'color' and 'points':

# green
# 5


# The code then stores the 'points' value (5) in a variable called new_points.

# Finally, it prints a formatted message using that variable:

# You just earned 5 points!


# ✅ In short:
# This code retrieves specific values from a dictionary and uses them in a message. 
# It shows how to access dictionary data and use it dynamically in your program.

# --------------------------------------------------------------------------------------

# ADDING NEW KEY-VALUE PAIRS
alien_0 = {'color': 'green', 'points': 5}
print(f"Original Dictionary: \n{alien_0}")

alien_0["x_psition"] = 0
alien_0["y_position"] = 25
print(f"\nUpdated Dictionary: \n{alien_0}")

# CHATGPT SUMMARY

# This Python code shows how to add new key–value pairs to a dictionary.

# Here’s what happens step by step:

# A dictionary named alien_0 is created with two key–value pairs:

# {'color': 'green', 'points': 5}


# The first print() statement displays the original dictionary.

# Two new key–value pairs are then added:

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25


# This expands the dictionary by giving the alien an x and y position.

# The second print() statement displays the updated dictionary, now showing:

# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}


# ✅ In short:
# This code demonstrates how to start with a basic dictionary and then add new 
# information (new keys and values) to it dynamically.

# --------------------------------------------------------------------------------------

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# CHATGPT SUMMARY

# This Python code demonstrates how to create an empty dictionary and 
# add key–value pairs to it.

# Here’s what it does:

# alien_0 = {} creates an empty dictionary — it starts with no data.

# Two key–value pairs are then added one by one:

# alien_0['color'] = 'green'
# alien_0['points'] = 5


# This means:

# The key 'color' has the value 'green'.

# The key 'points' has the value 5.

# Finally, print(alien_0) displays the dictionary:

# {'color': 'green', 'points': 5}

# ✅ In short:
# The code builds a dictionary from scratch by adding new keys and values, 
# then prints the final result.

# -------------------------------------------------------------------------------------

# MODIFYING VALUES IN DICTIONARY
alien_0 = {'color': 'green'}
print(f"The alien was a {alien_0['color']} color")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# CHATGPT SUMMARY

# This Python code demonstrates how to modify the value of an existing key in a 
# dictionary.

# Here’s what it does:

# A dictionary alien_0 is created with one key–value pair:

# {'color': 'green'}


# The first print() statement displays the initial color of the alien:

# The alien was a green color


# The value of the 'color' key is then updated from 'green' to 'yellow':

# alien_0['color'] = 'yellow'


# The second print() statement shows the updated color:

# The alien is now yellow.


# ✅ In short:
# The code shows how to access a dictionary value, change it, and 
# confirm the change by printing it.

# --------------------------------------------------------------------------------------

#EXAMPLE 2
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# CHATGPT SUMMARY

# This Python code demonstrates how to access a value from a dictionary.

# Here’s what it does:

# A dictionary alien_0 is created with three key–value pairs:

# {'x_position': 0, 'y_position': 25, 'speed': 'medium'}


# The print() statement accesses the value associated with the key 'x_position' 
# and displays it:

# Original position: 0


# ✅ In short:
# The code retrieves and prints the x-coordinate of the alien from the dictionary.

# --------------------------------------------------------------------------------------

# MOVE ALIEN TO RIGHT ACCORDING TO SPEED
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 x_increment = 3

#  CHATGPT SUMMARY

# This Python code demonstrates how to use a dictionary value in conditional logic
# to determine a variable.

# Here’s what it does step by step:

# It checks the value of the 'speed' key in the alien_0 dictionary.

# Based on the speed, it assigns a different value to the variable x_increment:

# If the speed is 'slow', x_increment = 1

# If the speed is 'medium', x_increment = 2

# Otherwise (e.g., 'fast'), x_increment = 3

# ✅ In short:
# The code determines how much the alien should move along the x-axis depending
# on its speed.

# --------------------------------------------------------------------------------------

# output new x position of alien
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"\nNew X Position: {alien_0['x_position']}\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# CHATGPT SUMMARY

# This Python code demonstrates updating and deleting values in a dictionary.

# Here’s a step-by-step breakdown:

# Part 1: Updating a value
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"\nNew X Position: {alien_0['x_position']}\n")


# Updates the 'x_position' of alien_0 by adding x_increment to its current value.

# Prints the new x-coordinate of the alien.

# Part 2: Deleting a key–value pair
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)


# Creates a new dictionary alien_0 with keys 'color' and 'points'.

# Prints the full dictionary: {'color': 'green', 'points': 5}

# Deletes the 'points' key using del alien_0['points'].

# Prints the dictionary again, showing that 'points' has been removed: {'color': 'green'}

# ✅ In short:
# The code shows how to update a dictionary value dynamically and how to remove 
# a key–value pair from a dictionary.