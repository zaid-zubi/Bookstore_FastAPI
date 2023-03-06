from pydantic import BaseModel,EmailStr,validator

class AuthorIn(BaseModel):
    username: str
    gender: str
    email: EmailStr
    phone: str
    
    @validator('gender')
    def validate_gender(cls,v: str):
        if "male"  ==  v.lower() or "female" == v.lower():
            return v.lower()
        return ValueError("Invalid gender")

    
    

