#!/usr/bin/env python3

import sys

"""Script to check to calculate factorial of a number"""
while True:
    try:
        """Asks user to enter a number"""
        user_input = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a number > 1 without spaces.")
        continue
    else:
        break

if user_input < 2:
    print("{} cannot be factorized. ':)'".format(user_input))
else:
    total = 1
    for num in range(1, user_input + 1):
        total *= num
    print(f"{user_input:,} factorial = {total:,}")
    print(f"{user_input:,} permutations = {total:,}")
