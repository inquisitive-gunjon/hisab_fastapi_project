from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from jose import JWTError, jwt #pip install python-jose pyjwt passlib
from passlib.context import CryptContext
from typing import List
from datetime import datetime, timedelta

# Replace 'mysql+pymysql://username:password@localhost/database' with your MySQL connection details
DATABASE_URL = "mysql+pymysql://root@localhost:3306/hishabproject"
SECRET_KEY = "your-secret-key"  # Replace with a strong secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True)
    email = Column(String(50))

Base.metadata.create_all(engine)

class UserBase(BaseModel):
    id: int
    username: str
    email: str

class UserList(BaseModel):
    users: List[UserBase]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# Dependency to get the database session
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

# Dependency to verify the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_jwt_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

app = FastAPI()

# Create a new user
@app.post("/users/", response_model=UserBase, dependencies=[Depends(verify_token)])
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
@app.get("/users/", response_model=UserList, dependencies=[Depends(verify_token)])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return {"users": users}

# ... (other endpoints)

# Endpoint to obtain a token
@app.post("/token", response_model=Token)
def login_for_access_token(username: str, password: str):
    # Validate the user's credentials (e.g., against a database)
    # For demonstration purposes, let's assume username="testuser" and password="testpassword"
    user_dict = {"sub": username, "scope": "me"}
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(user_dict, expires_delta=expires)


    
    return {"access_token": access_token, "token_type": "bearer"}
