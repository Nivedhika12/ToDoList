import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    print("Task added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return

    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i+1}. {status} {task['description']}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted.")
    else:
        print("Invalid task index.")


tasks = load_tasks()  # Load tasks at the beginning.

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save and Exit")  # Save before quitting.
    print("6. Exit (without saving)")

    choice = input("Enter your choice: ")

    try:
        choice = int(choice)
        if choice == 1:
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == 2:
            list_tasks(tasks)
        elif choice == 3:
            index = int(input("Enter task index to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == 4:
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == 5:
            save_tasks(tasks)  # Save the tasks
            break
        elif choice == 6:
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")