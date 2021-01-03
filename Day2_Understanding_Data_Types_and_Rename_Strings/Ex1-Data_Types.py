""" Given a random number add the digits together
EX 
input == 39
code does 3 + 9 = 12
 """

num = input("Please give a number > ")

length = len(num)


try:
    if length == 1:
        print(f"{num} + {0} = {num}")
    else:
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
except ValueError as verr:
    print("You must input a number")

""" 
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Ex1-Data_Types.py 
Please give a number > 23
2 + 3 = 5
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Ex1-Data_Types.py 
Please give a number > 5
5 + 0 = 5
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Ex1-Data_Types.py 
Please give a number > asdf
You must input a number
"""
