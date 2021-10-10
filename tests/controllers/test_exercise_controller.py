from api.controllers.exercise_controller import ExerciseController
from api.models.requests.exercise import Exercise


def test_response_create(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "e1"
    lesson_id = "l1"
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExerciseController.create(exercise)
    assert response == {
        "exercise": {
            "exercise_type": exercise_type,
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
            "exercise_id": exercise_id,
            "lesson_id": lesson_id
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
    exercise_id = "e1"
    lesson_id = "l1"
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    ExerciseController.create(exercise)

    result = ExerciseController.find()
    assert result == {
        "exercises": [
            {
                "exercise_type": exercise_type,
                "question": question,
                "options": options,
                "correct_answer": correct_answer,
                "exercise_id": exercise_id,
                "lesson_id": lesson_id
            }
        ]
    }
    exercises = result["exercises"]
    assert len(exercises) == 1
