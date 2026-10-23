
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "todo_db",
    "connection_timeout": 5,
    "use_pure": True,
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def add_todo(title, description=""):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO todos (title, description)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (title, description))
        connection.commit()

        print("Task added successfully!")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def list_todos():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, description, completed, created_at
            FROM todos
            ORDER BY id DESC
        """)

        tasks = cursor.fetchall()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n--- YOUR TO-DO LIST ---")

        for task in tasks:
            task_id, title, description, completed, created_at = task
            status = "Done" if completed else "Pending"

            print(f"\nID: {task_id}")
            print(f"Task: {title}")
            print(f"Description: {description or 'None'}")
            print(f"Status: {status}")
            print(f"Created: {created_at}")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def complete_todo(task_id):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE todos SET completed = TRUE WHERE id = %s",
            (task_id,)
        )
        connection.commit()

        if cursor.rowcount:
            print("Task marked as completed!")
        else:
            print("Task ID not found.")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def delete_todo(task_id):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM todos WHERE id = %s",
            (task_id,)
        )
        connection.commit()

        if cursor.rowcount:
            print("Task deleted successfully!")
        else:
            print("Task ID not found.")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

