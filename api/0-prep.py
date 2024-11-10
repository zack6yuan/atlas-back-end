#!/usr/bin/python3
""" Method: Return information using REST API """
import requests
from sys import argv


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
    if __name__ == "__main__":
        if not isinstance(employee_id, int):
            raise TypeError("Employee ID must be an integer.")
        elif len(argv) < 2:
            raise ValueError("Please enter Employee ID.")
        employee_id = int(argv[0])

        base = "https://jsonplaceholder.typicode.com"

        user = "{}/users".format(base)
        user_response = requests.get(user)
        if user_response.status_code == 200:
            username = user_response.json()
        else:
            print("Get request failed...")
        
        todo = "{}/todos".format(base)
        todo_response = requests.get(todo)
        if todo_response.status_code == 200:
            todo_total = todo_response.json()
        else:
            print("Get request failed...")

    
    complete = 0
    incomplete = 0
    for todo in todo_total:
        if todo == "completed":
            complete += 1
        else:
            incomplete += complete

    print(f"Employee {username} is done with tasks({incomplete}/{complete})")
