from fastapi import FastAPI,Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Union,Annotated,List
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from database import create_db_and_tables, get_session
from model import User, UserCreate, UserUpdate

app = FastAPI()

# Create User
@app.post("/user/", response_model=User)
def create_user(*, session: Session = Depends(get_session), UserCreate: UserCreate):
    # In a real application, you would hash the password here
    hashed_password = UserCreate.password + "_hashed" # Placeholder for hashing
    db_user = User(username=UserCreate.username, email=UserCreate.email, full_name=UserCreate.full_name, hashed_password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users")
def get_users(session:Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

# Read Single User
@app.get("/users/{user_id}", response_model=User)
def read_user(*, session: Session = Depends(get_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User
@app.patch("/users/{user_id}", response_model=User)
def update_user(*, session: Session = Depends(get_session), user_id: int, user_in: UserUpdate):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user_in.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        if key == "password" and value:
            setattr(db_user, "hashed_password", value + "_hashed") # Placeholder for hashing
        else:
            setattr(db_user, key, value)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# Delete User
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(*, session: Session = Depends(get_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}
    
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None =None
#     disabled: bool | None =None



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

# @app.get("user/me")
# async def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("item/")
async def read_item1(token:Annotated[str, Depends(oauth2_scheme)]):
    return {"token":token}    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}