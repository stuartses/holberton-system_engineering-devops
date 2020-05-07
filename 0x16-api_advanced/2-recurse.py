#!/usr/bin/python3
"""
Accesing end-point to Reddit Api
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Get a list of all Hot post by subreddit

    Arguments:
              subreddit: String with name of subreddit
              hot_list: List of Posts titles
    """

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)

    headers = {'user-agent': 'holberton-1199/0.0.1'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    # print ("{}: {}".format(after, url))
    if (req.status_code != 200):
        return None

    req_json = req.json()
    after = req_json.get('data').get('after')
    posts = req_json.get('data').get('children')

    for post in posts:
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        hot_list += recurse(subreddit, hot_list, after)

    return hot_list
