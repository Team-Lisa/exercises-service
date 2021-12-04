from api.controllers.exercise_controller import ExerciseController
from api.models.challenge import Challenge
from api.repositories.challenge_repository import ChallengeRepository


class ChallengesValidator:

    @staticmethod
    def is_valid(challenge: Challenge):
        errors = []
        ChallengesValidator.validate_name(challenge, errors)
        ChallengesValidator.validate_units_in_challenge(challenge, errors)
        if challenge.published == True:
            ChallengesValidator.min_units_and_lessons(challenge, errors)
            ChallengesValidator.min_exercises_in_lesson(challenge, errors)
            ChallengesValidator.min_exercises_in_exam(challenge, errors)
        if len(errors) == 0:
            return (True, [])
        return (False,errors)

    @staticmethod
    def validate_name(challenge, errors):
        if len(ChallengeRepository.get_challenge_by_name(challenge.name)) > 1:
            errors.append("Nombre del desafío no disponible")

    @staticmethod
    def validate_units_in_challenge(challenge, errors):
        if challenge.units == []:
            return
        unique = []
        for unit in challenge.units:
            if unit["name"] not in unique:
                unique.append(unit["name"])
            else:
                errors.append("Nombre de la unidad ya utilizado en este desafio.")
                return errors

    @staticmethod
    def min_units_and_lessons(challenge, errors):
        if len(challenge.units) < 1:
            errors.append("Se requiere un minimo de una unidad para publicar un desafio.")
            return errors
        for unit in challenge.units:
            if len(unit["lessons"]) < 1:
                errors.append("Se requiere un minimo de una leccion en la unidad " + unit["name"])
        return errors

    @staticmethod
    def min_exercises_in_lesson(challenge, errors):
        for unit in challenge.units:
            for lesson in unit["lessons"]:
                result = ExerciseController.find(lesson["id"])
                exercises = result.get("exercises")
                if len(exercises) != 8:
                    errors.append("Se requiere un minimo de 8 ejercicios en la leccion " + lesson["name"] + " de la unidad " + unit["name"])
        return errors

    @staticmethod
    def min_exercises_in_exam(challenge, errors):
        for unit in challenge.units:
            result = ExerciseController.find(unit["exam"]["id"])
            exercises = result.get("exercises")
            if len(exercises) != 16:
                errors.append("Se requiere un minimo de 16 ejercicios en el examen de la unidad " + unit["name"])
        return errors