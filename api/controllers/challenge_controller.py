from api.repositories.challenge_repository import ChallengeRepository
from api.models.challenge import Challenge


class ChallengeController:

    @staticmethod
    def create(challenge):
        units = list(map(lambda unit: unit.dict(), challenge.units))
        challenge_to_save = Challenge(name=challenge.name, units=units, challenge_id=challenge.id)
        result = ChallengeRepository.add(challenge_to_save)
        return {"challenge": result.to_json()}

    @staticmethod
    def find():
        result = ChallengeRepository.get_all()
        result = map(lambda challenge: challenge.to_json(), list(result))
        return {"challenges": list(result)}

    @staticmethod
    def add_unit(challenge_id, unit):
        ChallengeRepository.add_unit(challenge_id, unit.json())
        return {"message": "unit created"}

    @staticmethod
    def add_lesson(challenge_id, unit_id, lesson):
        ChallengeRepository.add_lesson(challenge_id, unit_id, lesson.json())
        return {"message": "lesson created"}

    @staticmethod
    def delete_challenge(challenge_id):
        ChallengeRepository.delete(challenge_id)
        return {"message": "challenge deleted"}