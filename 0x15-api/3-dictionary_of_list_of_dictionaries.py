#!/usr/bin/python3
"""returns all information about his/her todo list progress in json"""
import json
import requests

if __name__ == "__main__":
    users = 'https://jsonplaceholder.typicode.com/users/'
    todos = 'https://jsonplaceholder.typicode.com/todos'
    d_user = requests.get(users)
    d_todos = requests.get(todos)
    data_user = d_user.json()
    data_todo = d_todos.json()
    data = {}
    for user in data_user:
        data[user['id']] = []
        for todo in data_todo:
            if todo['userId'] == user['id']:
                data[user['id']].append({
                    'task': todo['title'],
                    'completed': todo['completed'],
                    'username': user['username']
                    })
    concat = 'todo_all_employees' + '.json'
    with open(concat, mode='w') as json_file:
        json.dump(data, json_file)
