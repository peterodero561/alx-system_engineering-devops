#!/usr/bin/python3
'''function to querry subreddit'''
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error: {e}")
        return 0  # Return 0 if an exception occurs
