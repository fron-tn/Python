# PASSING AN ARNITRARY NUMBER OF ARGS
toppings = "pepperoni"
def make_pizza(*toppings):
  """Print the list of toppings that have been requested."""
  print("f - {toppings}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# MIXING POSITIONAL & ARBITRARY ARGS

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# USING ARBITRARY KEYWORDS ARGUMENT

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last

  return user_info

user_profile = build_profile('mavo', 'swago', location='Pluto', field='Gamer')
print(user_profile)