#!/usr/bin/python3
""" Method: Export data in CSV format """
import requests
from sys import argv


def employee_statistics(employee_id):
    """ Method: Export data in CSV format
    (Comma-Separated Values)
    Arguments:
        - employee_id(int)
    Raises
        - ValueError - when employee_id is not provided.
        - TypeError - when employee_id is not type "int"
    Returns:
        - Employee data (CSV format)
    """
    if len(argv) < 2:
        raise ValueError("Please input employee id.")
    elif not isinstance(employee_id, int):
        raise TypeError("Employee id must be an integer.")
    else:
        employee_id = int(argv[1])

    """ Method: Build URL's """
    base = "https://jsonplaceholder.typicode.com"
    users = ("{}/users/".format(base))
    todos = ("{}/todos/".format(base))

    users_response = requests.get(users)
    if users_response.status_code == 200:
        username = users_response.json()
    else:
        print("GET request failed...")

    todos_response = requests.get(todos)
    if todos_response.status_code == 200:
        todo_list = todos_response.json()
    else:
        print("GET request failed...")

