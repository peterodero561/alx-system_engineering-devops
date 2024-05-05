#!/usr/bin/python3
'''Python script that, using this jsonplaceholder.typicode.com/,
for a given employee ID, returns information about
his/her TODO list progress'''
import requests
import sys


def get_ToDo_list(emp_id):
    '''Function to get the to do list'''
    base_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    response = requests.get(base_url)
    if response.status_code == 200:
        todos = response.json()

        # count completed tasks
        completed = [todo for todo in todos if todo['completed']]
        No_completed = len(completed)
        total_tasks = len(todos)

        # get employee name
        user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
        user_response = requests.get(user_url)
        emp_name = user_response.json()['name']

        # print output
        na = emp_name
        nc = No_completed
        tc = total_tasks
        print(
                f'Employee {na} is done with tasks {nc}/{tc}')
        for task in completed:
            print(f'\t{task["title"]}')
    else:
        print('Error: could not retrive data')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./0-gather_data_from_an_API.py <employee id>')
        sys.exit(1)

    emp_id = int(sys.argv[1])
    get_ToDo_list(emp_id)
