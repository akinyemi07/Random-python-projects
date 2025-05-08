import os

FILENAME = "tasks.txt"

def show_tasks():
    if not os.path.exists(FILENAME):
        print("\nNo tasks found.")
        return
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.strip()}")
    else:
        print("\nNo tasks found.")

def add_task():
    task = input("Enter your new task: ")
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"Removed task: {removed.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

