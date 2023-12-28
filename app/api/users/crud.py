from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.api.users.models import UserCreate
from app.models import User

def create_user(username: str, email: str, db: SessionLocal):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
