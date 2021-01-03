""" Given an age, print out how many days weeks, and months left if you live until your 90 """
MAX_DAYS = 90 * 365
MAX_WEEKS = 90 * 52
MAX_MONTHS = 90 * 12

try:
    age = int(input("Please give your age > "))
    days_left = MAX_DAYS - (age * 365)
    weeks_left = MAX_WEEKS - (age * 52)
    months_left = MAX_MONTHS - (age * 12)

    print(
        f"You have {days_left} days {weeks_left} weeks {months_left} months left.")

except ValueError:
    print("You must supply an integer")

""" 
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Ex3_How_Many_Weeks_Left.py 
Please give your age > 67
You have 8395 days 1196 weeks 276 months left.

"""
