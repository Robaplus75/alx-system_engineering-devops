#!/usr/bin/python3

""" For printing the titles of the first 10 hot posts"""

from sys import argv
from requests import get


def top_ten(subreddit: str) -> None:
    """prints the titles"""
    headers = {
        "User-Agent": "Marvel's Agents of Shield/21",
        "X-Forwared-For": "Phil J. Coulson"
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        api_res = get(url, headers=headers,
                       allow_redirects=False).json()
        data = api_res['data']['children']
        [print(post['data']['title']) for post in data[:10]]

    except Exception:
        print("None")


if __name__ == "__main__":
    (top_ten(argv[1]))
