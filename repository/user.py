from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from db.config import get_db
from schema.user import UserIn
from models.user import User

def get_all(db: Session):
	users = db.query(User).all()
	return users

def get(id: int,db: Session):
	user = db.query(User).filter_by(id=id).first()
	if user:
		return user
	else:
		raise HTTPException(400,"User not found")

def add(req: UserIn,db: Session):
	new_user = User(**req.dict())
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user


def delete(id: int,db: Session):
	user = db.query(User).filter_by(id=id).first()
	if user:
		db.delete(user)
		db.commit()
		return {
			"Message": "User deleted successfully"
		}
	else:
		raise HTTPException(400,"User not existed")

def update(id: int,req: UserIn,db: Session):
	user = db.query(User).filter_by(id=id).first()
	user_data = req.dict(exclude_unset=True)
	for key, value in user_data.items():
		print(f"key: {key} || Value : {value}")
		setattr(user, key, value)
	db.add(user)
	db.commit()
	db.refresh(user)
	return user

