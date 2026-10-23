
import mysql.connector

print("1. Program started.", flush=True)

try:
    print("2. Connecting to MySQL...", flush=True)

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="todo_db",
        connection_timeout=5,
        use_pure=True
    )

    print("3. Connected successfully!", flush=True)

    connection.close()
    print("4. Connection closed.", flush=True)

except Exception as error:
    print("ERROR:", repr(error), flush=True)

