from api.controllers.challenge_controller import ChallengeController
from api.models.requests.challenge import Challenge, Unit, Lesson
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

    unit_1 = Unit(
        name="mock_unit_1",
        exam="exam",
        id="U1",
        lessons=[
            lesson_1,
            lesson_2
        ]
    )

    unit_2 = Unit(
        name="mock_unit_2",
        exam="exam",
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
             'exam': 'exam',
             'lessons': [
                 {'name': 'lesson_1',
                  'id': 'C1U1L1'},
                 {'name': 'lesson_2',
                  'id': 'C1U1L2'}
             ]},
            {'name': 'mock_unit_2',
             'id': 'U2',
             'exam': 'exam',
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
    exam_1 = "exam_1"
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
    unit = Unit(
        name="mock_unit_2",
        id="U2",
        exam="exam",
        lessons=[
            lesson_3,
            lesson_4
        ]
    )

    result = ChallengeController.add_unit(challenge_id, unit)
    assert "message" in result
    assert result.get("message") == "unit created"
