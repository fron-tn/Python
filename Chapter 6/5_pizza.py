# LIST IN DICTIONARY
# EXAMPLE 1
pizza = {
    "crust" : "thick",
    "toppings" : ["mushroom", "extra cheese"]
    }

print(f"You ordered a {pizza["crust"]} crust pizza with the following toppings")

for topping in pizza["toppings"]:
    print(f"\t- {topping}")


# CHATGPT SUMMARY

# This code shows two examples of how to work with dictionaries and lists in Python.

# A dictionary named pizza stores information about an order:

# "crust": the type of crust ("thick")

# "toppings": a list of toppings (["mushroom", "extra cheese"])

# It prints a message describing the pizza.

# Then it loops through the list of toppings and prints each one with a dash (-).

# In short:
# It displays the type of crust and all the toppings for the pizza order.
    


# EXAMPLE 2
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f" - {language.title()}")

# CHATGPT SUMMARY

# A dictionary named favorite_languages stores people’s favorite programming languages.

# Each key (like 'jen' or 'phil') is a person’s name.

# Each value is a list of that person’s favorite languages.

# The code loops through each person and their languages, printing:

# The person’s name.

# Each language in their list (formatted nicely with a dash).

# In short:

# It prints each person’s name along with all their favorite programming languages.