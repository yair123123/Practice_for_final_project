from dataclasses import dataclass
from datetime import datetime


@dataclass
class Review:
    review_id: str
    content: str
    score: float
    date_time: str
    thumbs_up_count: int
    review_created_version: str
    app_version: str
    student_id: int

