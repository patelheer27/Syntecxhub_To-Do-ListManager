import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

# File Handling Functions
# -----------------------------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("\nError reading task file. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("\nError saving tasks.")


# Task Logic Functions
# -----------------------------
def add_task(tasks):
    print("\n--- Add New Task ---")
    title = input("Task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tag = input("Tag (optional): ").strip()
    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()

    # Validate date if entered
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return

    task = {
        "title": title,
        "done": False,
        "tag": tag,
        "due_date": due_date
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    print("\n========== TASK LIST ==========")

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "✖ Pending"

        print(f"\n{index}. {task['title']}")
        print(f"   Status   : {status}")

        if task.get("tag"):
            print(f"   Tag      : {task['tag']}")

        if task.get("due_date"):
            print(f"   Due Date : {task['due_date']}")

    print("\n================================")


def mark_task_done(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to mark as done: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"🗑 Task '{removed['title']}' deleted successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# User Interface
# -----------------------------
def display_menu():
    print("\n====================================")
    print("       TASK MANAGER SYSTEM")
    print("====================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("====================================")


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using Task Manager. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# Run Program
if __name__ == "__main__":
    main()