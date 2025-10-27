# DICTIONARY OF SIMILAR OBJECTS
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# CHATGPT SUMMARY

# This Python code shows how to access a specific value from a dictionary using its key.

# Here’s what it does step by step:

# A dictionary called favorite_languages is defined, where each key is a person’s name 
# and each value is their favorite programming language.

# The line

# language = favorite_languages['sarah'].title()


# retrieves the value associated with the key 'sarah' (which is 'c'), and formats it 
# with .title() to display it as 'C'.

# The print() statement then displays a personalized message:

# Sarah's favorite language is C.


# ✅ In short:
# The code looks up Sarah’s favorite programming language from the dictionary and 
# prints it in a nicely formatted sentence.

# --------------------------------------------------------------------------------------

# USE GET() TO ACCESS VALUE
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# CHATGPT SUMMARY

# This Python code demonstrates how to safely access dictionary values 
# using the .get() method.

# Here’s what happens step by step:

# A dictionary named alien_0 is created with two key–value pairs:

# 'color': 'green'

# 'speed': 'slow'

# The line

# print(alien_0['points'])


# tries to access the key 'points', but since it doesn’t exist, it would normally 
# cause a KeyError (an error that stops the program).

# The next line avoids that problem by using .get():

# point_value = alien_0.get('points', 'No point value assigned.')


# .get() checks for the 'points' key.

# If the key isn’t found, it returns the default message 'No point value assigned.' 
# instead of causing an error.

# Finally, it prints that message.

# ✅ In short:
# The code shows that using .get() is a safe way to retrieve a value from a dictionary — 
# it provides a fallback message when the key doesn’t exist.