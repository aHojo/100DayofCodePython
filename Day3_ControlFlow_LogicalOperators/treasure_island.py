
print("Welcome to the Treasure Island!\nYour mission is to find the treasure! ")


choice = ""

print("You enter the cave, go left or right?")

choice = input("> ").lower()


if choice == "left":
    print("You encounter a bridge and a lake, do you swim or walk over the bridge?")
    choice = input("> ").lower()
    if choice == "swim":
        print("Game Over.")
    else:
        print("You encounter three doors, Red, Blue and Yellow. Which door do you choose? ")
        choice = input("> ").lower()
        if choice == "red" or choice == "blue":
            print("Game Over.")
        else:
            print("You found the treasure!")
else:
    print("Game over! ")
