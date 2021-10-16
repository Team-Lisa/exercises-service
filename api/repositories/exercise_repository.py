from api.models.exercise import Exercise


class ExerciseRepository:

    @staticmethod
    def add(exercise):
        return exercise.save()

    @staticmethod
    def delete_all():
        Exercise.objects().delete()

    @staticmethod
    def get_all():
        return Exercise.objects()

    @staticmethod
    def get(lesson_id):
        if not lesson_id:
            return ExerciseRepository.get_all()
        return Exercise.objects(lesson_id=lesson_id)

    @staticmethod
    def get_new_id():
        last_id = "0"
        exercises = ExerciseRepository.get_all()
        if len(exercises) == 0:
            return last_id

        for exercise in exercises:
            if int(last_id) < int(exercise.exercise_id):
                last_id = exercise.exercise_id
        return str(int(last_id)+1)

    @staticmethod
    def delete(exercise_id):
        Exercise.objects(exercise_id=exercise_id).delete()
