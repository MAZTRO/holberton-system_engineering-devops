#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    av = argv
    uri = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(uri + 'users')
    name = ''
    relations = requests.get(uri + 'users/{}/todos'.format(av[1]))
    for user in users.json():
        if (user['id'] == int(av[1])):
            name = user['name']
    msg = ' is done with tasks('
    list_true = []
    for relation in relations.json():
        if (relation['completed'] is True):
            list_true.append(relation)
    trues = len(list_true)
    total = len(relations.json())
    print('Employee ' + name + msg + '{}/{}):'.format(trues, total))
    for todo in list_true:
        print("\t {}".format(todo['title']))
