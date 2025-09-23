from dataclasses import dataclass

@dataclass
class Task:
    description: str
    done: bool = False

def greet(user_name: str) -> str:
    return f"Hello, {user_name}"

def view_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t.done else "Not yet"
        print(f"{i}. Task: {t.description}, Status: {status}")

def add_task(tasks: list[Task], description: str) -> None:
    tasks.append(Task(description))

def mark_task(tasks: list[Task], task_number: int) -> None:
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1].done = True
        print(f"Task {task_number} marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks: list[Task], task_number: int) -> None:
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed.description}")
    else:
        print("Invalid task number.")

def view_done_tasks(tasks: list[Task]) -> None:
    done = [t for t in tasks if t.done]
    if not done:
        print("No tasks are done yet.")
        return
    print("\nDone tasks:")
    for i, t in enumerate(done, 1):
        print(f"{i}. {t.description} ✅")

def main() -> None:
    tasks: list[Task] = []
    user_name = input("Hello, what is your name? ")
    print(greet(user_name))

    while True:
        try:
            user_choice = int(input(
                "\nActions\n"
                "1- View your to-do list\n"
                "2- Add new task\n"
                "3- Mark task as done\n"
                "4- Delete task\n"
                "5- View done tasks\n"
                "0- Quit\n"
                "Enter your choice: "
            ))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match user_choice:
            case 0:
                print(f"Goodbye, {user_name}!")
                break
            case 1:
                view_tasks(tasks)
            case 2:
                new_task = input("Enter task description: ")
                add_task(tasks, new_task)
                view_tasks(tasks)
            case 3:
                try:
                    num = int(input("Task number to mark as done: "))
                    mark_task(tasks, num)
                except ValueError:
                    print("Please enter a valid number.")
            case 4:
                try:
                    num = int(input("Task number to delete: "))
                    delete_task(tasks, num)
                except ValueError:
                    print("Please enter a valid number.")
            case 5:
                view_done_tasks(tasks)
            case _:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
