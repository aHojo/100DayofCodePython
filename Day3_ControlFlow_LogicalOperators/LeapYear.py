""" 
Leap year is divisble by 4
not leap year if divisible by 100 but leap year if it's divisible by 400. 
 """


def check_leap_year(year):

    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        return False


year = int(input("What year do you want to check > "))

isLeap = check_leap_year(year)

if isLeap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is a not leap year")
