tasks = {
    "Complete assignment": "Pending",
    "Prepare presentation": "In Progress",
    "Submit project report": "Pending"
}
def display_tasks():
    print("\n--- PROJECT TASK BOARD ---")
    for task, status in tasks.items():
        print(f"{task} : {status}")
def update_task():
    task_name = input("Enter task name to update: ").strip()
    if task_name not in tasks:
        print("Task not found!")
        return
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    choice = input("Choose new status (1-3): ").strip()
    if choice == "1":
        tasks[task_name] = "Pending"
    elif choice == "2":
        tasks[task_name] = "In Progress"
    elif choice == "3":
        tasks[task_name] = "Completed"
    else:
        print("Invalid choice!")
        return
    print("Task status updated successfully.")
def main():
    while True:
        print("\n=== TASK BOARD MENU ===")
        print("1. Display Tasks")
        print("2. Update Task Status")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_tasks()
        elif choice == "2":
            update_task()
        elif choice == "3":
            print("Exiting Task Board.")
            break
        else:
            print("Invalid choice! Try again.")
main()
