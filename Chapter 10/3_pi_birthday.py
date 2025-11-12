# IS YOUR BIRTHDAY CONTAIN IN PI

from pathlib import Path

path = Path("pi_ten_million.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = " "
for line in lines:
    pi_string += line.lstrip()


birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of the pi.")
else:
    print("Your birthday does not appear in the first million digits of the pi.")

