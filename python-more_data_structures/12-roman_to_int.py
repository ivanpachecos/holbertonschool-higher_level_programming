#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    r_list = []
    rez = 0

    for c in roman_string:
        if c in roman_n:
            r_list.append(roman_n[c])
        else:
            return 0  # Si hay un carácter no válido en la cadena, retorna 0

    list_len = len(r_list)
    for i in range(list_len):
        if i == list_len - 1:
            rez += r_list[i]
        elif r_list[i] < r_list[i+1]:
            rez -= r_list[i]
        else:
            rez += r_list[i]
    return rez
