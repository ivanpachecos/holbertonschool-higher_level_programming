#!/usr/bin/python3
"""
This script fetches prints and save posts from a public API.
"""

import requests
import json


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

