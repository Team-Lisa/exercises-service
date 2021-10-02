from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise
from fastapi import HTTPException


class ExerciseController:

    @staticmethod
    def create(exercise):
        exercise_to_save = Exercise(exercise_type=exercise.exercise_type, question=exercise.question,
                                    options=exercise.options, correct_answer=exercise.correct_answer)
        result = ExerciseRepository.add(exercise_to_save)
        return {"exercise": result.to_json()}

    @staticmethod
    def find():
        result = ExerciseRepository.get_all()
        result = map(lambda exercise: exercise.to_json(), list(result))
        return {"exercises": list(result)}
