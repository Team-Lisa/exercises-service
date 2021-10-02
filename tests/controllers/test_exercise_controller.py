import pytest

from api.controllers.exercise_controller import ExerciseController
from api.models.requests.exercise import Exercise
from fastapi import HTTPException


def test_response_create(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"

    exercise = Exercise(exercise_type=exercise_type, question=question, options=options, correct_answer=correct_answer)

    response = ExerciseController.create(exercise)
    assert response == {
        "exercise": {
            "exercise_type": exercise_type,
            "question": question,
            "options": options,
            "correct_answer": correct_answer
        }
    }


def test_find_empty(init):
    result = ExerciseController.find()
    exercises = result["exercises"]
    assert len(exercises) == 0


def test_find(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"

    exercise = Exercise(exercise_type=exercise_type, question=question, options=options, correct_answer=correct_answer)
    ExerciseController.create(exercise)

    result = ExerciseController.find()
    assert result == {
        "exercises": [
            {
                "exercise_type": exercise_type,
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            }
        ]
    }
    exercises = result["exercises"]
    assert len(exercises) == 1
