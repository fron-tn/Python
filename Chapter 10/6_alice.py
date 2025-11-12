# HANDLING THE FILENOTFOUNDERROR EXCEPTION

from pathlib import Path
path = Path("alice")

try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Sorry, the file {path} does not exist!")


print("\n.......Reading another file.......")
