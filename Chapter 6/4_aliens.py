# NESTING

# LIST OF DICTIONARIES
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# CHATGPT SUMMARY

# This Python code demonstrates how to store multiple dictionaries inside a list and 
# loop through them.

# Here’s what it does step by step:

# It creates three dictionaries — alien_0, alien_1, and alien_2 — each representing 
# an alien with two key–value pairs:

# 'color': the alien’s color (green, yellow, or red)

# 'points': the number of points the alien is worth (5, 10, or 15)

# These three dictionaries are then stored together in a list called aliens.

# The for loop goes through each dictionary in the aliens list and prints it.

# ✅ In short:
# The code stores several alien records (as dictionaries) in a list and then 
# prints out each alien’s information one by one.

# -------------------------------------------------------------------------------------

# EXAMPLE 2

aliens = []
print("\n")

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

    for alien in aliens[:5]:
      print(alien)
      print("...")

print(f"Total number of aliens: = {len(aliens)}\n")

# CHATGPT SUMMARY

# This Python code demonstrates how to create a list of dictionaries using a loop and
# display part of it.

# Here’s what it does step by step:

# It starts with an empty list called aliens.

# Using a for loop with range(30), it creates 30 alien dictionaries — each with:

# "color": "green"

# "points": 5

# "speed": "slow"

# Each newly created dictionary (new_alien) is added to the aliens list using append().

# Inside the loop, it prints the first 5 aliens (aliens[:5]) and shows "..." after each 
# one (though this printing part should normally be placed outside the main loop to 
# avoid repetition).

# After the loop finishes, it prints the total number of aliens using len(aliens).

# ✅ In short:
# The code creates 30 identical alien dictionaries, stores them in a list, prints 
# a few examples, and then shows the total count of aliens.

# --------------------------------------------------------------------------------------

# EXAMPLE 3

aliens = []
print("\n")

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

print("\nGreen to Yellow")

for alien in aliens[:3]:
        if alien["color"] == "green":
            alien["color"] = "yellow"
            alien["speed"] = "medium"
            alien["points"] = 10

        elif alien['color'] == 'yellow':
             alien['color'] = 'red'
             alien['speed'] = 'fast'
             alien['points'] = 15    

for alien in aliens[:5]:
    print(alien)

# CHATGPT SUMMARY

# This Python code demonstrates how to create, modify, and display a collection 
# of dictionaries stored in a list.

# Here’s what it does step by step:

# It starts with an empty list called aliens.

# A for loop runs 30 times (range(30)), and during each iteration, 
# it creates a new alien dictionary with:

# "color": "green"

# "points": 5

# "speed": "slow"

# Each alien is then added to the aliens list.

# After creating the aliens, the code prints "Green to Yellow" to indicate an
# update process.

# The next for loop modifies the first three aliens in the list:

# If an alien’s color is "green", it changes to:

# "color": "yellow"

# "speed": "medium"

# "points": 10

# If an alien’s color is "yellow", it changes again to:

# "color": "red"

# "speed": "fast"

# "points": 15

# Finally, the code prints the first five aliens to show the updated values.

# ✅ In short:
# The code creates 30 green aliens, updates the first three to yellow (and adjusts
# their speed and points), and then prints the first five aliens to display the changes.

