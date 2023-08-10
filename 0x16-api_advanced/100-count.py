#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)."""

import praw

def count_words(subreddit, word_list, reddit=None):
    if reddit is None:
        reddit = praw.Reddit(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            user_agent='YOUR_USER_AGENT'
        )

    if not word_list:
        return

    if not subreddit:
        print("Invalid subreddit")
        return

    subreddit_obj = reddit.subreddit(subreddit)
    hot_articles = subreddit_obj.hot(limit=10)

    word_counts = {}

    for submission in hot_articles:
        title = submission.title.lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                if word_lower in word_counts:
                    word_counts[word_lower] += 1
                else:
                    word_counts[word_lower] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

    print("----------------------")

    count_words(subreddit, word_list[1:], reddit)

count_words("programming", ["java", "Python", "javascript", "ruby"])
