from fastapi import FastAPI
import models
from database import engine
from books import router as book_router
from root import router as root_router

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include routes from other files
app.include_router(book_router)
app.include_router(root_router)
