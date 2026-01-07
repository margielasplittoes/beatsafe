from pydantic import BaseModel
from typing import Optional

class BeatBase(BaseModel):
    title: str
    bpm: int
    key: str
    genre: str

class BeatCreate(BeatBase):
    pass

class BeatResponse(BeatBase):
    id: int
    producer_id: int

    class Config:
        from_attributes = True
