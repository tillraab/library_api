"""Books API Routes. Defines endpoints for managing library items and a health check."""
from api.routers import library_router, default_router
from database.library_connector import LibraryConnector
from definitions import BookIn, Author

from fastapi.responses import JSONResponse

library = LibraryConnector("database/library.db")

@library_router.post("/library")
async def create_library_item(book: dict[str, str]):
    """
    Create a new item in the library.
    """
    book_model = BookIn(**book)
    library.add_library_item(book_model)
    return JSONResponse(content={"message": "Item added successfully"}, status_code=201)

@library_router.get("/library")
async def read_library_items(author: str | None = None):
    """
    Retrieve all items in the library, or filter by author if provided.
    """

    if author:
        author_model = Author(author=author)
        items = library.get_library_items(author=author_model)
    else:
        items = library.get_library_items()
    return items

@default_router.get("/")
async def health_check():
    """
    Health check endpoint.
    """
    return JSONResponse(content={"status": "ok"}, status_code=200)