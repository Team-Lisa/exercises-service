from api.models.requests.challenge import Lesson, Unit, Exam
from api.models.requests.exercise import Exercise

class TestModels:

    @staticmethod
    def get_valid_challenge():
        lesson_1 = Lesson(
            name="lesson_1",
            id="C1U1L1"
        )

        exam = Exam(
            id="C1U1X",
            duration=3600
        )

        unit_1 = Unit(
            name="mock_unit_1",
            exam=exam,
            id="C1U1",
            lessons=[
                lesson_1
            ]
        )

        challenge_mock = Challenge(
            name="mock_name",
            units=[
                unit_1
            ],
            id="C1",
            published=True
        )

        return challenge_mock

    @staticmethod
    def get_eight_exercises(lesson_id):
        exercise_1 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_1",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E1"
        )

        exercise_2 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_2",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E2"
        )

        exercise_3 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_3",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E3"
        )

        exercise_4 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_4",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E4"
        )

        exercise_5 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_5",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E5"
        )

        exercise_6 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_6",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E6"
        )

        exercise_7 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_7",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E7"
        )

        exercise_8 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_8",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id+"E8"
        )

        return [exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6, exercise_7, exercise_8]

    @staticmethod
    def get_sixteen_exercises(lesson_id):
        exercise_1 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_1",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E1"
        )

        exercise_2 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_2",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E2"
        )

        exercise_3 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_3",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E3"
        )

        exercise_4 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_4",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E4"
        )

        exercise_5 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_5",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E5"
        )

        exercise_6 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_6",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E6"
        )

        exercise_7 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_7",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E7"
        )

        exercise_8 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_8",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E8"
        )
        exercise_9 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_9",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E9"
        )

        exercise_10 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_10",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E10"
        )

        exercise_11 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_11",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E11"
        )

        exercise_12 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_12",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E12"
        )

        exercise_13 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_13",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E13"
        )

        exercise_14 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_14",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E14"
        )

        exercise_15 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_15",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E15"
        )

        exercise_16 = Exercise(
            lesson_id=lesson_id,
            exercise_type="Complete",
            question="question_16",
            options=[
                "a",
                "b",
                "c",
                "d"
            ],
            correct_answer="a",
            exercise_id=lesson_id + "E16"
        )

        return [exercise_1, exercise_2, exercise_3, exercise_4, exercise_5, exercise_6, exercise_7, exercise_8,exercise_9, exercise_10, exercise_11, exercise_12, exercise_13, exercise_14, exercise_15, exercise_16]