
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
 print(f"\nKey: {key}")
print(f"Value: {value}")

# CHATGPT SUMMARY

# This Python code demonstrates how to loop through a dictionary and access 
# both its keys and values.

# Here’s what it does step by step:

# A dictionary named user_0 is created with three key–value pairs:

# 'username': 'efermi'

# 'first': 'enrico'

# 'last': 'fermi'

# The for loop

# for key, value in user_0.items():


# goes through each key–value pair in the dictionary.

# key stores the dictionary key (e.g., 'username')

# value stores the associated value (e.g., 'efermi')

# Inside the loop, it prints each key on one line and the corresponding value 
# on the next line.

# ⚠️ Note: In your code, the last print(f"Value: {value}") line is not indented, 
# so it runs after the loop, printing only the last value once. If it were indented, 
# it would correctly print all key–value pairs.

# ✅ In short:
# The code loops through a user dictionary and prints each key and its value — 
# but due to a small indentation issue, only the last value will display unless fixed.

# --------------------------------------------------------------------------------------

# EXAMPLE 2
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

print("\n")
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")

#  CHATGPT SUMMARY

# This Python code demonstrates how to loop through a dictionary and display each 
# key–value pair in a formatted sentence.

# Here’s what it does step by step:

# A dictionary named favorite_languages is defined, where:

# The keys are people’s names ('jen', 'sarah', 'edward', 'phil').

# The values are their favorite programming languages ('python', 'c', 'rust', 'python').

# The program prints a blank line (print("\n")) for cleaner output.

# The for loop

# for name, language in favorite_languages.items():


# goes through each person and their favorite language.

# Inside the loop, it prints a neatly formatted message using f-strings, capitalizing both 
# the person’s name and language with .title().

# ✅ In short:
# The code loops through a dictionary of people and their favorite programming languages, 
# printing each person’s name and preferred language in a readable sentence.

# --------------------------------------------------------------------------------------

# LOOPING THROUGH ALL KEYS IN DICTIONARY
for name in favorite_languages.keys():
 print(name.title())

print("\n")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
 
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")

  if name in friends:
   language = favorite_languages[name].title()
print(f"\tHey {name.title()}, I see you love {language}!")

print("\n")

if "erin" not in favorite_languages.keys():
 print("Erin please take our poll")

 print("\n")

#  CHATGPT SUMMARY

# This Python code demonstrates how to loop through dictionary keys, interact with 
# selected items, and check if a specific key exists.

# Here’s a step-by-step summary:

# The first loop:

# for name in favorite_languages.keys():
#     print(name.title())


# — Prints the names (keys) from the favorite_languages dictionary with the 
# first letter capitalized.

# Then the dictionary favorite_languages is defined again with four people and their 
# favorite languages.

# A list named friends (['phil', 'sarah']) is created — these are special users 
# the program will greet differently.

# The next loop:

# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\tHey {name.title()}, I see you love {language}!")


# — Greets every person.
# — If the person’s name is in the friends list, it also prints a personalized 
# message mentioning their favorite language.

# Finally, this condition:

# if "erin" not in favorite_languages.keys():
#     print("Erin please take our poll")


# — Checks if "erin" is not in the dictionary.
# — Since Erin isn’t listed, it invites her to take the poll.

# ✅ In short:
# The code prints all participants, gives extra messages to selected friends, and checks 
# if a specific person (Erin) has not taken the poll — 
# if not, it invites her to participate.

# --------------------------------------------------------------------------------------

 #LOOPING THRU DICTIONARY KEYS IN A PARTICULAR ORDER
 favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
 
 for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll")

print("\n")

# CHATGPT SUMMARY

# This Python code shows how to loop through a dictionary’s keys in alphabetical order 
# using the sorted() function.

# Here’s what it does step by step:

# A dictionary named favorite_languages is defined, storing people’s names (keys) 
# and their favorite programming languages (values).

# The for loop:

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll")


# Uses sorted() to arrange the dictionary’s keys (names) in alphabetical order.

# Prints a thank-you message for each person, with their name formatted in title case.

# Finally, it prints a blank line (print("\n")) to keep the output neat.

# ✅ In short:
# The code thanks each person from the dictionary for taking the poll, 
# displaying their names in alphabetical order.

# --------------------------------------------------------------------------------------

  # LOOPING THRU ALL VALUES IN A DICTIONARY
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
  
print("The following languages have been mentioned:")
for language in favorite_languages.values():
   print(language.title())

   print("\nUnique Values:")
   for language in set(favorite_languages.values()):
    print(language.title())

# CHATGPT SUMMARY

# This Python code demonstrates how to loop through dictionary values and 
# how to use a set to remove duplicates.

# Here’s what it does step by step:

# A dictionary named favorite_languages is defined, where each key is a person’s name 
# and each value is their favorite programming language.

# The first loop:

# for language in favorite_languages.values():
#     print(language.title())


# Goes through all the values (the programming languages).

# Prints each one with the first letter capitalized using .title().

# Since two people like Python, it will print “Python” twice.

# The next section:

# for language in set(favorite_languages.values()):
#     print(language.title())


# Converts the dictionary’s values into a set, which automatically removes duplicates.

# Prints each unique language only once.

# ✅ In short:
# The code first prints all mentioned languages (with duplicates), 
# then prints unique languages only using a set.
