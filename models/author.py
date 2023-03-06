from db.config import Base
from sqlalchemy import Column, String, Integer


class Author(Base):
    __tablename__ = "author"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    gender = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    phone = Column(String,nullable=False,unique=True)
    