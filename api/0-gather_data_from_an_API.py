#!/usr/bin/python3
""" Method: Return information using REST API """
import requests
from sys import argv


def employee_statistics(employee_id: int):
    """ Method: Format employee information from input
    Arguments:
        - employee_id(int)
    Returns:
        - Employee data (complete + incomplete tasks)
    """
    base = "https://jsonplaceholder.typicode.com"

    employee_url = "{}/users/{}".format(base, employee_id)
    employee_request = requests.get(employee_url)
    if employee_request.status_code == 200:
        employee_data = employee_request.json()
        employee_name = employee_data.get('name')
    else:
        print("Employee not found...")

    incomplete_tasks = 0
    total_tasks = len(todos_data)
    todos_url = "{}/todos/".format(base)
    todos_request = requests.get(todos_url)
    if todos_request.status_code == 200:
        todos_data = todos_request.json()
    for todo in todos_data:
        if todo['completed'] is False:
            incomplete_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        incomplete_tasks,
        total_tasks
    ))


if __name__ == "__main__":
    employee_statistics()
