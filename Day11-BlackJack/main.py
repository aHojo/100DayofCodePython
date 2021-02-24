
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random


# deal_card() function uses the List below to *return* a random card.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# function called calculate_score() that takes a List of cards as input
# and returns the score.


def calculate_score(cards=[]):
    score = sum(cards)
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if score == 21 and len(cards) == 2:
        return 0
    # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if (11 in cards) and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a Draw!!")
    elif computer_score == 0:
        # computer wins
        print(
            f"Computer wins with a score of: {computer_score}")
    elif user_score == 0:
        print(
            f"User wins with a score of: {user_score}")
    elif user_score > 21:
        print(
            f"Computer wins with a score of: {computer_score}")
    elif computer_score > 21:
        print(
            f"User wins with a score of: {user_score}")
    elif user_score > computer_score:
        print(
            f"User wins with a score of: {user_score}")
    else:
        print(
            f"Computer wins with a score of: {computer_score}")


def game():
    # Deal the user and computer 2 cards each using deal_card() and append()
    user_cards = []
    computer_cards = []
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(calculate_score([10, 10, 2, 11]))

    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            answer = input("Would you like to draw another card? (y/n) > ")
            if answer.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        # score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand::: {user_cards} :::")
    print(f"Computers final hand::: {computer_cards} :::")
    print(compare(user_score, computer_score))


while input("Would you like to play blackjack? y/n > ") == "y":
    game()
