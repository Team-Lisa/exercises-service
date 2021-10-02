from fastapi import APIRouter
from api.models.requests.exercise import Exercise
from api.controllers.exercise_controller import ExerciseController
from api.models.responses.exercise import Exercise as ExerciseResponse
from api.models.responses.exercises import Exercises as ExercisesResponse

router = APIRouter(tags=["Exercises"])


@router.post("/exercises", response_model=ExerciseResponse)
async def create_exercise(exercise: Exercise):
    return ExerciseController.create(exercise)


@router.get("/exercises", response_model=ExercisesResponse)
async def find():
    return ExerciseController.find()


