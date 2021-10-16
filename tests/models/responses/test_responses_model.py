from api.models.challenge import Challenge
from api.models.responses.exercises import Exercises as ExercisesResponse
from api.models.responses.exercise import Exercise as ExerciseResponse
from api.models.exercise import Exercise as ExerciseModel
from api.models.responses.challenge import Challenge as ChallengeResponse
from api.models.responses.challenges import Challenges as ChallengesResponse


def test_exercises_response():
    exercise_type = "listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "e1"
    lesson_id = "l1"
    exercise = ExerciseModel(exercise_type=exercise_type, question=question,
                             options=options, correct_answer=correct_answer,
                             exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExercisesResponse(
        exercises=[exercise.to_json()]
    )

    assert len(response.exercises) == 1


def test_exercise_response():
    exercise_type = "listening"
    question = "mock_question"
    options = ["option_a", "option_b", "option_c"]
    correct_answer = "option_b"
    exercise_id = "e1"
    lesson_id = "l1"
    exercise = ExerciseModel(exercise_type=exercise_type, question=question,
                             options=options, correct_answer=correct_answer,
                             exercise_id=exercise_id, lesson_id=lesson_id)

    response = ExerciseResponse(
        exercise=exercise.to_json()
    )

    assert response.exercise.dict() == exercise.to_json()


def test_challenge_response():
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = {
        "id": "1",
        "duration": 3600
    }
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]

    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1,
         "id": "1"}
    ]
    challenge_id = "D1"
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id)

    response = ChallengeResponse(
        challenge=challenge.to_json()
    )

    assert response.challenge.dict() == challenge.to_json()


def test_challenges_response():
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = {
        "id": "1",
        "duration": 3600
    }
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]

    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1,
         "id": "1"}
    ]
    challenge_id = "D1"
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id)

    response = ChallengesResponse(
        challenges=[challenge.to_json()]
    )

    assert len(response.challenges) == 1
