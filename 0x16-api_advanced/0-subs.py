#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the API URL for the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and the status code is 200 (OK)
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            return 0
    elif response.status_code == 302:
        return 0
    else:
        return 0