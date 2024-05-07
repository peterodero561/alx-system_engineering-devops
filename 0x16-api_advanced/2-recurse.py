#!/usr/bin/python3
'''returns a list containing the titles of all hot
articles for a given subreddit.'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''returns a list containing the titles of all
    hot articles for a given subreddit.'''
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
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error: {e}")
        return None  # Return None if an exception occurs
