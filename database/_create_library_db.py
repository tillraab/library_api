"""Helper script to create a SQLite database for a library system."""
import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    name TEXT NOT NULL
)
""")

# Sample data
entries = [
    ("J.K. Rowling", "Harry Potter and the Sorcerer's Stone"),
    ("J.R.R. Tolkien", "The Hobbit"),
    ("George Orwell", "1984"),
    ("Harper Lee", "To Kill a Mockingbird"),
    ("F. Scott Fitzgerald", "The Great Gatsby"),
    ("Jane Austen", "Pride and Prejudice"),
    ("Mark Twain", "Adventures of Huckleberry Finn"),
    ("Mary Shelley", "Frankenstein"),
    ("Leo Tolstoy", "War and Peace"),
    ("Homer", "The Odyssey"),
    ("Ernest Hemingway", "The Old Man and the Sea"),
    ("Gabriel Garcia Marquez", "One Hundred Years of Solitude"),
    ("Charles Dickens", "Great Expectations"),
    ("Emily Bronte", "Wuthering Heights"),
    ("Aldous Huxley", "Brave New World"),
    ("J.D. Salinger", "The Catcher in the Rye"),
    ("Miguel de Cervantes", "Don Quixote"),
    ("Fyodor Dostoevsky", "Crime and Punishment"),
    ("Herman Melville", "Moby Dick"),
    ("Virginia Woolf", "Mrs Dalloway"),
]

# Insert data
cursor.executemany("INSERT INTO library (author, name) VALUES (?, ?)", entries)

# Commit and close
conn.commit()
conn.close()
