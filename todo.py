tasks = []  # this is our empty to-do list

while True:  # keeps running
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):  # show tasks with numbers
            print(f"{i}. {task}")
    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)  # add task to list
        print("Task added!")
    elif choice == "3":
        num = int(input("Enter the task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Goodbye 👋")
        break  # stop the loop
    else:
        print("Please choose a number between 1 and 4!")

     