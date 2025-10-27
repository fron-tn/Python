# WHILE LOOPS

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# CHATGPT SUMMARY

# This Python code demonstrates a simple while loop that counts from 1 to 5.

# Here’s what happens step by step:

# The variable current_number starts at 1.

# The while loop runs as long as current_number is less than or equal to 5.

# Inside the loop:

# It prints the current number.

# Then increases (+= 1) the number by 1 each time the loop runs.

# When current_number becomes 6, the condition current_number <= 5 is no longer true, 
# so the loop stops.

# ✅ In short:
# The code prints the numbers 1 through 5, one per line, by repeatedly 
# increasing a counter in a while loop.

# -----------------------------------------------------------------------------------------

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program\n "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
     print(f"\nMessage = {message}")

# CHATGPT SUMMARY

# This Python code is a simple echo program that repeats back whatever the user types — 
# until they choose to quit.

# Here’s how it works:

# A prompt message is created that tells the user what to do and how to stop 
# the program (by typing 'quit').

# The variable message starts as an empty string.

# The while loop runs as long as the user’s input is not 'quit'.

# Inside the loop:

# The program asks for input using input(prompt).

# If the user doesn’t type 'quit', it prints the message back to them.

# When the user types 'quit', the condition fails and the loop ends.

# ✅ In short:
# The code repeatedly asks the user to type something, then prints it back — 
# and stops running when the user enters 'quit'.

# --------------------------------------------------------------------------------------

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message) 

# CHATGPT SUMMARY

# This Python code is another version of an interactive echo program that keeps running 
# until the user types 'quit'.

# Here’s how it works step by step:

# A prompt message tells the user to type something or enter 'quit' to stop.

# The variable active is set to True, meaning the program is currently running.

# The while active: loop continues as long as active remains True.

# Inside the loop:

# The user is asked for input (message = input(prompt)).

# If the user types 'quit', active is set to False, which ends the loop.

# Otherwise, the program prints back whatever the user typed.

# ✅ In short:
# The code repeatedly takes user input and echoes it back until the user enters 'quit', 
# at which point the loop stops.

# --------------------------------------------------------------------------------------

prompt = "\nPlease enter the name of a city you would like to visit:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}!")

# CHATGPT SUMMARY

# This Python code is an interactive program that asks the user to name cities they’d 
# like to visit and responds until the user decides to quit.

# Here’s how it works step by step:

# A prompt message asks the user to enter a city name or 'quit' to stop.

# The while True: loop runs indefinitely until it’s explicitly broken.

# Inside the loop:

# The user types a city name (city = input(prompt)).

# If the input is 'quit', the break statement ends the loop.

# Otherwise, it prints a message like "I'd love to go [City]!", 
# formatting the city name with .title().

# ✅ In short:
# The program keeps asking the user for cities and responds with a friendly message until 
# the user types 'quit', at which point the loop stops.

# --------------------------------------------------------------------------------------

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
     continue

    print(current_number)

# CHATGPT SUMMARY 

# This Python code demonstrates how to use the continue statement inside a while loop
# to skip certain iterations.

# Here’s what it does step by step:

# The variable current_number starts at 0.

# The loop runs while current_number is less than 10.

# Each time through the loop, current_number increases by 1.

# The line if current_number % 2 == 0: checks if the number is even.

# If it is even, the continue statement tells Python to skip the rest of the loop 
# and move to the next iteration.

# If the number is odd, it prints the number.

# ✅ In short:
# The code counts from 1 to 10 but only prints the odd numbers (1, 3, 5, 7, 9),
# skipping all even ones using continue.