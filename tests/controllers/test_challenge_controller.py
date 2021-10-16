from api.controllers.challenge_controller import ChallengeController
from api.models.requests.challenge import Challenge, Unit, Lesson, Exam
from api.repositories.challenge_repository import ChallengeRepository
from api.models.challenge import Challenge as ChallengeModel


def test_response_create(init):
    lesson_1 = Lesson(
        name="lesson_1",
        id="C1U1L1"
    )
    lesson_2 = Lesson(
        name="lesson_2",
        id="C1U1L2"
    )

    lesson_3 = Lesson(
        name="lesson_1",
        id="C1U2L1"
    )
    lesson_4 = Lesson(
        name="lesson_2",
        id="C1U2L2"
    )

    exam_1 = Exam(
        id="1",
        duration=3600
    )

    unit_1 = Unit(
        name="mock_unit_1",
        exam=exam_1,
        id="U1",
        lessons=[
            lesson_1,
            lesson_2
        ]
    )

    exam_2 = Exam(
        id="2",
        duration=3600
    )

    unit_2 = Unit(
        name="mock_unit_2",
        exam=exam_2,
        id="U2",
        lessons=[
            lesson_3,
            lesson_4
        ]
    )

    challenge_mock = Challenge(
        name="mock_name",
        units=[
            unit_1,
            unit_2
        ],
        id="D1"
    )

    result = ChallengeController.create(challenge_mock)

    assert "challenge" in result
    assert result.get("challenge") == {
        'name': 'mock_name',
        'challenge_id': 'D1',
        'units': [
            {'name': 'mock_unit_1',
             'id': 'U1',
             'exam': {
                 "id": "1",
                 "duration": 3600
             },
             'lessons': [
                 {'name': 'lesson_1',
                  'id': 'C1U1L1'},
                 {'name': 'lesson_2',
                  'id': 'C1U1L2'}
             ]},
            {'name': 'mock_unit_2',
             'id': 'U2',
             'exam': {
                 "id": "2",
                 "duration": 3600
             },
             'lessons': [
                 {'name': 'lesson_1',
                  'id': 'C1U2L1'},
                 {'name': 'lesson_2',
                  'id': 'C1U2L2'}
             ]
             }
        ]
    }


def test_add_unit(init):
    name = "mock_name"
    name_lesson_1 = "mock_name_lesson_1"
    exam_1 = {
                 "id": "2",
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
         "id": "U1",
         "exam": exam_1,
         "lessons": lessons_1},

    ]

    challenge_id = "D1"
    challenge = ChallengeModel(name=name, units=units, challenge_id=challenge_id)

    ChallengeRepository.add(challenge)

    lesson_3 = Lesson(
        name="lesson_1",
        id="C1U2L1"
    )
    lesson_4 = Lesson(
        name="lesson_2",
        id="C1U2L2"
    )

    exam = Exam(
        id="2",
        duration=3600
    )

    unit = Unit(
        name="mock_unit_2",
        id="U2",
        exam=exam,
        lessons=[
            lesson_3,
            lesson_4
        ]
    )

    result = ChallengeController.add_unit(challenge_id, unit)
    assert "message" in result
    assert result.get("message") == "unit created"


def test_delete_unit(init):
    lesson_1 = Lesson(
        name="lesson_1",
        id="C1U1L1"
    )
    lesson_2 = Lesson(
        name="lesson_2",
        id="C1U1L2"
    )

    lesson_3 = Lesson(
        name="lesson_1",
        id="C1U2L1"
    )
    lesson_4 = Lesson(
        name="lesson_2",
        id="C1U2L2"
    )

    exam_1 = Exam(
        id="1",
        duration=3600
    )

    exam_2 = Exam(
        id="2",
        duration=3600
    )

    unit_1 = Unit(
        name="mock_unit_1",
        exam=exam_1,
        id="U1",
        lessons=[
            lesson_1,
            lesson_2
        ]
    )

    unit_2 = Unit(
        name="mock_unit_2",
        exam=exam_2,
        id="U2",
        lessons=[
            lesson_3,
            lesson_4
        ]
    )

    challenge_mock = Challenge(
        name="mock_name",
        units=[
            unit_1,
            unit_2
        ],
        id="D1"
    )

    ChallengeController.create(challenge_mock)

    challenge_query = ChallengeRepository.get_by_id("D1")

    assert len(challenge_query.get().units) == 2

    result = ChallengeController.delete_unit("D1", "U1")

    assert result == {"message": "unit deleted"}

    challenge_query = ChallengeRepository.get_by_id("D1")

    assert len(challenge_query.get().units) == 1


def test_delete_lesson(init):
    lesson_1 = Lesson(
        name="lesson_1",
        id="C1U1L1"
    )
    lesson_2 = Lesson(
        name="lesson_2",
        id="C1U1L2"
    )

    exam = Exam(
        id="1",
        duration=3600
    )

    unit_1 = Unit(
        name="mock_unit_1",
        exam=exam,
        id="U1",
        lessons=[
            lesson_1,
            lesson_2
        ]
    )

    challenge_mock = Challenge(
        name="mock_name",
        units=[
            unit_1
        ],
        id="D1"
    )

    ChallengeController.create(challenge_mock)

    challenge_query = ChallengeRepository.get_by_id("D1")
    challenge = challenge_query.get()
    units = challenge.units
    unit = units[0]

    assert len(unit.get("lessons")) == 2

    result = ChallengeController.delete_lesson("D1", "U1", "C1U1L1")

    assert result == {"message": "lesson deleted"}

    challenge_query = ChallengeRepository.get_by_id("D1")
    challenge = challenge_query.get()
    units = challenge.units
    unit = units[0]

    assert len(unit.get("lessons")) == 1
