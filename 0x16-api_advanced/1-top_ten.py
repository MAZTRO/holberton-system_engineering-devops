#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    main_url = 'https://www.reddit.com/'
    sub_reddit = 'r/{}/hot.json?t=all&limit=10'.format(subreddit)
    header = {
        'User-Agent': 'MAZTRO',
        'From': 'youremail@domain.com'
    }

    response = requests.get(main_url + sub_reddit, headers=header)

    print(response.json()['data']['children'][0]['data']['title'])
