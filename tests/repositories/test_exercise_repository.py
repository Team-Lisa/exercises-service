from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise


def test_add_user_successfully(init):
    exercise_type = "listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "C1U1L1E1"
    lesson_id = "C1U1L1"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=exercise_id, lesson_id=lesson_id)
    result = ExerciseRepository.add(exercise)

    assert result.exercise_type == exercise_type
    assert result.question == question
    assert result.options == options
    assert result.correct_answer == correct_answer
    assert result.exercise_id == exercise_id
    assert result.lesson_id == lesson_id


def test_delete_all(init):
    ExerciseRepository.delete_all()
    result = ExerciseRepository.get_all()
    assert result.count() == 0


def test_find_by_lesson_id(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "C1U1L1E1"
    lesson_id = "C1U1L1"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=exercise_id, lesson_id=lesson_id)
    ExerciseRepository.add(exercise)

    exercise_type = "listing"
    question = "mock_question_1"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_c"
    exercise_id = "C1U1L1E2"
    lesson_id = "C1U1L1"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=exercise_id, lesson_id=lesson_id)
    ExerciseRepository.add(exercise)

    exercise_type = "listing"
    question = "mock_question_1"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_c"
    exercise_id = "C1U1L2E2"
    lesson_id_2 = "C1U1L2"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=exercise_id, lesson_id=lesson_id_2)
    ExerciseRepository.add(exercise)

    result = ExerciseRepository.get_all()

    assert result.count() == 3

    result = ExerciseRepository.get(lesson_id)

    assert result.count() == 2


def test_new_id(init):
    assert ExerciseRepository.get_next_id("C1U1L1") == "C1U1L1E1"

def test_get_next_exercise_id(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=ExerciseRepository.get_next_id(lesson_id), lesson_id=lesson_id)
    ExerciseRepository.add(exercise)

    assert ExerciseRepository.get_next_id(lesson_id) == "C1U1L1E2"

def test_edit_exercise(init):
    exercise_type = "listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "C1U1L1E1"
    lesson_id = "C1U1L1"
    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer,
                        exercise_id=exercise_id, lesson_id=lesson_id)
    ExerciseRepository.add(exercise)

    new_exercise = Exercise(exercise_type="pruebita", question="question edit", options=options,
                            correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExerciseRepository.edit_exercise(exercise_id, new_exercise)
    assert response.exercise_type == "pruebita"
    assert response.question == "question edit"
    assert response.options == options
    assert response.correct_answer == correct_answer
    assert response.exercise_id == exercise_id
    assert response.lesson_id == lesson_id