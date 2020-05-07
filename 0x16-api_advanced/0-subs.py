#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    main_url = 'https://www.reddit.com/'
    sub_reddit = 'r/{}/about.json'.format(subreddit)
    header = {
        'User-Agent': 'MAZTRO',
        'From': 'youremail@domain.com'
    }

    response = requests.get(main_url + sub_reddit, headers=header)

    if ('error' in response.json().keys()):
        return 0
    return (response.json()['data']['subscribers'])
