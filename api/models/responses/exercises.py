from typing import List

from pydantic.main import BaseModel
from api.models.responses.exercise import ExerciseResponse


class Exercises(BaseModel):
    exercises: List[ExerciseResponse]
