# Header
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Chris's Custom Comic Cars!!")
print("Car Customization Form: DC Special")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("(Note: For multiple choice questions, please select a, b, c, or d)")
print()

# Q1: Get the make and model
print("** Make and Model **")
print()
print("What car are you interested in?")
print("     a. Batman Batmobile")
print("     b. Superman Sporta S ")
print("     c. Flash Speedforce T")
print("     d. Green Lantern Lumina")
print()
model = input("Please select a car: ")
print()

# Q2: Offer EV upgrade or Fuel
print("Would you like the electric model?")
ev = input("Please enter 'yes' or 'no': ")
print()

# Q3: Get the exterior Color
print("** Exterior **")
print()
print("What exterior paint would you like?")
extColor = input("You may choose any color or gradient and we will make it: ")
print()

# Q4: Get the interior Color
print("** Interior **")
print()
print("What interior color scheme would you like? ")
print("     a. Gotham Black")
print("     b. Kryptonian Red")
print("     c. Martian Green")
print("     d. Cord Beetle Blue")
print()
intColor = input("Please select an interior color scheme: ")
print()

# Q5: Offer climate control seats
print("Would you like Wayne Enterprises climate controlled seats? ")
seats = input("Please enter yes or no: ")
print()

# Q6: Have then select sports package or tech package
print("** Other **")
print()
print("Would you like the Standard, Sports, or Tech package?")
package = input("Please select a package: ")
print()

#Q7: Ask for dditional requests
request = input("If you have any additional requests or customizations, please enter them now and they will be evaulated for consideration, or put N/A: ")
print()

# Summary
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("** Order Summary  **")
print()
print(f"Model Option: {model}")
print(f"EV Model: {ev}")
print(f"Exterior color: {extColor}")
print(f"Interior color scheme: {intColor}")
print(f"Climate controlled seats: {seats}")
print(f"Trim Package: {package}")
print()
print(f"Additional Requests: {request}")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")