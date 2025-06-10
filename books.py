from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Book
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/books")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for request data
class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    in_stock: bool

# Add a new book
@router.post("/", response_model=BookCreate)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Search books by title
@router.get("/search", response_model=List[BookCreate])
def search_books(title: str, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
    return books

# View book by ID
@router.get("/{book_id}", response_model=BookCreate)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

