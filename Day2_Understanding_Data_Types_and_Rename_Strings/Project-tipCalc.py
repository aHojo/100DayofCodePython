""" TIP CALCULATOR
    Give total bill, percentage of tip you want to give, how many people to split the bill. 
    Print out - the amount each person should pay.
"""


BILL_TOTAL = float(input("What was the total bill? > $"))
TIP_PERCENT = float(
    input("What percent of tip would you like to give (10,12,15)? > "))
SPLIT_TOTAL = int(input("How many people are splitting the bill? > "))


ADJUSTED_BILL_AFTER_TIP = BILL_TOTAL + (BILL_TOTAL * (TIP_PERCENT / 100))

AMOUNT_PER_PERSON = ADJUSTED_BILL_AFTER_TIP / SPLIT_TOTAL

print(f"Each person should pay: ${AMOUNT_PER_PERSON:.2f}")


""" 
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Project-tipCalc.py 
What was the total bill? > $150
What percent of tip would you like to give (10,12,15)? > 12
How many people are splitting the bill? > 5
Each person should pay: $33.60
"""
