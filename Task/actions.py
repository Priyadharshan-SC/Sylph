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

#Function to update task status
def update_task_status():
    task_id=int(input("Enter Task ID to update status: "))
    new_status=input("Enter new status (pending/completed): ").strip().lower()
    if new_status in ["pending", "completed"]:
        store.tasks[task_id-1]['status']=new_status
        print(f"Task ID {task_id} status updated to {new_status}.")
    else:
        print("Invalid status. Please enter 'pending' or 'completed'.")

# Function to sumarize tasks
def summarize_tasks():
    total_tasks=len(store.tasks)
    pending_task=len([task for task in store.tasks if task['status']=="pending"])
    completed_task=len([task for task in store.tasks if task['status']=="completed"])
    print(f"Total Tasks: {total_tasks}")
    print(f"Pending Tasks: {pending_task}")
    print(f"Completed Tasks: {completed_task}")