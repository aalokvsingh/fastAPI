from sqlmodel import Session, select
from app.models.user import User, UserCreate
from app.core.security import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()

def create_user(db: Session, UserCreate: UserCreate):
    hashed_pw = get_password_hash(UserCreate.password)
    user = User(username=UserCreate.username, email=UserCreate.email, full_name=UserCreate.full_name, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    print("alok singh")
    user = get_user_by_username(db, username)
    print(user)
    if not user or not verify_password(password, user.hashed_password):
        print("error in verification")
        return None

    return user

