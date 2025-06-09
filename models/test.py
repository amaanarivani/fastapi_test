from pydantic import BaseModel


class TestModel(BaseModel):
    title: str
    desc: str = None
    important: bool = False