from typing import List

from pydantic.main import BaseModel


class Lesson(BaseModel):
    name: str
    id: str


class Unit(BaseModel):
    name: str
    exam: str
    lessons: List[Lesson]
    id: str


class Challenge(BaseModel):
    name: str
    units: List[Unit]
    id: str
