#!/usr/bin/python3
''' Gathers data from an API '''

if __name__ == "__main__":

    import requests
    import json
    from sys import argv

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    completed = 0
    tasks = 0
    user_id = int(argv[1])

    for todo in todos.json():
        if (todo['userId'] == user_id):
            if (todo['completed'] is True):
                completed += 1
                tasks += 1
            else:
                tasks += 1

    print("Employee {} is done with tasks({}/{})".format(
        users.json()[user_id - 1]['name'], completed, tasks))

    for task in todos.json():
        if (task['userId'] == user_id and task['completed'] is True):
            print("\t " + task['title'])
