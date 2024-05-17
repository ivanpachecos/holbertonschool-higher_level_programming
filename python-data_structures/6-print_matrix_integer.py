#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
   for row in matrix:
      item = " ".join("{}".format(element) for element in row)
      print(item)
