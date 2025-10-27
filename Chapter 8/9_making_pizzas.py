# IMPORTING AN ENTIRE MODULE

import pizza_module
pizza_module.make_pizza(16, "pepperoni", "mushrooms")


# IMPORT SPECIFIC FUNCTIONS FROM A MODULE

from pizza_module import make_pizza

make_pizza(16, "chicken", "mushrooms", "bbq", "pineapple")


# USING AS TO GIVE A FUNCTION AN ALIAS

from pizza_module import make_pizza as mp

mp(16, "pepperoni")

# USING AS TO GIVE A MODULE AN ALIAS
import pizza_module as p

p.make_pizza(12, "bbq chicken", "pineapple", "extra cheese")