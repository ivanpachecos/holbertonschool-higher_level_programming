#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = list(map(lambda list_: list(map(lambda x : x ** 2, list_)), matrix))
    return new_list
