# MODULE OPERATOR

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")

#  CHATGPT SUMMARY

# This Python code is a simple even-or-odd checker that determines whether 
# a user’s input number is even or odd.

# Here’s how it works step by step:

# The program asks the user to enter a number using input().

# The input (which is text by default) is converted to an integer with int(number).

# It uses the modulus operator % to check if the number is divisible by 2:

# If number % 2 == 0, the number is even.

# Otherwise, it’s odd.

# Finally, it prints a message telling the user whether the number is even or odd.

# ✅ In short:
# The code takes a number from the user and prints whether it’s even 
# or odd based on the remainder when divided by 2.