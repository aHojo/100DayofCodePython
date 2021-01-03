""" 
Given Height in meters, and weight in kg calculate the bmi
"""

try:
    height = float(input("Please input your height (m) > "))
    weight = float(input("Please input your weight (kg) > "))

    BMI = weight / (height * height)

    print(f"BMI is {weight} / {height} * {height} = {BMI}")

except ValueError:
    print("Only numbers allowed in the input")

""" 
vscode ➜ /workspaces/100DayofCodePython (main ✗) $ python Day2_Understanding_Data_Types_and_Rename_Strings/Ex2-BMI_Calculator.py 
Please input your height (m) > 1.8288
Please input your weight (kg) >104.326
BMI is 104.326 / 1.8288 * 1.8288 = 31.19321439260162
"""
