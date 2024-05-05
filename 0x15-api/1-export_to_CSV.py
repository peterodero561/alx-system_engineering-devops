#!/usr/bin/python3
''' Python script to export data in the CSV format'''
import csv
import requests
import sys


def export_csv(emp_id):
    '''function to create csv'''
    base_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    response = requests.get(base_url)
    if response.status_code == 200:
        todos = response.json()

        # get employee name
        name_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
        user_response = requests.get(name_url)
        emp_name = user_response.json()['username']

        # create csv file
        filename = f'{emp_id}.csv'
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            for todo in todos:
                comp = str(todo['completed'])
                title = todo['title']
                writer.writerow([f'{emp_id}, {emp_name}, {comp}, {title}'])
    else:
        print("Error: Could not retrieve data")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <employee id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])
    export_csv(emp_id)
