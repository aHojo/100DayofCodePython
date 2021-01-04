""" 
Determine whether a number is even or odd.


"""

try:
    num = int(input("Please enter a number > "))

    if num % 2 == 0:
        print("This is an EVEN number")
    else:
        print("This is an ODD number")
except ValueError:
    print("Only numbers please")
