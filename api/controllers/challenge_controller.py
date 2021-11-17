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
        ChallengeRepository.add_unit(challenge_id, unit.dict())
        return {"message": "unit created"}

    @staticmethod
    def add_lesson(challenge_id, unit_id, lesson):
        ChallengeRepository.add_lesson(challenge_id, unit_id, lesson.dict())
        return {"message": "lesson created"}

    @staticmethod
    def delete_challenge(challenge_id=None):
        if not challenge_id:
            ChallengeRepository.delete_all()
        else:
            ChallengeRepository.delete(challenge_id)
        return {"message": "challenge deleted"}

    @staticmethod
    def delete_unit(challenge_id, unit_id):
        ChallengeRepository.delete_unit(challenge_id, unit_id)
        return {"message": "unit deleted"}

    @staticmethod
    def delete_lesson(challenge_id, unit_id, lesson_id):
        ChallengeRepository.delete_lesson(challenge_id, unit_id, lesson_id)
        return {"message": "lesson deleted"}

    @staticmethod
    def get_next_challenge_id():
        # Ids:
        #   - "C1" is for Challenge 1
        #   - "C1U1" is for Challenge 1, Unit 1
        #   - "C1U1L1" is for Challenge 1, Unit1, Lesson 1
        #   - "C1U1L1E1" is for Challenge 1, Unit 1, Lesson 1, Exercise 1
        #   - "C1U1E" is for Challenge 1, Unit 1, Exam
        #   - "C1U1EE1" is for Challenge 1, Unit 1, Exam, Exercise 1
        result = ChallengeRepository.get_next_id()
        return {"challenges_next_id": result}
