from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Hi! Welcome to my bookstore API"}

