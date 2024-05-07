list = []

while(True):
    user_action = input("Enter your action (add, view, remove, exit): ")

    if (user_action == "add"):
        tasks = input("Enter your task: ")
        list.append(tasks)
        print("task added.")
    elif (user_action == "view"):
        if not list:
            print("No tasks to display")
        else:
            for task in list:
                print(task)
    elif (user_action == "remove"):
        if not list:
            print("No tasks to display")
        else:
            tasks = input("Remove any task: ")
            if tasks in list:
                list.remove(tasks)
                print(f"{tasks} is removed from list.")
            else:
                print("Task not found.")
    elif (user_action == "exit"):
        break
    else:
        print("Invalid command.")

