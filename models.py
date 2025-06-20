from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)
    in_stock = Column(Boolean)

