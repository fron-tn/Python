# CREATING A LIST
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# ACCESSING ELEMENT IN A LIST
print(bicycles[1])
print(f"First Element in List: {bicycles[0].title()}")
print(f"Fourth Element in List: {bicycles[3].title()}")

print("\n")
print(f"Last Element in List: {bicycles[-1].title()}")
print(f"Last Element in List: {bicycles[-2].title()}")

print("\n")
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
