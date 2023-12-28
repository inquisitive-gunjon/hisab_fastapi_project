from fastapi import FastAPI
from app.api.users import endpoints as user_endpoints

app = FastAPI()

app.include_router(user_endpoints.router, prefix="/users", tags=["users"])
