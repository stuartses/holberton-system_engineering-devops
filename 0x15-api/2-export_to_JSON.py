#!/usr/bin/python3
"""Read thata from the API JSONPlaceholder and create a json
https://jsonplaceholder.typicode.com/

Resources: users, todos
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    usr_req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1]))

    usr_username = usr_req.json().get('username')
    usr_id = usr_req.json().get('id')

    task_req = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    task_list = task_req.json()

    task_dict_list = []
    for task in task_list:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = usr_username
        task_dict_list.append(task_dict)

    usr_dict = {}
    usr_dict[usr_id] = task_dict_list
    print(json.dumps(usr_dict))
