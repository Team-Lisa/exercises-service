from api.repositories.exercise_repository import ExerciseRepository
from api.models.exercise import Exercise


class ExerciseController:
    EXAM_EXERCISES_AMOUNT = 16
    LESSON_EXERCISES_AMOUNT = 8

    @staticmethod
    def create(exercise):
        exercise_to_save = Exercise(exercise_type=exercise.exercise_type, question=exercise.question,
                                    options=exercise.options, correct_answer=exercise.correct_answer,
                                    lesson_id=exercise.lesson_id, exercise_id=ExerciseRepository.get_next_id(exercise.lesson_id))
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
    def find_exercises(lesson_id, amount_exercises):
        result = ExerciseController.find(lesson_id)
        exercises = result.get("exercises")
        if len(exercises) < amount_exercises:
            return {"exercises": exercises}
        return {"exercises": exercises[:amount_exercises]}

    @staticmethod
    def edit_exercise(exercise_id, exercise):
        exercise_updated = ExerciseRepository.edit_exercise(exercise_id, exercise)
        if exercise_updated == None:
            return {"exercise": {}}
        return {"exercise": exercise_updated.to_json()}


    @staticmethod
    def delete(exercise_id=None):
        if not exercise_id:
            ExerciseRepository.delete_all()
        else:
            ExerciseRepository.delete(exercise_id)
        return {"message": "exercise deleted"}

    @staticmethod
    def get_next_exercise_id(lesson_id):
        # Ids:
        #   - "C1" is for Challenge 1
        #   - "C1U1" is for Challenge 1, Unit 1
        #   - "C1U1L1" is for Challenge 1, Unit1, Lesson 1
        #   - "C1U1L1E1" is for Challenge 1, Unit 1, Lesson 1, Exercise 1
        #   - "C1U1E" is for Challenge 1, Unit 1, Exam
        #   - "C1U1EE1" is for Challenge 1, Unit 1, Exam, Exercise 1
        result = ExerciseRepository.get_next_id(lesson_id)
        return {"exercise_next_id": result}
