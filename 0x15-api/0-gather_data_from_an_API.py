#!/usr/bin/python3
" get a information about the employee "
from requests import get
from sys import argv

if __name__ == "__main__":
    " TODO list of progress "
    list_title = []
    user_req = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(argv[1])).json()
    todo_req = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(argv[1])).json()
    for item in todo_req:
        if item.get('completed'):
            list_title.append(item.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(user_req.get('name'), len(list_title), len(todo_req)))
    for each in list_title:
        print('\t {}'.format(each))
