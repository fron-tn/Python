# IF STATEMENTS

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?\n")
    

# IF-ELSE STATEMENT
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?\n")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")
    
    
    
# IF-ELIF-ELSE STATEMENT
# Option 1
age = 12

if age < 4:
    print("Your admission cost is R0")
elif age < 18:
    print("Your admission cost is R25")
else:
    print("Your admission cost is R40")

# Option 2
age = 80
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
    
print(f"Your admission cost is R{price}\n")


# TEST MULTIPLE CONDITIONS
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
    
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
    
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!\n")


# IF STATEMENTS WITH LISTS
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
        
print("\nFinished making your pizza!")


# CHECKING LIST IS NOT EMPTY
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")


# USING MULTIPLE LISTS
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
     else:
        print(f"Sorry, we don't have {requested_topping}.")
        
print("\nFinished making your pizza!")