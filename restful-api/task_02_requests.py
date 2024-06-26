#!/usr/bin/python3
"""
This script fetches prints and save posts from a public API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from the JSONPlaceholder API and print the titles of
    the posts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)
    posts = response.json()
    status = response.status_code

    print("Status Code: {}".format(status))

    if status == 200:
        for post in posts:
            print("{}".format(post['title']))

def fetch_and_save_posts():
    """
    Fech posts all content from JSONplaceholder API and save in a file csv
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)
    status = response.status_code

    if status == 200:
        posts = response.json()
        # Create structure
        data_posts = [{'id': post['id'], 'title': post['title'],
                       'body': post['body']} for post in posts]
        with open("posts.csv", 'w', newline='', encoding='utf-8') as file_csv:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
            writer.writeheader()
            for post in data_posts:
                writer.writerow(post)
