#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
import requests


def get_employee_todo_progress(employee_id):
    '''exports data in json'''
    b_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(b_url)

    if response.status_code == 200:
        todos = response.json()

        # Get employee name
        u_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(u_url)
        username = user_response.json()['username']

        # Organize tasks for the employee
        user_tasks = []
        for todo in todos:
            task = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            user_tasks.append(task)

        # Write JSON data to file
        filename = f"{employee_id}.json"
        with open(filename, "w") as file:
            json.dump({employee_id: user_tasks}, file, indent=4)
    else:
        print("Error: Could not retrieve data")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
