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
    def edit_exercise(exercise_id, new_exercise):
        try:
            exercise = Exercise.objects(exercise_id=exercise_id).get()
            exercise.lesson_id = new_exercise.lesson_id
            exercise.exercise_type = new_exercise.exercise_type
            exercise.question = new_exercise.question
            exercise.options = new_exercise.options
            exercise.correct_answer = new_exercise.correct_answer
            exercise.save()
            return exercise
        except Exception:
            return

    @staticmethod
    def delete(exercise_id):
        Exercise.objects(exercise_id=exercise_id).delete()

    @staticmethod
    def get_next_id(lesson_id):
        exercises = Exercise.objects.filter(lesson_id=lesson_id).order_by('-exercise_id')
        if len(exercises) == 0:
            return lesson_id + "E" + str(1)
        else:
            next_id = int(exercises[0].exercise_id.split('E')[1]) + 1
            return lesson_id + "E" + str(next_id)
