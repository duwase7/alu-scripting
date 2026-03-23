#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:my.reddit.app:v1.0.0 (by /u/elie)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except requests.RequestException:
        print("None")
