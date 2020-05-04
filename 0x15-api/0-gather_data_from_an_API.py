#!/usr/bin/python3
"""Read thata from the API JSONPlaceholder
https://jsonplaceholder.typicode.com/

Resources: users, todos
"""

import requests
from sys import argv

if __name__ == "__main__":
    usr_req = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1]))

    usr_name = usr_req.json().get('name')

    task_req = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    task_list = task_req.json()

    count_tasks = 0
    count_done = 0
    done_list = []
    for task in task_list:
        count_tasks += 1
        if task.get('completed') is True:
            count_done += 1
            done_list.append("\t {}".format(task.get('title')))

    print("Employee {} is done with tasks({}/{}):".
          format(usr_name, count_done, count_tasks))

    print(*done_list, sep='\n')
