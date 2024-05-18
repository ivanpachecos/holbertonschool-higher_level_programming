#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    char = set_1.intersection(set_2)
    unio_t = set_1.union(set_2)
    result = unio_t - char
    return list(result)
