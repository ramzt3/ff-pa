from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        from_attributes = True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime