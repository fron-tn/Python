#  USING WHILE LOOPS IN LISTS AND DICTIONARIES
# MOVING ITEMS FROM ON LIST TO ANOTHER

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
 current_user = unconfirmed_users.pop()

 print(f"Verifying user: {current_user.title()}")
 confirmed_users.append(current_user)

print("\nThe following users have been comfirmed:")
for confirmed_user in confirmed_users:
 print(f"- {confirmed_user.title()}")

#  CHATGPT SUMMARY 

# This Python code shows how to process items from one list and move them 
# to another using a while loop.

# Here’s what it does:

# Two lists are defined:

# unconfirmed_users: contains users waiting to be verified ('alice', 'brian', 'candace').

# confirmed_users: starts empty and will store verified users.

# The while unconfirmed_users: loop runs as long as there are still names in 
# unconfirmed_users.

# It removes (pop()) the last user from the list and assigns it to current_user.

# Prints a message showing that this user is being verified.

# Adds (append()) the verified user to the confirmed_users list.

# After all users are processed, it prints a summary listing all the verified users.

# ✅ In short:
# The code simulates verifying users by moving each one from the unconfirmed list 
# to the confirmed list and then printing the names of all confirmed users.

# --------------------------------------------------------------------------------------------

# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"\nOriginal List: \n{pets}")

while "cat" in pets:
    pets.remove("cat")
    print(f"- {pets}")

print(f"\nUpdated List: \n{pets}")

# CHATGPT SUMMARY

# This Python code shows how to remove all occurrences of a specific
# item from a list using a while loop.

# Here’s how it works:

# A list named pets is created with several animal names — some repeated (like "cat").

# It first prints the original list.

# The while loop checks if "cat" is still in the list:

# If "cat" is found, it removes one occurrence using pets.remove("cat").

# After each removal, it prints the current state of the list.

# Once all "cat" entries are gone, the loop stops.

# Finally, it prints the updated list without any "cat" entries.

# ✅ In short:
# The code removes every "cat" from the list and shows the list’s changes after 
# each removal.


#----------------------------------------------------------------------------------------

# FILLING DICTIONARY WITH USER INPUT

responses = {}

polling_active = True

while polling_active:
 name = input("What is your name? ")
 response = input("Whcih mountain would your like to climb someday? ")

 responses[name] = response

 repeat = input("Would you like to let another person respond? (Yes/No) ")
 if repeat == "no":
  polling_active = False

  print("\n ---- Poll Results ----")
  for name, response in responses.items():
   print(f"- {name.title()} would like to climb {response}")


# CHATGPT SUMMARY

# This Python code is a simple polling program that collects user responses in a loop.

# Creates an empty dictionary responses to store each person’s answer.

# The person’s name is used as the key.

# The mountain they want to climb is the value.

# Starts a while loop controlled by the variable polling_active (set to True).

# Inside the loop:

# It asks for the user’s name.

# Then asks which mountain they would like to climb.

# Stores this data in the responses dictionary.

# Asks if another person should respond.

# If the user types "no", the loop stops (polling_active = False).

# After polling ends, it prints the results:

# Loops through the responses dictionary.

# Displays each person’s name and the mountain they chose.

# ✅ In short:
# This code repeatedly asks different users which mountain they’d like to climb, 
# stores their answers, and finally prints a summary of all responses.