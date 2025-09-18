from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username:str = Field(index=True,unique=True)
    email:str = Field(unique=True)
    full_name: Optional[str] = None
    

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

class Token(SQLModel):
    access_token: str
    token_type: str
