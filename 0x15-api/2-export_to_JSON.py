#!/usr/bin/python3
''' Gathers data from an API '''

if __name__ == "__main__":

    import requests
    import json
    import csv
    from sys import argv

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()
    username = users.get('username')
    
    user_id = int(argv[1])

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({str(user_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todos.json()
            if (todo['userId'] == user_id)]}, jsonfile)
