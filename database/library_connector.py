"""Library Connector for SQLite Database. Connects the API to a SQLite database for managing library items."""
import sqlite3
from definitions import BookIn, Author


class LibraryConnector:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def get_library_items(self, author: Author | None = None):
        """
        Retrieve all library items or filter by author if provided.
        """

        if author:
            self.cursor.execute("SELECT id, author, name FROM library WHERE author = ?", (author.author,))
        else:
            self.cursor.execute("SELECT id, author, name FROM library")
        results = self.cursor.fetchall()
        return results

    def add_library_item(self, book: BookIn):
        """
        Add a new library item to the database.
        """
        self.cursor.execute(
            "INSERT INTO library (author, name) VALUES (?, ?)",
            (book.author, book.name)
        )
        self.conn.commit()

    def __del__(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()