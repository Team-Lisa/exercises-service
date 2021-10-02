import pytest
from api.repositories.exercise_repository import ExerciseRepository
from api.repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    ExerciseRepository.delete_all()
    return 0
