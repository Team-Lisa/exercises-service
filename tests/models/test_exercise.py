from api.models.exercise import Exercise


def test_model_to_json():
    exercise_type = "listing"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"

    exercise = Exercise(exercise_type=exercise_type, question=question, options=options, correct_answer=correct_answer)
    assert exercise.to_json() == {
        "exercise_type": exercise_type,
        "question": question,
        "options": options,
        "correct_answer": correct_answer
    }
