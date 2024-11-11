#!/usr/bin/python3
""" Method: Return information using REST API """
import json
import requests
from sys import argv


def employee_statistics(employee_id: int):
    """ Method: Format employee information from input
    Arguments:
        - employee_id(int)
    Returns:
        - Employee data (complete + total tasks)
    """
    base = "https://jsonplaceholder.typicode.com"

    employee_url = "{}/users/{}".format(base, employee_id)
    employee_request = requests.get(employee_url)
    if employee_request.status_code == 200:
        employee_data = employee_request.json()
        employee_name = employee_data.get('name')
    else:
        print("Employee not found...")
        return

    

    complete_tasks = 0
    total_tasks = 0
    # filter tasks based on the specific user.
    todos_url = "{}/users/{}/todos".format(base, employee_id)
    todos_request = requests.get(todos_url)
    if todos_request.status_code == 200:
        todos_data = todos_request.json()
        total_tasks = len(todos_data)
        for todo in todos_data:
            if todo['completed'] is True:
                complete_tasks += 1


if __name__ == "__main__":
    if len(argv) < 2:
        print("Employee ID not found...")
    else:
        try:
            employee_id = int(argv[1])
            employee_statistics(employee_id)
        except ValueError:
            print("Please enter Employee ID as an integer.")
