import pytest

from api.repositories.challenge_repository import ChallengeRepository
from api.repositories.exercise_repository import ExerciseRepository
from api.repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    ExerciseRepository.delete_all()
    ChallengeRepository.delete_all()
    return 0
