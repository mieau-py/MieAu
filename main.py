
from todo import add_todo, list_todos, complete_todo, delete_todo


def main():
    while True:
        print("\n==============================")
        print("       MIEAU TO-DO LIST")
        print("==============================")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue

            description = input("Enter task description: ").strip()
            add_todo(title, description)

        elif choice == "2":
            list_todos()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_todo(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_todo(task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Thank you for using MieAu To-Do List!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()
