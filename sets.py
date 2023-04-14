#!/usr/bin/env python3

import sys

"""Script to perform calculations on three sets of numbers"""


"""
2* Write a python program to enter three sets of numbers with label A,B and C
2i* find the union of the set
2ii* find the intercession of the set.
2iii* Find the set disjoint .
"""

while True:
    try:
        """Asks user to enter a number"""
        A = input("Enter a set of numbers separated by comma for A: ").split(",")
        B = input("Enter a set of numbers separated by commas for B: ").split(",")
        C = input("Enter a set of numbers separated by commas for C: ").split(",")

        A = [int(num) for num in A]
        B = [int(num) for num in B]
        C = [int(num) for num in C]
    except:
        print("Invalid sets of numbers entered.")
        continue
    else:
        break

# finding the union of the sets
set_A = []
for num in A:
    if (num not in set_A):
        set_A.append(num)
for num in B:
    if (num not in set_A):
        set_A.append(num)
for num in C:
    if (num not in set_A):
        set_A.append(num)

# finding the intersection of the sets
set_B = []
for num in A:
    if (num in B and num in C and num not in set_B):
        set_B.append(num)

# finding the set disjoint
flag_A, flag_B = False, False
for num in A:
    if (num in B or num in C):
        flag_A = True
        break
for num in B:
    if (num in C):
        flag_B = True
        break
disjoint = "The sets have common element(s): disjoint = False" if flag_A and flag_B else "The sets have no common element(s): disjoint = True"


# print values to the screen
print("----------------------------------")
print("A input set: {}".format(A))
print("B input set: {}".format(B))
print("C input set: {}".format(C))
print("---------------------------------")
print("Union of the sets: {}".format(set_A))
print("Intersection of the sets: {}".format(set_B))
print("{}".format(disjoint))
