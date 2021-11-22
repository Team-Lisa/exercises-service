from typing import List

from pydantic.main import BaseModel

from api.models.requests.challenge import Unit


class ChallengeResponse(BaseModel):
    name: str
    units: List[Unit]
    challenge_id: str
    published: bool


class Challenge(BaseModel):
    challenge: ChallengeResponse
