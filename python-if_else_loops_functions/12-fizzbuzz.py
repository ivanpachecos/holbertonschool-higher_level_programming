#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 100):
        if n % 3 == 0 and n % 5 == 0:  # Use 'and' for logical AND
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
    print("{}".format(chr(36)), end="")
