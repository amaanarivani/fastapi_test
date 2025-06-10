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

@test.delete("/test/{test_id}")
async def delete_test(test_id: str):
    result = conn.py_test.test.delete_one({"id": test_id})
    if result.deleted_count == 1:
        return {"message": "Test deleted successfully"}
    else:
        return {"message": "Test not found"}
    

@test.put("/test/{test_id}")
async def update_test(test_id: str, test: TestModel):
    result = conn.py_test.test.update_one({"id": test_id}, {"$set": dict(test)})
    if result.modified_count == 1:
        return TestSchema(result=test_id, **test.dict())
    else:
        return {"message": "Test not found or no changes made"}