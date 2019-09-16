#!/usr/bin/python3
" export information about the employee "
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    " TODO list of progress JSON file "
    user_req = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(argv[1])).json()
    todo_req = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(argv[1])).json()
    id = argv[1]
    list_task = []
    user_id = user_req.get('id')
    user_username = user_req.get('username')
    for item in todo_req:
        info = {
            'task': item.get('title'),
            'completed': item.get('completed'),
            'username': user_username,
        }
        list_task.append(info)
    dict_json = {user_id: list_task}
    with open(id + '.json', 'w') as json_file:
        json.dump(dict_json, json_file)
