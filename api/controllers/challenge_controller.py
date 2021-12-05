from fastapi import HTTPException

from api.repositories.challenge_repository import ChallengeRepository
from api.models.challenge import Challenge
from api.services.challenges_validator import ChallengesValidator


class ChallengeController:

    @staticmethod
    def create(challenge):
        units = list(map(lambda unit: unit.dict(), challenge.units))
        challenge_to_save = Challenge(name=challenge.name, units=units, challenge_id=challenge.id, published=challenge.published)
        is_valid, errors = ChallengesValidator.is_valid(challenge_to_save)
        if is_valid:
            result = ChallengeRepository.add(challenge_to_save)
            return {"challenge": result.to_json()}
        else:
            raise HTTPException(status_code=400, detail={"errors": errors})

    @staticmethod
    def find(published):
        result = ChallengeRepository.get_all(published)
        result = map(lambda challenge: challenge.to_json(), list(result))
        return {"challenges": list(result)}

    @staticmethod
    def add_unit(challenge_id, unit):
        errors = ChallengeRepository.add_unit(challenge_id, unit.dict())
        if errors:
            return  {"errors": errors}
        return {"message": "unit created"}

    @staticmethod
    def add_lesson(challenge_id, unit_id, lesson):
        ChallengeRepository.add_lesson(challenge_id, unit_id, lesson.dict())
        return {"message": "lesson created"}

    @staticmethod
    def edit_challenge(challenge_id, challenge):
        units = list(map(lambda unit: unit.dict(), challenge.units))
        new_challenge = Challenge(name=challenge.name, units=units, challenge_id=challenge.id,
                                      published=challenge.published)
        is_valid, errors = ChallengesValidator.is_valid(new_challenge)
        if is_valid:
            challenge_updated = ChallengeRepository.edit_challenge(challenge_id, challenge)
            if challenge_updated == None:
                return {"challenge": {}}
            return {"challenge": challenge_updated.to_json()}
        else:
            raise HTTPException(status_code=400, detail={"errors": errors})

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
        #   - "C1U1XE1" is for Challenge 1, Unit 1, Exam, Exercise 1
        result = ChallengeRepository.get_next_id()
        return {"challenges_next_id": result}

    @staticmethod
    def get_challenge_by_challenge_id(challenge_id):
        result = ChallengeRepository.get_by_id(challenge_id)
        return {"challenge": result[0].to_json()}
