from pydantic import BaseModel

class UserModel(BaseModel):
    id: str
    name: str
    email: str
    password: str
    is_active: bool = True