#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_users = users.json()
    data_todos = todos.json()
    data = {}
    for user in data_users:
        data[user.get('id')] = []
        for td in data_todos:
            if user.get('id') == td.get('userId'):
                data[user.get('id')].append({"username": user.get('username'),
                                            "task": td.get('title'),
                                            "completed": td.get('completed')})
    con = "todo_all_employees" + ".json"
    with open(con, mode='w') as json_file:
        json.dump(data, json_file)
