from api.models.challenge import Challenge
from api.repositories.challenge_repository import ChallengeRepository


class ChallengesValidator:

    @staticmethod
    def is_valid(challenge: Challenge):
        errors = []
        ChallengesValidator.validate_name(challenge, errors)
        ChallengesValidator.validate_units_in_challenge(challenge, errors)
        if len(errors) == 0:
            return (True, [])
        return (False,errors)

    @staticmethod
    def validate_name(challenge, errors):
        if len(ChallengeRepository.get_challenge_by_name(challenge.name)) > 0:
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
                errors.append("Nombre de la unidad ya utilizado")
                return errors
