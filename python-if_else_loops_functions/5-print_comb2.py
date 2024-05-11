#!/usr/bin/python3

for n in range(0, 99):
    if n <= 9:
        print("0{}".format(n), end=", ")
        continue
    print("{}".format(n), end=", ")
