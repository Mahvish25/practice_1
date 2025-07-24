print("Welcome to the TO-DO App Console-Based")
task_list = []

while True:
    print("\n Welcome to the TO-DO App")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Choose an option 1-4: "))

    if choice == 1:
        task = input("Enter the task: ")
        task_list.append(task)
        print("Task Added Successfully")

    elif choice == 2:
        if not task_list:
            print("No tasks to show")
        else:
            print("Your tasks")
            for i, t in enumerate(task_list, start=1):
                print(f"{i}.{t}")

    elif choice == 3:
        if not task_list:
            print("No tasks to delete")
        else:
            print("Your tasks")
            for i, t in enumerate(task_list, start=1):
                print(f"{i}. {t}")
            del_index = int(input("Enter the task to delete"))
            if 1 <= del_index <= len(task_list):
                task_list.pop(del_index - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid input please choose a number from 1-4.")
