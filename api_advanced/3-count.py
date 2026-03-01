cat > api_advanced/3-count.py << 'EOF'
#!/usr/bin/python3
"""Module that recursively counts keywords in hot posts of a subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively counts occurrences of words in hot post titles."""

    if counts is None:
        counts = {}
        word_list = [w.lower() for w in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    for child in children:
        title = child.get('data', {}).get('title', '').lower().split()
        for word in word_list:
            if word in title:
                counts[word] = counts.get(word, 0) + title.count(word)

    if after:
        return count_words(subreddit, word_list, after, counts)

    if counts:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
EOF
