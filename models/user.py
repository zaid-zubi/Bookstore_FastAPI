from sqlalchemy import Column,String,Integer
from db.config import Base


class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String,nullable=False)
	email = Column(String,nullable=False,unique=True)
	password = Column(String,nullable=False)
	phone_first = Column(String,nullable=False,unique=True)
	address = Column(String,nullable=False)
	birth_date = Column(String,nullable=False)
	gender = Column(String,nullable=False)
	
	