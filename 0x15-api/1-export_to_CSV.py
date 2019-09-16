#!/usr/bin/python3
" export information about the employee "
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    " TODO list of progress .csv "
    list_title = []
    user_req = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(argv[1])).json()
    todo_req = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(argv[1])).json()
    id = argv[1]
    user_id = user_req.get('id')
    user_username = user_req.get('username')
    with open(id + '.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_NONNUMERIC)
        for item in todo_req:
            writer.writerow([str(user_id), user_username,
                             str(item.get('completed')), item.get('title')])
