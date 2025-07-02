""" Unittests for the library connector.

Execute via 'python3 -m unittest discover -s test' in the project root directory.
"""

import unittest
import os
import sqlite3
from database.library_connector import LibraryConnector
from definitions import BookIn, Author

class TestLibraryConnector(unittest.TestCase):
    TEST_DB = 'test_library.db'

    def setUp(self):
        # Create a fresh test database
        if os.path.exists(self.TEST_DB):
            os.remove(self.TEST_DB)
        self.conn = sqlite3.connect(self.TEST_DB)
        self.conn.execute('''CREATE TABLE library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            name TEXT NOT NULL
        )''')
        self.conn.commit()
        self.conn.close()
        self.connector = LibraryConnector(self.TEST_DB)

    def tearDown(self):
        del self.connector
        if os.path.exists(self.TEST_DB):
            os.remove(self.TEST_DB)

    def test_add_and_get_library_item(self):
        book = BookIn(author="Test Author", name="Test Book")
        self.connector.add_library_item(book)
        items = self.connector.get_library_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], "Test Author")
        self.assertEqual(items[0][2], "Test Book")

    def test_get_library_items_by_author(self):
        book1 = BookIn(author="Author1", name="Book1")
        book2 = BookIn(author="Author2", name="Book2")
        self.connector.add_library_item(book1)
        self.connector.add_library_item(book2)

        author1 = Author(author="Author1")
        items = self.connector.get_library_items(author=author1)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], "Author1")
        self.assertEqual(items[0][2], "Book1")

if __name__ == "__main__":
    unittest.main()
