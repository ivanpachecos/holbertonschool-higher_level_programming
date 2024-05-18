#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def r_value(item):
        return replace if item == search else item

    n_list = list(map(r_value, my_list))
    return n_list
