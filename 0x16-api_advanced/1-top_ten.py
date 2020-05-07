#!/usr/bin/python3
"""
Accesing end-point to Reddit Api
"""

import requests


def top_ten(subreddit):
    """Print the the first 10 hot posts listed for a given subreddit
    Or None if it is invalid subreddit

    Arguments:
              subreddit: String with name of subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'holberton-1199/0.0.1'}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if (req.status_code != 200):
        print(None)
        return

    req_json = req.json()
    posts = req_json.get('data').get('children')

    for post in posts:
        title = post.get('data').get('title')
        print(title)
