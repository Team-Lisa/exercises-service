from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise


class ExerciseController:

    @staticmethod
    def create(exercise):
        exercise_to_save = Exercise(exercise_type=exercise.exercise_type, question=exercise.question,
                                    options=exercise.options, correct_answer=exercise.correct_answer,
                                    lesson_id=exercise.lesson_id, exercise_id=ExerciseRepository.get_new_id())
        result = ExerciseRepository.add(exercise_to_save)
        return {"exercise": result.to_json()}

    @staticmethod
    def find(lesson_id=None):
        result = ExerciseRepository.get(lesson_id)
        result = map(lambda exercise: exercise.to_json(), list(result))
        return {"exercises": list(result)}

    @staticmethod
    def delete(exercise_id=None):
        if not exercise_id:
            ExerciseRepository.delete_all()
        else:
            ExerciseRepository.delete(exercise_id)
        return {"message": "exercise deleted"}
