
"""Recursive function to get all hot post titles"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot post titles"""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-api-advanced/1.0'}
    params = {'after': after}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')

    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
