#!/usr/bin/env python3
s = input("Give me a number: ")
n = float(s)

if n.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")