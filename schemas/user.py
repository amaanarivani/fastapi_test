from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    name: str
    email: str
    password: str
    is_active: bool = True