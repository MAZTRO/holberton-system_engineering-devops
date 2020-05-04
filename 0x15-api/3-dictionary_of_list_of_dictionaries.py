#!/usr/bin/python3
"""
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.
"""
from sys import argv
import json
import requests

if __name__ == "__main__":
    av = argv
    uri = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(uri + 'users')
    todos = requests.get(uri + 'todos')

    todo_list = []
    data = {}

    for user in users.json():
        for todo in todos.json():
            if user['id'] == todo.get('userId'):
                todo_list.append({"username": user.get('username'),
                                 "task": todo.get('title'),
                                 "completed": todo.get('completed')})
        data[user['id']] = todo_list
        todo_list = []
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data, json_file)
