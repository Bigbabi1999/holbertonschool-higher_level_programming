#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

res = number % 10
while number > 6:
if number > 5:
    print(f"Last digit of {number} is {8} and is greater than 5")
elif number < 6:
    print(f"Last digit of {number} is {-8} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {0} and is 0")
