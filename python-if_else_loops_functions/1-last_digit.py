#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number == 0
number % 12345
if number > 5:
    print(f"Last digit of {number} is 0 and is greater than 5")
elif number < 5:
    print(f"Last digit of {number} is 0 less than 5")
else:
    print(f"Last digit of {number} and is 0")
