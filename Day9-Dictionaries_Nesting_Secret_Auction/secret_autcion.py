import os
from art import logo

os.system('cls' if os.name == 'nt' else 'clear')


bids = {}
print(logo)
print("Welcome to the secret auction program.")
while True:
    name = input("What is your name? > ")
    bid = input("What's your bid? > ")

    if bid.startswith("$"):
        bid = bid.strip("$")

    bids[name] = int(bid)

    answer = input("Are there any other bidders? Type 'yes' or 'no ").lower()
    if answer == 'no':
        break
    elif answer == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        print("Please type yes or no")

max_bidder = ""

for k in bids:
    if not max_bidder:
        max_bidder = k
    if bids[max_bidder] < bids[k]:
        max_bidder = k

os.system('cls' if os.name == 'nt' else 'clear')
print(f"The max bidder is {max_bidder} with ${bids[max_bidder]}")
