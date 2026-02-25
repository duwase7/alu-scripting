#!/usr/bin/python3
"""
Append all the hot post's titles from a particular
subreddit on a list calleg hot_list.
"""

import json
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves all hot post titles of a subreddit."""
    if hot_list is None:
        hot_list = []url = f"https://www.reddit.com/r/{subreddit}/hot.json"
headers = {'User-Agent': 'Mozilla/5.0'}
params = {'after': after}
response = requests.get(url, headers=headers, params=params, allow_redirects=False)

if response.status_code != 200:
    return None  # invalid subreddit

data = response.json().get('data')
after = data.get('after')
children = data.get('children', [])

# Add all titles to hot_list
for child in children:
    hot_list.append(child.get('data', {}).get('title'))

# Recursive call if more pages
if after:
    return recurse(subreddit, hot_list, after)
return hot_list
    return hot_list
