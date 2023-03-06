from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from db.config import get_db
from schema.user import Login,UserIn
from models.user import User

router = APIRouter()

@router.post("/login")
async def login(req: Login,db : Session = Depends(get_db)):
    email =req.email
    password = req.password
    q = db.query(User).filter_by(userEmail=email,userPass=password).first()
    if q:
        return "Login successfully..."
    else:
        raise HTTPException(400,"Invalid Username and Password")
    
@router.post("/signup/")
async def singup(req: UserIn,db: Session = Depends(get_db)):
                    New_user = User(**req.dict())
                    db.add(New_user)
                    db.commit()
                    db.refresh(New_user)
                    return New_user