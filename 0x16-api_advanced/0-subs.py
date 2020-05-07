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
           Integer with number of subscribers or 0 if invalid subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'holberton-1199/0.0.1'}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if (req.status_code != 200):
        return 0

    req_data = req.json().get('data')
    return req_data.get('subscribers')
