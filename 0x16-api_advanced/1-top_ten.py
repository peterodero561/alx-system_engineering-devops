#!/usr/bin/python3
'''created api for reddit'''
import requests


def top_ten(subreddit):
    '''function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error: {e}")
        print("None")  # Print None if an exception occurs
