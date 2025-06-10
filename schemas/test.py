from pydantic import BaseModel

class TestSchema(BaseModel):
    id: str
    title: str
    desc: str = None
    important: bool = False

    
# def testEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "title": item["title"],
#         "desc": item(["desc"]) if "desc" in item else None,
#         "important": item(["important"]) if "important" in item else False
#     }