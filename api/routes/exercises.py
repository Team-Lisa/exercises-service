from fastapi import APIRouter
from api.models.requests.exercise import Exercise
from api.controllers.exercise_controller import ExerciseController
from api.models.responses.exercise import Exercise as UserResponse

router = APIRouter(tags=["Users"])


@router.post("/exercises", response_model=UserResponse)
async def create_exercise(exercise: Exercise):
    return ExerciseController.create(exercise)


@router.get("/exercises")
async def find():
    return ExerciseController.find()


