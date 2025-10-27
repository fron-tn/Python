# copying a list
my_foods = ["pizza", "frecnch toast", "carrot cake" ]
friend_foods = my_foods[:]

print(f"My favorite foods are: {my_foods}")
print(f"My friends favorite foods are: {friend_foods}")

my_foods.append("pasta")
friend_foods.append("BBQ")

print(f"\nMy favorite foods are: {my_foods}")
print(f"My friends favorite foods are: {friend_foods}")
