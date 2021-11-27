from api.controllers.exercise_controller import ExerciseController
from api.models.requests.exercise import Exercise
from api.repositories.exercise_repository import ExerciseRepository


def test_response_create(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
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
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
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


def test_delete(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c","option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    ExerciseController.create(exercise)

    result = ExerciseController.find()
    exercises = result["exercises"]
    assert len(exercises) == 1

    result = ExerciseController.delete(exercise_id)
    assert result.get("message") == "exercise deleted"

    result = ExerciseController.find()
    exercises = result["exercises"]
    assert len(exercises) == 0


def test_find_lesson(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    for i in range(ExerciseController.LESSON_EXERCISES_AMOUNT + 3):
        ExerciseController.create(exercise)

    result = ExerciseController.find_lesson(lesson_id)

    exercises = result.get("exercises")

    assert len(exercises) == ExerciseController.LESSON_EXERCISES_AMOUNT


def test_find_exam(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    for i in range(ExerciseController.EXAM_EXERCISES_AMOUNT + 3):
        ExerciseController.create(exercise)

    result = ExerciseController.find_exam(lesson_id)

    exercises = result.get("exercises")

    assert len(exercises) == ExerciseController.EXAM_EXERCISES_AMOUNT

def test_edit_exercise(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    exercise_id = ExerciseRepository.get_next_id("C1U1L1")
    lesson_id = "C1U1L1"
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

    new_exercise = Exercise(exercise_type=exercise_type, question="question edit", options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExerciseController.edit_exercise(exercise_id, new_exercise)
    assert response == {
        "exercise": {
            "exercise_type": exercise_type,
            "question": "question edit",
            "options": options,
            "correct_answer": correct_answer,
            "exercise_id": exercise_id,
            "lesson_id": lesson_id
        }
    }

def test_edit_exercise_without_id(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    exercise_id = ExerciseRepository.get_next_id("C1U1L1")
    lesson_id = "C1U1L1"
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

    new_exercise = Exercise(exercise_type=exercise_type, question="question edit", options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExerciseController.edit_exercise(None, new_exercise)
    assert response == {
        "exercise": {}
    }

def test_get_next_exercise_id(init):
    exercise_type = "Complete"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "option_d"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = "C1U1L1E1"
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)
    ExerciseController.create(exercise)
    result = ExerciseController.get_next_exercise_id(lesson_id)
    assert result == {"exercise_next_id": "C1U1L1E2"}
