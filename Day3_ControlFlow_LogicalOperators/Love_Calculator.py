print("Welcome to the Love Calculator!")
name1 = input("What is your name? > ").lower()
name2 = input("What is his/her name? > ").lower()

love_total1 = 0
love_total2 = 0

love_list1 = ["t", "r", "u", "e"]
love_list2 = ["l", "o", "v", "e"]

marriage = name1 + name2
for letter in love_list1:
    love_total1 += marriage.count(letter)

for letter in love_list2:
    love_total2 += marriage.count(letter)

score = str(love_total1) + str(love_total2)
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
