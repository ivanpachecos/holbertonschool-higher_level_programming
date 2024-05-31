#!/usr/bin/python3
"""
This script converts a CSV file to JSON format and saves the
result in 'data.json'.
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts a CSV file to JSON format and saves it to 'data.json'.
    """
    try:
        data = []

        with open(csv_file, 'r', encoding="utf-8") as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                data.append(row)

        # Write the data to a JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
