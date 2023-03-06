from fastapi import Depends
from sqlalchemy.orm import Session
from db.config import get_db
from schema.author import AuthorIn
from models.author import Author


def get(author_id: int,db: Session):
    author = db.query(Author).filter_by(id=author_id).first()
    return author

def get_all(db: Session):
    authors = db.query(Author).all()
    return authors

def add(req: AuthorIn,db: Session):
    newAuthor = Author(**req.dict())
    db.add(newAuthor)
    db.commit()
    db.refresh(newAuthor)
    return newAuthor

def delete(author_id: int,db: Session):
    author = db.query(Author).filter_by(id=author_id).first()
    db.delete(author)
    db.commit()
    return {
        "Message":"Author deleted successfully"
    }
def update(author_id: int,req: AuthorIn,db: Session):
    author = db.query(Author).filter_by(id=author_id).first()
    author_data = req.dict(exclude_unset=True)
    for key, value in author_data.items():
        print(f"key: {key} || Value : {value}")
        setattr(author, key, value)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author