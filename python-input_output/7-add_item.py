#!/usr/bin/python3
import json
import sys
import os


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    filename = 'add_item.json'

    # comprobar si existe
    # si no []
    if os.path.exists(filename):
        item = load_from_json_file(filename)
    else:
        item = []

    # debemos add lo dado por el usuario
    item.extend(sys.argv[1:])

    save_to_json_file(item, filename)

if __name__ == "__main__":
    main()
