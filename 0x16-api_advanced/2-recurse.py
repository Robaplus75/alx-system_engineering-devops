#!/usr/bin/python3
""" for quering the rest api using recursive function """
import sys
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """the recursive func """
    global after
    headers = {'User-Agent': 'user agent here'}
    api_url = "https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    api_res = requests.get(
            url, headers=headers,
            allow_redirects=False, params=params)

    if api_res.status_code == 200:
        next_ = api_res.json().get('data').get('after')

        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        title_coll = api_res.json().get('data').get('children')

        for t in title_coll:
            hot_list.append(t_.get('data').get('title'))

        return hot_list
    else:
        return (None)
