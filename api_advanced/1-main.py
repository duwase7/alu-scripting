
"""Print top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-api-advanced/1.0'}
    params = {'limit': 10}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data').get('children')

    for post in posts:
        print(post.get('data').get('title'))
