#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_all = 0
    new_list = list(set(my_list))
    for number in new_list:
        sum_all += number

    return sum_all
