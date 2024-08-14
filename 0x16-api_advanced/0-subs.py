#!/usr/bin/python3
"""Function to query Reddit API and return no of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Query reddit api and return no of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-agent": "my-app/0.0.1"}
    try:
        responce = requests.get(url, headers=headers, allow_redirects=False)
        if responce.status_code == 200:
            data = responce.json()
            return data['data']['subscribers']

        else:
            return 0

    except requests.RequestException:
        return 0
