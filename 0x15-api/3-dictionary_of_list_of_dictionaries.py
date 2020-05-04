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
                USER_NAME = user['username']
                USER_ID = todo['userId']
                TASK_STATUS = todo['completed']
                TASK_TITLE = todo['title']
                todo_list.append({"username": USER_NAME,
                                 "task": TASK_TITLE,
                                 "completed": TASK_STATUS})
        data[user['id']] = todo_list
        todo_list = []
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data, json_file)
