from db.config import Base
from sqlalchemy import Column,String,Integer,Float,DateTime
from datetime import datetime

class Order(Base):
    __tablename__ = "order"
    
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    method = Column(String,nullable=False)
    amount = Column(Float,nullable=False)
    date = Column(DateTime,default=datetime.now())
    invoice_id = Column(Integer,nullable=False,autoincrement=True,unique=True)
    cust_id = Column(Integer,nullable=False)
    description = Column(String,nullable=False)
    
    
    