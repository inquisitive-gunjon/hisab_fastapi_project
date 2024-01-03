from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from jose import JWTError, jwt #pip install python-jose pyjwt passlib
from passlib.context import CryptContext
from typing import List, Annotated
from datetime import datetime, timedelta
from starlette import status
from database import SessionLocal
from models import Users
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dotenv import load_dotenv
import os


load_dotenv()

router =  APIRouter(
    prefix= '/auth',
    tags=['auth']
)

# SECRET_KEY = 'super-secret-6FDFBB8F-2909-4565-85EA-3F685784355E'
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class CreateUserRequest(BaseModel):
    username: str
    email:str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_bd)]

@router.post("/sign_up", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request:CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )

    db.add(create_user_model)
    db.commit()

@router.post("/sign_in", response_model= Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm, Depends()],db:db_dependency):
    user=authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate user.")
    token = create_access_token(user.username,user.id,timedelta(minutes=20))

    return {'access_token': token, 'token_type':'bearer'}


def authenticate_user(username:str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()

    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username:str, user_id: int,expires_delta: timedelta):
    encode = {"sub":username,"id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp":expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)