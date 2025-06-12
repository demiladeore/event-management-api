# routes/speaker.py

from fastapi import APIRouter, HTTPException
from typing import List
from schemas import speaker as speaker_schema
from services import speaker_service

router = APIRouter()

@router.get("/", response_model=List[speaker_schema.Speaker])
def get_speakers():
    return speaker_service.get_all_speakers()

@router.get("/{speaker_id}", response_model=speaker_schema.Speaker)
def get_speaker(speaker_id: int):
    speaker = speaker_service.get_speaker(speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker
