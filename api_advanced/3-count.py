#!/usr/bin/python3
"""Module that recursively counts keywords in hot posts of a subreddit."""
import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print sorted count of given keywords"""
    if counts is None:
        counts = {}
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(
        url,
        headers={'User-Agent': 'alu-api-advanced/1.0'},
        params={
            'after': after,
            'limit': 100
        },
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get('data')

    for post in data.get('children'):
        title = post.get('data').get('title').lower()
        words = re.findall(r'\b\w+\b', title)

        for word in words:
            if word in counts:
                counts[word] += 1

    after = data.get('after')

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    sorted_words = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))
