#!/usr/bin/python3
'''prints a sorted count of given keywords
(case-insensitive, delimited by spaces.'''
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    '''prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.'''
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
                url, headers=headers, params=params,
                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        word_count[word] = word_count.get(word, 0) + 1

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(
                        word_count.items(),
                        key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word.lower()}: {count}")
        else:
            return
    except Exception as e:
        print(f"Error: {e}")
