#  numberical comparisons

age = 18
print(f"Is the person 18years old?: {age == 18}")

age = 21
print(f"\nIs the person below 21years old?: {age < 21}")
print(f"\n Is the person 21 years or younger?: {age <= 21}")

print(f"\n Is the person above 21 years of age?: {age > 21}")
print(f"\n Is the person atleast 21 years of age?: {age >= 21}")

# CHECKING MULTIPLE CONDITIONS
# 1) USING AND OPERATOR 

age_0 = 22
age_1 = 18

admission = age_0 >= 20 and age_1 >=16

print(f"\n Are both patrons allowed to purchase?: {admission}")

# USING OR OPERATOR

age_0 = 16
age_1 = 18

admission = age_0 >= 21 or age_1 >= 21
print(f"\n Can they enter the movie theatre?: {admission}")

# CHECKING WHETHER A VALUE IS IN A LIST
requested_toppings = ["mushrooms", "onions", "pineapple"]
print(f'\nAdd mushrooms for order?: {"mushrooms"}' in requested_toppings)

print(f"\nAdd pepperoni for order?: {"pepperoni"}" in requested_toppings)

# CHECKING WHETHER A VALUE IS IN A LIST
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish")



