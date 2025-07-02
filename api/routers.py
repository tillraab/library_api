"""Define API routers for the Books API. 

The default router handles general endpoints, while the library router manages library-specific operations."""
from fastapi import APIRouter

default_router = APIRouter(tags=["default"])
library_router = APIRouter(tags=["library"])
