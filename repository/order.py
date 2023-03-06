from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from db.config import get_db
from schema.order import OrderIn
from models.order import Order

def get_all(db:Session):
    orders = db.query(Order).all()
    return orders

def get(id: int,db: Session):
    order = db.query(Order).filter_by(id=id).first()
    return order

def add(req: OrderIn,db:Session):
    new_order = Order(**req.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def delete(id: int,db:Session):
    order = db.query(Order).filter_by(id=id).first()
    if order:
        db.delete(order)
        db.commit()
        return{
            "Message":"Order deleted successfully"
        }
    else:
        raise HTTPException(400,"Order not existed !")

def update(id:int,req: OrderIn,db: Session):
    order = db.query(Order).filter_by(id=id).first()
    order_data = req.dict(exclude_unset=True)
    for key,value in order_data.items():
        print(f"{key=} || {value=}")
        setattr(order,key,value)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order