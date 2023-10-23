#!/usr/bin/python3
''' Gathers data from an API '''

if __name__ == "__main__":

    import requests
    import json
    import csv
    from sys import argv

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    user_id = int(argv[1])
    
    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos.json():
            if (todo['userId'] == user_id):
                writer.writerow([user_id, users.json()[user_id - 1]['username'],
                        todo['completed'], todo['title']])
