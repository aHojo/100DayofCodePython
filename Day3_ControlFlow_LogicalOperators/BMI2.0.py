""" 
Given Height in meters, and weight in kg calculate the bmi
"""

try:
    height = float(input("Please input your height (m) > "))
    weight = float(input("Please input your weight (kg) > "))

    BMI = weight / (height * height)

    if BMI < 18.5:
        print(
            f"BMI is {weight} / {height} * {height} = {BMI}, your BMI is Underweight")
    elif BMI < 25:
        print(
            f"BMI is {weight} / {height} * {height} = {BMI}, your BMI is Normal Weight")
    elif BMI < 30:
        print(
            f"BMI is {weight} / {height} * {height} = {BMI}, your BMI is Overweight")
    elif BMI < 35:
        print(
            f"BMI is {weight} / {height} * {height} = {BMI}, your BMI is obes")
    else:
        print(
            f"BMI is {weight} / {height} * {height} = {BMI}, your BMI is Clinically obese")

except ValueError:
    print("Only numbers allowed in the input")
