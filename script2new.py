import requests
import json
import time

BASE_URL = "http://localhost:8000/tasks"

def get_all_tasks():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        tasks = response.json()
        if tasks:
            print("All tasks:")
            print(json.dumps(tasks[0], indent=2))  # Print first task
        else:
            print("No tasks found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching all tasks: {e}")
    print("-" * 30)

def get_specific_tasks(task_id):
    """Fetches and prints a specific task by ID from the API"""
    print(f"---- Getting task with ID: {task_id} ----")
    url = f"{BASE_URL}/{task_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        task = response.json()
        print(f"Task {task_id}:")
        print(json.dumps(task, indent=2))
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Task with ID '{task_id}' not found.")
        else:
            print(f"Error fetching task {task_id}: {e}")
    print("-" * 30)

# Call the functions
get_all_tasks()
get_specific_tasks("task123")