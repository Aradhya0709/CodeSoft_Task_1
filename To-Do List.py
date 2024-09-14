# Simple Command-Line To-Do List Application

tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high/medium/low): ")
    tasks.append({"title": title, "description": description, "due_date": due_date, "priority": priority, "completed": False})
    print("Task added successfully.")

def view_tasks():
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['title']} - {task['description']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {status}")

def update_task():
    view_tasks()
    task_number = int(input("Enter task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["title"] = input("Enter new title: ")
        tasks[task_number]["description"] = input("Enter new description: ")
        tasks[task_number]["due_date"] = input("Enter new due date (YYYY-MM-DD): ")
        tasks[task_number]["priority"] = input("Enter new priority (high/medium/low): ")
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def mark_task_completed():
    view_tasks()
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
