from api.models.exercise import Exercise
from api.repositories.exercise_repository import ExerciseRepository
from api.services.exercises_validator import ExercisesValidator


def test_valid_exercise(init):
    exercise_type = "Listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "opcion_d", "opcion_e", "opcion_f"]
    correct_answer = "option_b"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)
    is_valid, errors = ExercisesValidator.is_valid(exercise)
    assert True == is_valid

def test_invalid_exercise(init):
    exercise_type = "Listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c", "opcion_d", "opcion_e"]
    correct_answer = "option_h"
    lesson_id = "C1U1L1"
    exercise_id = ExerciseRepository.get_next_id(lesson_id)
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, exercise_id=exercise_id, lesson_id=lesson_id)
    is_valid, errors = ExercisesValidator.is_valid(exercise)
    assert False == is_valid
    assert len(errors) == 2
    assert "Se requieren 6 respuestas para este ejercicio" in errors
    assert "La respuesta correcta no se encuentra entre las opciones" in errors
