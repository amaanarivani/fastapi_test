from pydantic import BaseModel


class TestModel(BaseModel):
    id: str
    title: str
    desc: str = None
    important: bool = False