todo_list = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif choice == '2':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Please enter a number between 1 and 4.")

