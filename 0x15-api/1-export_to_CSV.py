#!/usr/bin/python3
"""Read thata from the API JSONPlaceholder and create a csv file
https://jsonplaceholder.typicode.com/

Resources: users, todos
"""

import csv
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

    with open(argv[1] + '.csv', mode='w+') as usr_file:
        usr_writer = csv.writer(usr_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in task_list:
            usr_writer.writerow([usr_id, usr_username, task.get('completed'),
                                 task.get('title')])
