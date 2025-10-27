# DICTIONARY WITHIN A DICTIONARY

users = {
'einstein101': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},

'smoking101': {
'first': 'smoking',
'last': 'guap',
'location': 'jhb',
},
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"- Full name: {full_name.title()}")
    print(f"- Location: {location.title()}")


# CHATGPT SUMMARY
# Each key in the users dictionary (like 'einstein101' or 'smoking101') is a username.

# Each value is another dictionary containing details about that user — specifically their 'first' name, 'last' name, and 'location'.

# Then, the for loop:

# Goes through each user in the dictionary using .items().

# Prints the username.

# Combines the user’s first and last names into a full name.

# Prints the user’s full name (with title case formatting) and location (also in title case).

# ✅ In short:
# The code loops through a list of users and neatly prints each user’s username, full name, and location.