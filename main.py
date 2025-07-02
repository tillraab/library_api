"""Books API main application entry point."""
from fastapi import FastAPI
from api.routes import library_router, default_router

app = FastAPI()
app.include_router(library_router)
app.include_router(default_router)