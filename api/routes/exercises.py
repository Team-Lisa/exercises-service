from typing import Optional

from fastapi import APIRouter
from api.models.requests.exercise import Exercise
from api.controllers.exercise_controller import ExerciseController
from api.models.responses.exercise import Exercise as ExerciseResponse
from api.models.responses.exercises import Exercises as ExercisesResponse

router = APIRouter(tags=["Exercises"])


@router.post("/exercises", response_model=ExerciseResponse, status_code=201)
async def create(exercise: Exercise):
    return ExerciseController.create(exercise)


@router.get("/exercises", response_model=ExercisesResponse)
async def find(lesson_id: Optional[str] = None):
    return ExerciseController.find(lesson_id)

@router.get("/lessons/{lesson_id}/exercises", response_model=ExercisesResponse)
async def find(lesson_id:str):
    return ExerciseController.find_lesson(lesson_id)

@router.get("/exams/{exam_id}/exercises", response_model=ExercisesResponse)
async def find(exam_id: str):
    return ExerciseController.find_exam(exam_id)

@router.post("/exercises/{exercise_id}", status_code=201)
async def edit_exercise(exercise_id: str, exercise: Exercise):
    return ExerciseController.edit_exercise(exercise_id, exercise)

@router.delete("/exercises/{exercise_id}")
async def delete(exercise_id: Optional[str] = None):
    return ExerciseController.delete(exercise_id)