#!/usr/bin/python3
"""
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    av = argv
    uri = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(uri + 'users/{}'.format(av[1]))
    name = users.json()['username']
    name_file = str(users.json()['id']) + ".json"
    relations = requests.get(uri + 'users/{}/todos'.format(av[1]))

    with open(name_file, mode='w') as json_file:
        task_list = []
        for relation in relations.json():
            USER_ID = relation['userId']
            TASK_STATUS = relation['completed']
            TASK_TITLE = relation['title']
            task_list.append({"task": TASK_TITLE,
                             "completed": TASK_STATUS,
                             "username": name})
        data = {relation['userId']: task_list}
        json.dump(data, json_file)
