#!/usr/bin/python3

exect_letter_one = "q"
exect_letter_two = "e"

for letters in range(97, 123):
    if chr(letters) == exect_letter_one or chr(letters) == exect_letter_two:
        continue
    print("{}".format(chr(letters)), end="")
