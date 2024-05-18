#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    add_all = 0

    for number in new_list:
        add_all += number

    return add_all
