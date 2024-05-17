#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    copy_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return copy_list
    else:
        del my_list[idx]
        del copy_list[idx]
        return copy_list
