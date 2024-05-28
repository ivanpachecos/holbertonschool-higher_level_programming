#!/usr/bin/python3
"""
Este módulo contiene una función para convertir un objeto de Python
a una cadena JSON.
"""
import json


def to_json_string(my_obj):
    """
    Convierte un objeto de Python a una cadena JSON.

    Parámetros:
    my_obj: El objeto de Python que se desea convertir.

    Retorna:
    Una cadena JSON que representa el objeto de Python.
    """
    using_js = json.dumps(my_obj)
    return using_js
