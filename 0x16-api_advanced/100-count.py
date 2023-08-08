#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)."""

import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = {}

    headers = {'User-Agent': 'CustomUserAgent'}

    # API URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    # API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_counts:
                    print(f"{word}: {count}")
                return

            for post in posts:
                title = post['data']['title']
                title_words = title.lower().split()

                for word in word_list:
                    if word in title_words:
                        if word in word_counts:
                            word_counts[word] += title_words.count(word)
                        else:
                            word_counts[word] = title_words.count(word)

            after = data['data']['after']
            return count_words(subreddit, word_list, after, word_counts)
        except KeyError:
            return None
    elif response.status_code == 302:
        return None
    else:
        return None