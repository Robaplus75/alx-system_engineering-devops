#!/usr/bin/python3
""" for quering reddit apit using recursive fucntion"""
import sys
import requests

para_after = None
count_dict = []


def count_words(subreddit, word_list):
    """recursive func"""
    global para_after
    global count_dict

    headers = {
            "User-Agent": "Of course I had to use a custom User-Agent",
            "X-Forwared-For": "iamthecavalry"
            }
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': para_after}

    response = requests.get(
            api_url, headers=headers,
            allow_redirects=False, params=params)
