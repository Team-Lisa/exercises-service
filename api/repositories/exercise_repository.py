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
    def delete(exercise_id):
        Exercise.objects(exercise_id=exercise_id).delete()

    @staticmethod
    def get_next_id(lesson_id):
        exercises = Exercise.objects.filter(lesson_id=lesson_id).values_list('exercise_id')
        return lesson_id + "E" + str(len(exercises) + 1)
