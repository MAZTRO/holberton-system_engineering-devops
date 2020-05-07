#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    main_url = 'https://www.reddit.com/'
    sub_reddit = 'r/{}/hot.json?after={}'.format(subreddit, after)
    header = {
        'User-Agent': 'MAZTRO',
        'From': 'youremail@domain.com'
    }

    response = requests.get(main_url + sub_reddit,
                            headers=header,
                            allow_redirects=False)

    if ('error' in response.json().keys()):
        return (None)

    for titles in response.json()['data']['children']:
        hot_list.append(titles['data']['title'])

    after = response.json()['data']['after']

    if (after is None):
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
