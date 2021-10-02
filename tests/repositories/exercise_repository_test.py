from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise


def test_add_user_successfully(init):
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"

    exercise = Exercise(exercise_type=exercise_type, question=question,
                        options=options, correct_answer=correct_answer)
    result = ExerciseRepository.add(exercise)

    assert result.exercise_type == exercise_type
    assert result.question == question
    assert result.options == options
    assert result.correct_answer == correct_answer


def test_delete_all_users(init):
    ExerciseRepository.delete_all()
    result = ExerciseRepository.get_all()
    assert result.count() == 0
