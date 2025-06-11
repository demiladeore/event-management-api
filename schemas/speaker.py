from pydantic import BaseModel

class Speaker(BaseModel):
    id: str
    name: str
    topic: str