#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent to avoid potential issues with the Reddit API
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    # Add 'after' parameter for pagination if provided
    if after:
        url += f'&after={after}'

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and the status code is 200 (OK)
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                return hot_list

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Recursive call with 'after' parameter for next page
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        except KeyError:
            return None
    elif response.status_code == 302:
        return None
    else:
        return None