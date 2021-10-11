from api.models.exercise import Exercise


def test_model_to_json():
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    lesson_id = "l1"
    exercise_id = "e1"
    exercise = Exercise(exercise_type=exercise_type, question=question, options=options,
                        correct_answer=correct_answer, lesson_id=lesson_id, exercise_id=exercise_id)
    assert exercise.to_json() == {
        "exercise_type": exercise_type,
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "lesson_id": lesson_id,
        "exercise_id": exercise_id,
    }
