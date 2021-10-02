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
