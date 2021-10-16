from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise


class ExerciseController:
    EXAM_EXERCISES_AMOUNT = 16
    LESSON_EXERCISES_AMOUNT = 8

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
    def find_exam(exam_id):
        return ExerciseController.find_exercises(exam_id, ExerciseController.EXAM_EXERCISES_AMOUNT)

    @staticmethod
    def find_lesson(lesson_id):
        return ExerciseController.find_exercises(lesson_id, ExerciseController.LESSON_EXERCISES_AMOUNT)

    @staticmethod
    def find_exercises(exercise_id, amount_exercises):
        result = ExerciseController.find(exercise_id)
        exercises = result.get("exercises")
        if len(exercises) < amount_exercises:
            return {"exercises": exercises}
        return {"exercises": exercises[:amount_exercises]}

    @staticmethod
    def delete(exercise_id=None):
        if not exercise_id:
            ExerciseRepository.delete_all()
        else:
            ExerciseRepository.delete(exercise_id)
        return {"message": "exercise deleted"}
