# INPUT() FUNCTION

message =input("Tell me something and I will repeat it back to you:")
print(message)

# CHATGPT SUMMARY

# This Python code is a simple input and output example that echoes the user’s message.

# Here’s what it does:

# It uses input() to ask the user to type something.

# Whatever the user types is stored in the variable message.

# The program then prints that same message back to the screen using print(message).

# ✅ In short:
# The code takes user input and immediately repeats (displays) it back — 
# a basic example of reading and printing data in Python.
# --------------------------------------------------------------------------------------------

name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")

# CHATGPT SUMMARY

# This Python code is a simple greeting program that personalizes a message using 
# the user’s input.

# Here’s how it works step by step:

# The program asks the user to enter their name using input().

# The entered name is stored in the variable name.

# It then prints a greeting message — "Hello, [Name]!" — where:

# {name.title()} formats the name so that the first letter is capitalized.

# ✅ In short:
# The code asks for the user’s name and responds with a friendly, 
# properly formatted greeting.

# ---------------------------------------------------------------------------------------

prompt = "If you share your name, we can personalize the message you see"
prompt+= "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name.title()}")

# CHATGPT SUMMARY

# This Python code is a personalized greeting program that uses a multi-line input prompt.

# Here’s how it works step by step:

# A variable prompt stores a message explaining that sharing a name will personalize 
# the output.

# The += operator adds another line to the prompt asking for the user’s first name.

# The program then displays this full prompt and waits for user input using input(prompt).

# The entered name is stored in the variable name.

# Finally, it prints a friendly greeting — "Hello, [Name]" — with the name 
# formatted in title case (first letter capitalized).

# ✅ In short:
# The code politely asks for the user’s first name and 
# then prints a personalized hello message.

# ------------------------------------------------------------------------------------------

age = input("How old are you? ")
print(age)
print(type(age))

print("\n")

age = int(age)
print(type(age))

if age >= 18:
    print("Access Granted")


# CHATGPT SUMMARY 

# This Python code demonstrates how to get user input, convert data types, 
# and use a conditional statement.

# Here’s what it does step by step:

# It asks the user, "How old are you?", and stores the input in the variable age.

# It prints the entered value and its data type — which will be <class 'str'> (a string).

# Then it converts the string input to an integer using int(age) and
# prints the new data type (<class 'int'>).

# Finally, it checks if the user’s age is 18 or older using an if statement.

# If true, it prints "Access Granted".

# ✅ In short:
# The code collects the user’s age, shows the difference between a string 
# and an integer, and grants access only if the user is 18 or older.


# ----------------------------------------------------------------------------------------------

height = input("How tall are you, in inches?")
height =int(height)

if height >= 48:
    print("You are tall enough to ride!")
else:
    print("Sorry, you can get on the ride when you are a little taller!")

# CHATGPT SUMMARY 

# This Python code is a simple height-check program that decides if someone 
# is tall enough for a ride.

# Here’s what it does step by step:

# It asks the user, "How tall are you, in inches?", and stores the response 
# in the variable height.

# Since input() returns a string, it converts the value to an integer using int(height).

# It then uses an if-else statement to check the person’s height:

# If the height is 48 inches or taller, it prints "You are tall enough to ride!".

# Otherwise, it prints "Sorry, you can get on the ride when you are a little taller!".

# ✅ In short:
# The code takes a person’s height and tells them whether they are tall enough 
# to go on a ride.