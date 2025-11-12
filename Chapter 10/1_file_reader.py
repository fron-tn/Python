# READING CONTENTS OF A FILE

from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

# contents = contents.rstrip()
# print(contents)
# print("---")


# lines = contents.splitlines() #accessing a file's lines
# for line in lines:
#     print(f"- {line}")
    

# WORKING WITH A FILES CONTENTS
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()
    

print(pi_string)
print(len(pi_string))




