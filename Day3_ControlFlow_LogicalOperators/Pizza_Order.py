""" 
Small Pizza $15
Medium Pizza $20
Large Pizza $25 

pep for S +2
pep for m or L +3

extra cheese +1 any pizza
"""

print("Welcome to the Pizza Delivery App!")
size = input("What size would you like? (L, M, S) > ")
add_pepperoni = input("Would you like to add Pepporni? (Y/N) > ")
extra_cheese = input("Do you want extra cheese? (Y/N) > ")


total = 0

if size.upper() == "L":
    total += 25
elif size.upper() == "M":
    total += 20
else:
    total += 15

if add_pepperoni.upper() == "Y":
    if size.upper() == "L" or size.upper() == "M":
        total += 3
    else:
        total += 2

if extra_cheese.upper() == "Y":
    total += 1

print(f"Your order for a {size} pizza is {total}")
