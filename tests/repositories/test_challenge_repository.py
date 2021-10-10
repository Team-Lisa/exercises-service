from api.models.challenge import Challenge
from api.repositories.challenge_repository import ChallengeRepository


def test_model_with_valid_units(init):
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = "exam_1"
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]
    name_lesson_2 = "mock_name_lesson_2"
    exam_2 = "exam_1"
    lessons_2 = [
        {"name": "lesson_1",
         "id": "C1U2L1"},
        {"name": "lesson_2",
         "id": "C1U2L2"}
    ]
    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1},
        {"name": name_lesson_2,
         "exam": exam_2,
         "lessons": lessons_2}
    ]
    challenge = Challenge(name=name, units=units)
    challenge_saved = ChallengeRepository.add(challenge)

    assert challenge_saved.name == name
    assert challenge_saved.units == units


def test_add_unit(init):
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = "exam_1"
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]

    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1},

    ]
    challenge_id = "D1"
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id)

    ChallengeRepository.add(challenge)

    result = ChallengeRepository.get_all()
    assert result.count() == 1

    challenge_saved = result.get()

    assert len(challenge_saved.units) == 1

    name_lesson_2 = "mock_name_lesson_2"
    exam_2 = "exam_1"
    lessons_2 = [
        {"name": "lesson_1",
         "id": "C1U2L1"},
        {"name": "lesson_2",
         "id": "C1U2L2"}
    ]
    new_unit = {"name": name_lesson_2,
                "exam": exam_2,
                "lessons": lessons_2}

    ChallengeRepository.add_unit(challenge_id, new_unit)

    result = ChallengeRepository.get_all()
    assert result.count() == 1

    challenge_saved = result.get()

    assert len(challenge_saved.units) == 2


def test_add_lesson(init):
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = "exam_1"
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"}
    ]
    unit_id = "U1"
    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "id": unit_id,
         "lessons": lessons_1},

    ]
    challenge_id = "D1"
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id)

    ChallengeRepository.add(challenge)

    result = ChallengeRepository.get_all()
    assert result.count() == 1

    challenge_saved = result.get()

    assert len(challenge_saved.units) == 1

    lessons = challenge_saved.units[0].get("lessons")

    assert len(lessons) == 1

    lessons_2 = {"name": "lesson_2",
                 "id": "C1U2L2"}

    ChallengeRepository.add_lesson(challenge_id, unit_id, lessons_2)

    result = ChallengeRepository.get_all()
    assert result.count() == 1

    challenge_saved = result.get()

    assert len(challenge_saved.units) == 1

    lessons = challenge_saved.units[0].get("lessons")

    assert len(lessons) == 2


def test_delete_challenge(init):
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = "exam_1"
    lessons_1 = [
        {"name": "lesson_1",
         "id": "C1U1L1"},
        {"name": "lesson_2",
         "id": "C1U1L2"}
    ]

    units = [
        {"name": name_lesson_1,
         "exam": exam_1,
         "lessons": lessons_1},

    ]
    challenge_id = "D1"
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id)

    ChallengeRepository.add(challenge)

    result = ChallengeRepository.get_all()
    assert result.count() == 1

    ChallengeRepository.delete(challenge_id)

    result = ChallengeRepository.get_all()
    assert result.count() == 0
