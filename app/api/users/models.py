from pydantic import BaseModel
from typing import List


# Create a Pydantic model for the User
class UserCreate(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Change 'from_attributes' to 'orm_mode'

class UserResponse(BaseModel):
    # Define the response model
    id: int
    username: str
    email: str

# Pydantic model for the list of users
class UserList(BaseModel):
    users: List[UserCreate]

    class Config:
        orm_mode = True  # Change 'from_attributes' to 'orm_mode'

