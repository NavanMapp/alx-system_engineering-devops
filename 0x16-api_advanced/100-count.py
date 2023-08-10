#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)."""

import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    if after is None:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers={'User-agent': 'Mozilla/5.0'}).json()
    else:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}', headers={'User-agent': 'Mozilla/5.0'}).json()

    if 'data' in response and 'children' in response['data']:
        for post in response['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if word in word_count:
                    word_count[word] += title.count(word)
                else:
                    word_count[word] = title.count(word)

        if 'after' in response['data'] and response['data']['after'] is not None:
            count_words(subreddit, word_list, response['data']['after'], word_count)
        else:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

subreddit_name = "programming"
keywords = ["javascript", "python", "java"]

count_words(subreddit_name, keywords)