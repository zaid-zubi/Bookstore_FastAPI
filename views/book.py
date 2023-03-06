from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.config import get_db
from schema.book import BookIn
from schema.cust_response import Response
from repository.book import get,get_all,add,update,delete

router = APIRouter()

@router.get("/")
async def read_books(db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get_all(db))

@router.get("/{book_id}")
async def get_book(book_id: int,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get(book_id, db))

@router.post("/")
async def add_book(req: BookIn,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=add(req,db))

@router.delete("/{book_id}")
async def dalete_book(book_id: int,db:Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=delete(book_id,db))

@router.put("/{book_id}")
async def update_book(book_id: int,req: BookIn,db:Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=update(book_id,req,db))
