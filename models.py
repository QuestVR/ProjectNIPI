from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    array: List[str]

class SessionResult(BaseModel):
    session_id: str
    result: int