from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.config import get_db
from schema.order import OrderIn
from schema.cust_response import Response
from repository.order import get,get_all,add,update,delete

router = APIRouter()

@router.post("/")
async def add_order(req: OrderIn,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=add(req,db))


@router.get("/{order_id}")
async def read_order(order_id: int,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get(order_id,db))


@router.get("/")
async def read_orders(db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=get_all(db))


@router.delete("/{order_id}")
async def cancel_order(order_id: int,db: Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=delete(order_id, db))

@router.put("/")
async def update_order(order_id: int,req: OrderIn,db:Session = Depends(get_db)):
    return Response(code=200, status="OK", message="Success fetch all data", result=update(order_id,req,db))



