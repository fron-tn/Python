# WRITING A SINGLE LINE


from pathlib import Path

# Writing multiple lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path("programming.txt")
# path.write_text("I love programming") # Writing a single line

path.write_text(contents)