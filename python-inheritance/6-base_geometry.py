#!/usr/bin/python3
"""Class gremetry"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """Public instance method: def area(self): that raises an Exception
        with the message area() is not implemented"""
        exepcion = Exception("area() is not implemented")
        raise exepcion
