from pydantic import BaseModel,Field,validator

class BookIn(BaseModel):
    title: str = Field(...,min_length=4)
    price: float
    AuthorId: int
    @validator("title")
    def validate_title(cls,v):
        if len(v) < 3:
            return ValueError("Title can't be less than three letters")
        if len(v) > 50:
            return ValueError("Title can't be more than 50")
        return v
