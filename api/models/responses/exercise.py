from pydantic.main import BaseModel


class Exercise(BaseModel):
    exercise: dict
