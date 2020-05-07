#!/usr/bin/python3
"""
Accesing end-point to Reddit Api
"""

import requests


def number_of_subscribers(subreddit):
    """
    Send a GET request to take the numbers of subscribers in subreddit

    Arguments:
             subreddit: String with name of subreddit
    Return:
           Integer with number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'holberton-1199/0.0.1'}
    req = requests.get(url, headers=headers).json().get('data')

    return req.get('subscribers')
