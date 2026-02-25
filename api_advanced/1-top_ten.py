#!/usr/bin/python3
"""Module that prints the titles of the top 10 hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles of a subreddit.

    Returns:
        True if successful (valid subreddit), None if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Prevent redirect to search for invalid subreddit
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return None  # invalid subreddit

    data = response.json().get('data', {})
    children = data.get('children', [])

    # Print first 10 titles
    for post in children[:10]:
        print(post.get('data', {}).get('title'))

    return True  # indicates valid subreddit
