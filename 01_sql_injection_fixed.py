import sqlite3

DB = "week9_demo.db"


def initialise_database():
    conn = sqlite3.connect(DB)
    conn.execute("DROP TABLE IF EXISTS users")
    conn.execute("CREATE TABLE users (username TEXT, password TEXT)")
    conn.execute("INSERT INTO users VALUES (?, ?)", ("admin", "secret123"))
    conn.commit()
    return conn


conn = initialise_database()
username = input("Username: ")
password = input("Password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
print("\nSQL template:\n", query)
print("Parameters:", (username, password))

result = conn.execute(query, (username, password)).fetchone()
print("\nLOGIN SUCCESSFUL" if result else "\nLOGIN FAILED")
conn.close()
