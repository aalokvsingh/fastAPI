from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from app.models.user import Token, UserCreate
from app.crud import user as crud_user
from app.db.session import get_session as get_db
from app.core import security, config

router = APIRouter()

@router.post("/signup")
def signup(user_in: UserCreate, db: Session = Depends(get_db)):    
    existing_user = crud_user.get_user_by_username(db, user_in.username)
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = crud_user.create_user(db, user_in)
    token = security.create_access_token(
        {"sub": user.username},
        expires_delta=timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = security.create_access_token(
        {"sub": user.email},
        expires_delta=timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}
