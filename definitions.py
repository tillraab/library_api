"""Pydantic models for the Books API."""
from pydantic import BaseModel

class BookIn(BaseModel):
    author: str
    name: str

class Author(BaseModel):
    author: str