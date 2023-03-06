from fastapi import FastAPI
from routes import author_router,auth_router,order_router,user_router,book_router
from db.config import engine
from models.user import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router,prefix="/auth",tags=['Auth'])
app.include_router(user_router,prefix="/user",tags=['User'])
app.include_router(book_router,prefix="/book",tags=['Book'])
app.include_router(order_router,prefix="/order",tags=['Order'])
app.include_router(author_router,prefix="/author",tags=['Author'])

