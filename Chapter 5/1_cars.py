# SIMPLE IF STATEMENT EXAMPLES

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
 if car == 'bmw':
   print(car.upper())
else:
 print(car.title())

 # CHECKING FOR EQUALITY
 car = "bmw"
 print(f"Is the car a bmw?: {car == "bmw"}")

 print("\n")
 car = "audi"
 print(f"Is the car a bmw?: {car == "bmw"}")

#   CASE SENSITIVE 
car = "Audi"
print(f"\nIs the car a Audi?: {car == "Audi"}")

print(f"\nIs the car a Audi?: {car == "audi"}")

print(f"\nIs the car a Audi?: {car.lower() == "audi"}")

#  checking for inequality
