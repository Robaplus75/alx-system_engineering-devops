#!/usr/bin/python3
''' Gathers data from an API '''

if __name__ == "__main__":

    import requests
    import json
    import csv
    from sys import argv

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    with open("todo_all_employees.json", "w") as jsonfile:
        for user_id in range(1, 11):
            users = requests.get(
                    ("https://jsonplaceholder.typicode"
                        + f".com/users/{user_id}")).json()
            username = users.get('username')
            json.dump({str(user_id): [
                {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in todos.json()
                if (todo['userId'] == user_id)]}, jsonfile)
