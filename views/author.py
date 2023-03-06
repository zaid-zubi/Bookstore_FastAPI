from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.config import get_db
from schema.author import AuthorIn
from schema.cust_response import Response
from repository.author import  get,get_all,add,update,delete

router = APIRouter()

@router.get("/")
async def read_authors(db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get_all(db))

@router.get("/{author_id}")
async def read_author(author_id: int, db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get(author_id,db))

@router.post("/")
async def add_new_author(req: AuthorIn,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=add(req,db))

@router.delete("/{author_id}")
async def delete_author(author_id: int,db:Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=delete(author_id,db))

@router.put("/{author_id}")
async def update_author(author_id: int,req: AuthorIn, db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=update(author_id,req,db))