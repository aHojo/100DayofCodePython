def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return print(f"{number} is NOT a prime number")
    return print(f"{number} is in fact a Prime number.")


n = int(input("Check this number: "))
is_prime(number=n)
