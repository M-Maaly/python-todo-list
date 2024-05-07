def add_task(task_list):
    tasks = input("Enter your task: ")
    task_list.append(tasks)
    print("Task added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
    else:
        for task in task_list:
            print(task)

def remove_task(task_list):
    if not task_list:
        print("No tasks to remove.")
    else:
        tasks = input("Remove any task: ")
        if tasks in task_list:
            task_list.remove(tasks)
            print(f"{tasks} is removed from the list.")
        else:
            print("Task not found.")

def main():
    task_list = []

    while True:
        user_action = input("Enter your action (add, view, remove, exit): ")

        if user_action == "add":
            add_task(task_list)
        elif user_action == "view":
            view_tasks(task_list)
        elif user_action == "remove":
            remove_task(task_list)
        elif user_action == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
