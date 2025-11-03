#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 5:
    print("Last digit of {number} is 2 greater than 5")
elif number < 5:
    print("Last digit of {number} is 2 less than 5")
else:
    print("Last digit of {number} and is 0")
