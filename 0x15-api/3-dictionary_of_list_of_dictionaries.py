#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
import requests
import sys


def export_json():
    base_url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(base_url)
    if response.status_code == 200:
        users = response.json()
        todo_data = {}
        for user in users:
            user_id = user['id']
            username = user['username']
            tU = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
            user_todos = requests.get(tU).json()
            user_tasks = []
            for todo in user_todos:
                task = {
                        'username': username,
                        'task': todo['title'],
                        'completed': todo['completed']
                        }
                user_tasks.append(task)
            todo_data[user_id] = user_tasks

        # write to json data file
        with open('todo_all_employees.json', 'w') as f:
            json.dump(todo_data, f, indent=4)
    else:
        print("Error: Could not retrieve data")


if __name__ == '__main__':
    export_json()
