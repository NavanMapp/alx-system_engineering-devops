import sys
import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    if response_user.status_code != 200 or response_todos.status_code != 200:
        print("Failed to retrieve data from the API.")
        return

    user_data = response_user.json()
    todos_data = response_todos.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])
    done_task_titles = [todo['title'] for todo in todos_data if todo['completed']]

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in done_task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

# #!/usr/bin/python3
# """Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""
# import json
# import requests
# import sys


# base_url = 'https://jsonplaceholder.typicode.com'

# if __name__ == "__main__":

#     user_id = sys.argv[1]

#     # get user info e.g https://jsonplaceholder.typicode.com/users/1/
#     user_url = '{}/users?id={}'.format(base_url, user_id)
#     # print("user url is: {}".format(user_url))

#     # get info from api
#     response = requests.get(user_url)
#     # pull data from api
#     data = response.text
#     # parse the data into JSON format
#     data = json.loads(data)
#     # extract user data, in this case, name of employee
#     name = data[0].get('name')
#     # print("id is: {}".format(user_id))
#     # print("name is: {}".format(name))

#     # get user info about todo tasks
#     # e.g https://jsonplaceholder.typicode.com/users/1/todos
#     tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
#     # print("tasks url is: {}".format(tasks_url))

#     # get info from api
#     response = requests.get(tasks_url)
#     # pull data from api
#     tasks = response.text
#     # parse the data into JSON format
#     tasks = json.loads(tasks)

#     # initialize completed count as 0 and find total number of tasks
#     completed = 0
#     total_tasks = len(tasks)

#     # initialize empty list for completed tasks
#     completed_tasks = []
#     # loop through tasks counting number of completed tasks
#     for task in tasks:

#         if task.get('completed'):
#             # print("The tasks are: {}\n".format(task))
#             completed_tasks.append(task)
#             completed += 1

#     # print the output in the required format
#     print("Employee {} is done with tasks({}/{}):"
#           .format(name, completed, total_tasks))
#     for task in completed_tasks:
#         print("\t {}".format(task.get('title')))