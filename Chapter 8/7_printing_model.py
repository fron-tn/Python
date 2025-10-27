# MODIFYING A LIST IN A FUNCTION

# EXAMPLE 1
# start with some design that needs to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
      current_design = unprinted_designs.pop()
      print(f"Printing model: {current_design}")
      completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# EXAMPLE 2

def print_models(unprinted_designs, completed_models):
     """Simulate printing each design, until there are none left.
        Move each design to completed_models after printing"""
     
     while unprinted_designs:
          current_design = unprinted_designs.pop()
          print(f"Printing model: {current_design}")
          completed_models.append(current_design)

def show_completed_models(completed_models):
     """Show all models that were printed"""
     print(f"\nThe following models have been printed:")
     for completed_model in completed_models:
          print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"] 
completed_models = []

new_designs = ["x", "y", "z"]
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# EXAMPLE 3
print("\n--- EXAMPLE 3 ---\n")
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"] 
completed_models = []
copy_of_list = unprinted_designs[:]

print_models(copy_of_list, completed_models)
show_completed_models(completed_models)

print(f"\nOriginal List: {unprinted_designs}")
print(f"\nCopy of Original List: {copy_of_list}")