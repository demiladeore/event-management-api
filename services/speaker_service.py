# services/speaker_service.py

from schemas import speaker as speaker_schema
from typing import List, Optional

# Initialize with 3 predefined speakers
_speakers: List[speaker_schema.Speaker] = [
    speaker_schema.Speaker(id=1, name="Alice Johnson", topic="Data Science in 2025"),
    speaker_schema.Speaker(id=2, name="Bob Smith", topic="AI and Ethics"),
    speaker_schema.Speaker(id=3, name="Clara Lee", topic="Scaling Microservices with FastAPI")
]

def get_all_speakers() -> List[speaker_schema.Speaker]:
    return _speakers

def get_speaker(speaker_id: int) -> Optional[speaker_schema.Speaker]:
    return next((speaker for speaker in _speakers if speaker.id == speaker_id), None)
