#!/usr/bin/python3
" export information about the employee "
import json
from requests import get

if __name__ == "__main__":
    " TODO list of all employees progress JSON file "
    user_req = get('https://jsonplaceholder.typicode.com/users').json()
    todo_req = get('https://jsonplaceholder.typicode.com/todos').json()
    dict_json = {}
    for i_user_req in user_req:
        list_task = []
        user_id = i_user_req.get('id')
        user_username = i_user_req.get('username')
        for item in todo_req:
            if user_id == item.get('userId'):
                info = {
                    'task': item.get('title'),
                    'completed': item.get('completed'),
                    'username': user_username,
                }
                list_task.append(info)
            dict_user = {user_id: list_task}
        dict_json.update(dict_user)
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dict_json, json_file)
