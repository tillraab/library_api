""" Unittests for the Library API.

Execute vai 'python3 -m unittest discover -s test' in the project root directory.
"""

import sys
import os
from unittest.mock import patch
import sqlite3

# Patch sqlite3.connect globally before importing app
patch('sqlite3.connect', lambda db_path, *args, **kwargs: sqlite3.Connection(db_path, check_same_thread=False, *args, **kwargs)).start()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from fastapi.testclient import TestClient
from main import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_library(self):
        response = self.client.get("/library")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_library_by_author(self):
        response = self.client.get("/library", params={"author": "J.K. Rowling"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_post_library(self):
        data = {"author": "T. Raab", "name": "My Book"}
        response = self.client.post("/library", json=data)
        self.assertIn(response.status_code, [200, 201])
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Item added successfully")

if __name__ == "__main__":
    unittest.main()
