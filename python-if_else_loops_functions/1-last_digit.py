#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "
last_digit = number - (10 * int(number / 10))

# sentances
str_more = "and is greater than 5"
str_zero = "and is 0"
str_less = "and is less than 6 and not 0"

if last_digit > 5:
    print("{}{} is {} {}".format(str, number, last_digit, str_more))
elif last_digit == 0:
    print("{}{} is {} {}".format(str, number, last_digit, str_zero))
else:
    print("{}{} is {} {}".format(str, number, last_digit, str_less))
