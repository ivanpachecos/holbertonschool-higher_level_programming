#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    item1 = tuple_a + (0, 0)
    item2 = tuple_b + (0, 0)

    add_one = item1[0] + item2[0]
    add_second = item1[1] + item2[1]

    return (add_one, add_second,)
