from api.models.challenge import Challenge
from api.models.requests.challenge import Unit, Exam, Lesson
from api.repositories.challenge_repository import ChallengeRepository
from api.services.challenges_validator import ChallengesValidator


def test_valid_challenge(init):
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
    ).dict()

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
    ).dict()

    challenge_mock = Challenge(
        name="mock_name",
        units=[
            unit_1,
            unit_2
        ],
        id="D1",
        published=False
    )
    is_valid, errors = ChallengesValidator.is_valid(challenge_mock)
    assert True == is_valid

def test_invalid_challenge(init):
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
    ).dict()

    exam_2 = Exam(
        id="2",
        duration=3600
    )

    unit_2 = Unit(
        name="mock_unit_1",
        exam=exam_2,
        id="U2",
        lessons=[
            lesson_3,
            lesson_4
        ]
    ).dict()

    challenge_mock = Challenge(
        name="mock_name",
        units=[
            unit_1,
            unit_2
        ],
        id="D1",
        published=False
    )
    is_valid, errors = ChallengesValidator.is_valid(challenge_mock)
    assert False == is_valid
