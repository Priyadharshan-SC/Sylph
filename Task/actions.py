from Task import store


# Function to add a task
def add_task():
    task=input("Enter a new task: ")
    id=1 if not store.tasks else store.tasks[-1]['id'] + 1
    status="pending"
    store.tasks.append({"id": id, "task": task, "status": status})
    print(f"Task added with ID: {id}")

# Function to show all task 
def show_tasks():
    if not store.tasks:
        print("No tasks available.")
    else:
        for task in store.tasks:
            print(f"ID: {task['id']}\nTask: {task['task']}\nStatus: {task['status']}")
        
# Function to delete task
def delete_task():
    task_id=int(input("Enter Task ID to delete"))
    store.tasks.pop(task_id-1)