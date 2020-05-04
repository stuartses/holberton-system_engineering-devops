#!/usr/bin/python3
"""Read data from the API JSONPlaceholder and export to json file
https://jsonplaceholder.typicode.com/

Getting data of all users

Resources: users, todos
"""

import csv
import json
import requests
from sys import argv


def get_tasks(usr_id):
    """ Make a request by usr_id and creates a dictionary

    Arguments:
             usr_id: integer with id of user
    Return:
           dictionaty with all tasks of the user
    """

    task_req = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(usr_id))
    task_list = task_req.json()

    task_dict_list = []
    for task in task_list:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = usr_username
        task_dict_list.append(task_dict)

    return task_dict_list


if __name__ == "__main__":
    usr_req = requests.get("https://jsonplaceholder.typicode.com/users")
    usr_list = usr_req.json()
    usr_dict = {}

    for usr in usr_list:
        usr_username = usr.get('username')
        usr_id = usr.get('id')
        usr_task_dict = get_tasks(usr_id)
        usr_dict[usr_id] = usr_task_dict

    with open("todo_all_employees.json", mode="w") as usr_file:
        usr_file.write(json.dumps(usr_dict))
