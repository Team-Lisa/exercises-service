from fastapi import APIRouter
from api.models.requests.challenge import Challenge, Unit, Lesson
from api.controllers.challenge_controller import ChallengeController
from api.models.responses.challenge import Challenge as ChallengeResponse
from api.models.responses.challenges import Challenges as ChallengesResponse

router = APIRouter(tags=["Challenge"])


@router.post("/challenges", response_model=ChallengeResponse)
async def create_exercise(challenge: Challenge):
    return ChallengeController.create(challenge)


@router.get("/challenges", response_model=ChallengesResponse)
async def find():
    return ChallengeController.find()


@router.post("/challenges/{challenge_id}/units")
async def add_unit(challenge_id: str, unit: Unit):
    return ChallengeController.add_unit(challenge_id, unit)


@router.post("/challenges/{challenge_id}/units/{unit_id}")
async def add_unit(challenge_id: str, unit_id: str, lesson: Lesson):
    return ChallengeController.add_lesson(challenge_id, unit_id, lesson)


