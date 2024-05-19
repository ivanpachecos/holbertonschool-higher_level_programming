#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    orden_key = {}
    # order dictionary
    for key in sorted_keys:
        orden_key[key] = a_dictionary[key]

    for key_, value in orden_key.items():
        print("{}: {}".format(key_, value))
