#!/usr/bin/python3
"""Module that prints the titles of the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = {'User-Agent': 'alu-api-advanced/1.0'}
    params = {'limit': 10}
   response = requests.get(
    reddit_url,
    headers=headers,
    params=params,
    allow_redirects=False
)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
