#!/usr/bin/python3

save_string = ""

for word in range(122, 96, -1):
    if word % 2 == 0:
        save_string += chr(word)
    else:
        save_string += chr(word - 32)

print(save_string)
