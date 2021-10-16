from typing import List

from pydantic.main import BaseModel
from api.models.responses.challenge import ChallengeResponse


class Challenges(BaseModel):
    challenges: List[ChallengeResponse]
