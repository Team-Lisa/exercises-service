from api.models.exercise import Exercise

class ExercisesValidator:

    @staticmethod
    def is_valid(exercise: Exercise):
        errors = []
        ExercisesValidator.validate_type(exercise, errors)
        ExercisesValidator.validate_options(exercise, errors)
        ExercisesValidator.validate_correct_answer(exercise, errors)
        if len(errors) == 0:
            return (True, [])
        return (False,errors)

    @staticmethod
    def validate_type(exercise, errors):
        if not exercise.exercise_type in ["Listening", "TranslateToOriginal", "TranslateToNew", "Complete"]:
            errors.append("Tipo de ejercicio incorrecto")

    @staticmethod
    def validate_options(exercise, errors):
        if exercise.exercise_type in ["Listening", "TranslateToOriginal", "TranslateToNew"]:
            if len(exercise.options) != 6:
                errors.append("Se requieren 6 respuestas para este ejercicio")
        if exercise.exercise_type == "Complete":
            if len(exercise.options) != 4:
                errors.append("Se requieren 4 respuestas para este ejercicio")

    @staticmethod
    def validate_correct_answer(exercise, errors):
        if exercise.correct_answer not in exercise.options:
            errors.append("La respuesta correcta no se encuentra entre las opciones")


