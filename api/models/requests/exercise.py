from pydantic.main import BaseModel


class Exercise(BaseModel):
    lesson_id: str
    exercise_type: str
    question: str
    options: list
    correct_answer: str
