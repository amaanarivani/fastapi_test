from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from routers.test import test
from routers.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test)
app.include_router(user)


@app.get("/")
async def root():
    return {"message": "My First FastAPI App"}

# class Item(BaseModel):
#     name: str
#     price: float | None = None
#     is_offer: bool = None

# @app.post("/items")
# async def create_item(item: Item):
#     print(item)
#     return item

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# users_items = [
#     {
#         "id": 1,
#         "name": "Rick Sanchez",
#         "email": "rick@example.com"
#     },
#     {
#         "id": 2,
#         "name": "Mike Tyson",
#         "email": "mike@example.com"
#     },
#     {
#         "id": 3,
#         "name": "Alex Trebek",
#         "email": "alex@example.com"
#     },
# ]

# @app.get("/user-details")
# async def get_user_details():
#     return users_items

# @app.get("/users")
# async def read_item():
#     return ["Ricky", "Morty", "Summer", "Beth", "Jerry"]


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
