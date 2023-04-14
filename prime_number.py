#!/usr/bin/env python3

import sys

"""Script to check for prime numbers"""
while True:
    try:
        """Asks user to enter a number"""
        user_input = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid number without spaces.")
        continue
    else:
        break

if user_input < 2:
    print("{} is not a prime".format(user_input))
else:
    flag = False
    # check for factors
    for i in range(2, user_input):
        if user_input % i == 0:
            # if factor is found, set the flag to True and exit loop
            flag = True
            break
    if flag:
        print("{} is not a prime number".format(user_input))
    else:
        print("{} is a prime number".format(user_input))
