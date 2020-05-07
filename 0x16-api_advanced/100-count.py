#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import operator
import requests


def count_words(subreddit, word_list, dict_words={}, after=""):
    main_url = 'https://www.reddit.com/'
    sub_reddit = 'r/{}/hot.json?limit=100&after={}'.format(subreddit, after)
    header = {
        'User-Agent': 'MAZTRO',
        'From': 'youremail@domain.com'
    }

    response = requests.get(main_url + sub_reddit,
                            headers=header,
                            allow_redirects=False)

    if ('error' in response.json().keys()):
        return


    if (len(dict_words) == 0):
        dict_words = dict.fromkeys(word_list, 0)
    words = ''
    list_word = []
    for titles in response.json()['data']['children']:
        words += titles['data']['title']
        list_word = words.split(' ')


    for word in list_word:
        for key, value in dict_words.items():
            if key == word:
                dict_words[key] += 1

    after = response.json()['data']['after']

    if (after is None):
        for k, v in sort_dict.items():
            if v is not 0:
                print("{}: {}".format(k, v))
    else:
        return count_words(subreddit, word_list, dict_words, after)
