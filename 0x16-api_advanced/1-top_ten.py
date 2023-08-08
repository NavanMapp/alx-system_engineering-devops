#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid potential issues with the Reddit API
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                print(f"No hot posts found for subreddit '{subreddit}'.")
                return

            print(f"Top 10 hot posts in '{subreddit}':")
            for post in posts:
                title = post['data']['title']
                print(f"- {title}")
        except KeyError:
            print("An error occurred while processing the response.")
    elif response.status_code == 302:
        print(f"'{subreddit}' is not a valid subreddit.")
    else:
        print("An error occurred while making the API request.")