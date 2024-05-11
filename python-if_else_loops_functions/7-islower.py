#!/usr/bin/python3
# assci table

def islower(c):
    start_lower = 97
    end_lower = 123
    for n in range(start_lower, end_lower):
        if n == ord(c):
            return True
        else:
            return False
