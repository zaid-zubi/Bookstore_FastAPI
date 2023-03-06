from sqlalchemy.orm import Session
from fastapi import Depends
from db.config import get_db
from schema.book import BookIn
from models.book import Book


def get_all(db: Session):
    books = db.query(Book).all()
    return books

def get(book_id: int, db: Session):
    book = db.query(Book).filter_by(id=book_id).first()
    return book

def delete(id: int,db: Session):
    book = db.query(Book).filter_by(id=id).first()
    db.delete(book)
    db.commit()
    return {
        "Message":"Book deleted successfully"
    }

def add(req: BookIn,db:Session):
    new_book = Book(**req.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update(book_id: int, req: BookIn,db: Session):
    book = db.query(Book).filter_by(id=book_id).first()
    book_data = req.dict(exclude_unset=True)
    for key, value in book_data.items():
        print(f"key: {key} || Value : {value}")
        setattr(book, key, value)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book