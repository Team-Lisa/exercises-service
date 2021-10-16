from typing import Dict

from pydantic.main import BaseModel
from api.models.requests.exercise import Exercise as ExerciseRequest


class ExerciseResponse(ExerciseRequest):
    exercise_id: str


class Exercise(BaseModel):
    exercise: ExerciseResponse
