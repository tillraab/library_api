import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

cursor.execute("SELECT id, author, name FROM library")
rows = cursor.fetchall()

headers = ["ID", "Author", "Name"]
print(tabulate(rows, headers, tablefmt="grid"))

conn.close()
