#!/usr/bin/python3
"""Returns number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return subscriber count"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alu-api-advanced/1.0'}

    response = requests.get(url,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
