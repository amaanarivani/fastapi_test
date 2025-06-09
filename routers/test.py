from fastapi import APIRouter
from models.test import TestModel
from config.db import conn
from schemas.test import TestSchema

test = APIRouter()

@test.get("/test")
async def get_tests():
    tests = conn.py_test.test.find()
    return [TestSchema(result=str(test["_id"]), **test) for test in tests]

@test.post("/test")
async def create_test(test: TestModel):
    result = conn.py_test.test.insert_one(dict(test))
    return TestSchema(result=str(result.inserted_id), **test.dict())