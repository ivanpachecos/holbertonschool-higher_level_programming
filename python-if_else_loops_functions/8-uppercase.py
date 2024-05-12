#!/usr/bin/python3

def uppercase(str):
    text_upper = ""
    for char in str:
        if 'a' <= char <= 'z':
            text_upper += chr(ord(char) - 32)
        else:
            text_upper += char
    print("{}".format(text_upper))
