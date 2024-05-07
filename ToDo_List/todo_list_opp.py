class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        tasks = input("Enter your task: ")
        self.task_list.append(tasks)
        print("Task added.")

    def view_tasks(self):
        if not self.task_list:
            print("No tasks to display.")
        else:
            for task in self.task_list:
                print(task)

    def remove_task(self):
        if not self.task_list:
            print("No tasks to remove.")
        else:
            tasks = input("Remove any task: ")
            if tasks in self.task_list:
                self.task_list.remove(tasks)
                print(f"{tasks} is removed from the list.")
            else:
                print("Task not found.")

    def main(self):
        while True:
            user_action = input("Enter your action (add, view, remove, exit): ")

            if user_action == "add":
                self.add_task()
            elif user_action == "view":
                self.view_tasks()
            elif user_action == "remove":
                self.remove_task()
            elif user_action == "exit":
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()
