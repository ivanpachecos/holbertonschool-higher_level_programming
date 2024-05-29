#!/usr/bin/python3
"""Serialize and deserialize custom Python
objects using the pickle module.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return (pickle.load(file))
        except (IOError, pickle.PickleError) as e:
            print(f"Error deserializing object: {e}")
            return (None)

    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}". format(
            self.name, self.age, self.is_student))