from db.config import Base
from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from datetime import datetime

class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    AuthorId = Column(Integer,nullable=False)
    created_at = Column(DateTime,default=datetime.now())