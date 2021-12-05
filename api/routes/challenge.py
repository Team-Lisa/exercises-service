from typing import Optional

from fastapi import APIRouter
from api.models.requests.challenge import Challenge, Unit, Lesson
from api.controllers.challenge_controller import ChallengeController
from api.models.responses.challenge import Challenge as ChallengeResponse
from api.models.responses.challenges import Challenges as ChallengesResponse

router = APIRouter(tags=["Challenge"])


@router.post("/challenges", response_model=ChallengeResponse, status_code=201)
async def create(challenge: Challenge):
    return ChallengeController.create(challenge)

@router.post("/challenges/{challenge_id}", status_code=201)
async def edit_challenge(challenge_id: str, challenge: Challenge):
    return ChallengeController.edit_challenge(challenge_id, challenge)


@router.get("/challenges", response_model=ChallengesResponse)
async def find(published: str = None):
    return ChallengeController.find(published)

@router.get("/challenges/next")
async def get_next_challenge_id():
    return ChallengeController.get_next_challenge_id()

@router.post("/challenges/{challenge_id}/units", status_code=201)
async def add_unit(challenge_id: str, unit: Unit):
    return ChallengeController.add_unit(challenge_id, unit)


@router.post("/challenges/{challenge_id}/units/{unit_id}", status_code=201)
async def add_lesson(challenge_id: str, unit_id: str, lesson: Lesson):
    return ChallengeController.add_lesson(challenge_id, unit_id, lesson)


@router.delete("/challenges/{challenge_id}")
async def delete(challenge_id: Optional[str] = None):
    return ChallengeController.delete_challenge(challenge_id)


@router.delete("/challenges/{challenge_id}/units/{unit_id}")
async def delete_unit(challenge_id: str, unit_id: str):
    return ChallengeController.delete_unit(challenge_id, unit_id)


@router.delete("/challenges/{challenge_id}/units/{unit_id}/lessons/{lesson_id}")
async def delete_lesson(challenge_id: str, unit_id: str, lesson_id: str):
    return ChallengeController.delete_lesson(challenge_id, unit_id, lesson_id)

@router.get("/challenges/{challenge_id}", response_model=ChallengeResponse)
async def get_challenge_by_challenge_id(challenge_id: str):
    return ChallengeController.get_challenge_by_challenge_id(challenge_id)