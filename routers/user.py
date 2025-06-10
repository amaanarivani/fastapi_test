from fastapi import APIRouter
from models.user import UserModel
from config.db import conn
from schemas.user import UserSchema

user = APIRouter()

@user.post("/user")
async def create_user(user: UserModel):
    result = conn.py_test.user.insert_one(dict(user))
    return UserSchema(result=str(result.inserted_id), **user.dict())

@user.get("/user")
async def get_users():
    users = conn.py_test.user.find()
    return [UserSchema(result=str(user["_id"]), **user) for user in users]