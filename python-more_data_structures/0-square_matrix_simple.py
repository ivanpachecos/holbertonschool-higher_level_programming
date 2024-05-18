#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # we access the first and second list using map function,
    # save m_l new matrix
    m_l = list(map(lambda list_: list(map(lambda x: x ** 2, list_)), matrix))
    return m_l
