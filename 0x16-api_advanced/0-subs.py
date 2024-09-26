import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers, or 0 if invalid.
    """
    # Define the API URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid 'Too Many Requests' error
    headers = {'User-Agent': 'subreddit-subscriber-counter/0.1'}
    
    try:
        # Make the request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates success
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            # Return the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If the status code is anything other than 200, return 0
            return 0
    except requests.RequestException:
        # In case of any network-related errors, return 0
        return 0
