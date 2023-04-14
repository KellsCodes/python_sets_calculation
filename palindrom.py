#!/usr/bin/env python3

"""Script that will accept a word,check if the world is palindrome"""

user_input = input("Enter a word to check for palindrome: ")
count = 0
for index, char in enumerate(user_input):
    # only count letters that match in reverse
    if (char == user_input[(len(user_input) - 1) - index]):
        count += 1
# check if the counted letter in reverse is equal to length of input
if (count == len(user_input)):
    print("{} is a palindrome".format(user_input))
else:
    print("{} is not a palindrome".format(user_input))
