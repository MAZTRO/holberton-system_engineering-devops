#!/usr/bin/python3
"""
    Using what you did in the task #0,
    extend your Python script to export data in the CSV format
"""
from sys import argv
import csv
import requests

if __name__ == "__main__":
    av = argv
    uri = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(uri + 'users/{}'.format(av[1]))
    name = users.json()['username']
    name_file = str(users.json()['id']) + ".csv"
    relations = requests.get(uri + 'users/{}/todos'.format(av[1]))

    with open(name_file, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for relation in relations.json():
            USER_ID = relation['userId']
            USERNAME = name
            TASK_STATUS = relation['completed']
            TASK_TITLE = relation['title']
            writer.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
