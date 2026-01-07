from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from database import get_db

router = APIRouter(
    prefix = "/beats",
    tags = ["beats"]
)

@router.post("/", response_model=schemas.BeatResponse)
def create_beat(
    beat: schemas.BeatCreate,
    db: Session = Depends(get_db)
):
    new_beat = models.Beat(
        title=beat.title,
        bpm=beat.bpm,
        key=beat.key,
        genre=beat.genre,
        producer_id = 1

    )
    db.add(new_beat)
    db.commit()
    db.refresh(new_beat)
    return new_beat

@router.get("/", response_model=List[schemas.BeatResponse])
def list_beats(db: Session = Depends(get_db)):
    return db.query(models.Beat).all()

