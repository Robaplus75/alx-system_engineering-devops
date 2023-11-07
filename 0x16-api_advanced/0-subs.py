#!/usr/bin/python3

""" For returning the number of subscribers in the subredit"""

from requests import get
from sys import argv


headers = {
    "User-Agent": "Of course I had to use a custom User-Agent",
    "X-Forwared-For": "iamthecavalry"
}


def number_of_subscribers(subreddit: str):
    """returns the no of subscribers"""
    api_res = get(f"https://www.reddit.com/r/{subreddit}/about.json",
                   headers=headers)
    try:
        if 'error' in api_res.json().keys():
            return 0
        else:
            return api_res.json()['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
