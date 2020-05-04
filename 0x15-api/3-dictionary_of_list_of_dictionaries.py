#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests

if __name__ == "__main__":
    uri = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(uri + 'users')
    todos = requests.get(uri + 'todos')
    data = {}
    for user in users.json():
        data[user.get('id')] = []
        for td in todos.json():
            if user.get('id') == td.get('userId'):
                data[user.get('id')].append({"username": user.get('username'),
                                            "task": td.get('title'),
                                            "completed": td.get('completed')})
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data, json_file)
