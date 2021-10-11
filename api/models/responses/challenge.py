from pydantic.main import BaseModel


class Challenge(BaseModel):
    challenge: dict
