import os

def load_tasks():
    if not os.path.exists("dodol.txt"):
        return []

    with open("dodol.txt", "r", encoding="utf-8") as file:
        return [task.rstrip("\n") for task in file]


def save_tasks(tasks):
    with open("dodol.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()
while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        print("Exiting...")
        break

    if choice == "1":
        task = input("Enter your task: ").strip()

        if task :
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        else:
            print("Task not found!")

    elif choice == "2":
        print("Showing tasks...")

        if not tasks:
            print("Task not found!")
        else:
            for task in tasks:
                print(task)

    elif choice == "3":
        print("Deleting task...")

        if not tasks:
            print("Task not found!")
        else :
            for index, task in enumerate(tasks, start=1):
                print(index, task)
            try:
                number = int(input("Enter a number: "))

                if number > len(tasks) or number < 1:
                    print("Task number out of range!")
                else:
                    tasks.pop(number - 1)
                    save_tasks(tasks)
                    print("Task deleted!")
            except ValueError:
                print("Please enter a number!")