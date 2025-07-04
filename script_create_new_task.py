import requests
import json
import time

BASE_URL = "http://localhost:8000/tasks"

def partial_update_task():


def create_new_task():
    """ Creates a new taks by sending a POST request to the API"""
    print("----Createing a new task----")
    new_task_data = {
        "title": "Plan weekend trip2",
        "description": "Reserach, destination, book flights, arrange",
        "status": "pending",
        "dueDate": "2025-07-15"
        }
    try: 
        response = requests.post(BASE_URL, json=new_task_data)
        response.raise_for_status() # Raise an exception for HTTP
        created_task = response.json()
        print("Task created successfully:")
        print(json.dumps(created_task, indent=2))


    except requests.exceptions.HTTPError as e:
        print(f"Error creating task: {e}")
        if e.response.status_code == 400:
            print(f"Bad Request {e.response.json().get('error', 'unknown')}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Drror connecting to API: {e}")

create_new_task()