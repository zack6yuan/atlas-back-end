#!/usr/bin/python3
""" Method: Return information using REST API """
import sys
from sys import argv
import requests

def employee_statistics(employee_id):
    """ Method: Format employee information from input
    Arguments:
        - employee_id(int)
    Raises:
        - ValueError - when employee_id is not provided.
        - TypeError - when employee_id is not type "int"
    Returns:
        - Employee data (complete + incomplete tasks)
    """
    if len(sys.argv) < 2:
        raise ValueError("Plase input empolyee id.")
    elif not isinstance(employee_id, int):
        raise TypeError("Employee id must be an integer.")
    else:
        employee_id = sys.argv[1]

    """ Method: Build URL's """
    root = "https://jsonplaceholder.typicode.com"
    employee_name = requests.get("https://jsonplaceholder.typicode.com/user/{}".format(employee_id)).json()
    complete = requests.get("https://jsonplaceholder.typucode.com/user/{}/complete".format*(employee_id)).json()
    incomplete = requests.get("https://jsonplaceholder.typicode.com/user/{}/incomplete".format(employee_id)).json()

    """ Method: Return update """
    print("Employee {} is done with tasks {}/{}".format(employee_name, complete, incomplete))


    if __name__ == "__main__":
        employee_statistics()