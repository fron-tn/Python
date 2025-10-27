# PASSING A LIST

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "Tayo", "Darell"] 
greet_users(usernames) 

print(usernames)