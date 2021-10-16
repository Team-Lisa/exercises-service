from typing import List

from pydantic.main import BaseModel

from api.models.requests.challenge import Unit


class ChallengeResponse(BaseModel):
    name: str
    units: List[Unit]
    challenge_id: str


class Challenge(BaseModel):
    challenge: ChallengeResponse
