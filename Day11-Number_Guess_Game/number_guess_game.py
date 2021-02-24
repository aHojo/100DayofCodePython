#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
game_mode = "easy"
attempts = 10
random_number = 0


def get_random_number():
    return random.randint(1, 100)

def check_guess(guess, random_number):
    if guess == random_number:
        return True
    elif guess < random_number:
        print("Too low")
    else:
        print("Too High.")
    return False 
        

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice.lower() == "hard":
    game_mode = "hard"
    attempts = 5

def game(attempts):
    random_number = get_random_number()
    while True:
        guess = int(input("Make a guess: "))

        is_win = check_guess(guess, random_number)
        if is_win:     
            print(f"You win! The number was > {random_number}")
            break

        attempts -= 1
        if attempts == 0: 
            print(f"You have run out of attempts. Oops. Number was {random_number}")
            break
        print("Guess again -> ")
        print(f"You have {attempts} remaining")

game(attempts)
    



