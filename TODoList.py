from datetime import *

tasks = []

try:
    file = open("tasks.txt", "r")
    tasks = file.readlines()
    file.close()

    for i in range(len(tasks)):
        tasks[i] = tasks[i].strip()

except:
    tasks = []

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # View tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    # Add task
    elif choice == "2":
        task = input("Enter task: ")
        now = datetime.now()

        time_stamp = now.strftime("%Y-%m-%d %H:%M")

        task_with_time = f"[{time_stamp}] {task}"

        tasks.append(task_with_time)

        file = open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()

        print("Task added!")

    # Delete task
    elif choice == "3":
        for i in range(len(tasks)):
            print(i + 1, tasks[i])

        user = input("Enter number to delete: ")

        if user.isdigit():
            num = int(user)

            if num >= 1 and num <= len(tasks):
                deleted_item = tasks.pop(num - 1)

                file = open("tasks.txt", "w")
                for t in tasks:
                    file.write(t + "\n")
                file.close()

                print(f"'{deleted_item}' deleted successfully!")
            else:
                print("Invalid input")
        else:
            print("Invalid number, please enter a valid number")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")