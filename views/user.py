from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.config import get_db
from schema.user import UserIn
from schema.cust_response import Response
from repository.user import get,get_all,update,delete,add

router = APIRouter()

@router.get("/")
async def show_users(db:Session = Depends(get_db)):
	return  Response(code=200,status="OK",message="Success fetch all data",result=get_all(db))

@router.get("/{id}")
async def show_User(id: int,db: Session = Depends(get_db)):
	return Response(code=200,status="OK",message="Success fetch all data",result=get(id,db))

@router.post("/")
async def add_User(user: UserIn,db: Session = Depends(get_db)):
	return Response(code=200,status="OK",message="Success fetch all data",result=add(user,db))
	

@router.delete("/{user_id}")
async def remove_user(user_id: int,db: Session = Depends(get_db)):
	return Response(code=200,status="OK",message="Success fetch all data",result=delete(user_id,db))


@router.put("/{user_id}")
async def update_user(user_id: int,req: UserIn,db: Session = Depends(get_db)):
	return Response(code=200,status="OK",message="Success fetch all data",result=update(user_id,req,db))

