import pytest
from api.Repositories.exercise_repository import ExerciseRepository
from api.Repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    ExerciseRepository.delete_all()
    return 0
