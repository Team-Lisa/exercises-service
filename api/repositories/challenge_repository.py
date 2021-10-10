from api.models.challenge import Challenge


class ChallengeRepository:

    @staticmethod
    def add(challenge):
        return challenge.save()

    @staticmethod
    def delete_all():
        Challenge.objects().delete()

    @staticmethod
    def get_all():
        return Challenge.objects()

    @staticmethod
    def add_unit(challenge_id, unit):
        result = ChallengeRepository.get_by_id(challenge_id)
        challenge = result.get()
        units = challenge.units
        units.append(unit)
        result.update(set__units=units)

    @staticmethod
    def add_lesson(challenge_id, unit_id, lesson):
        result = ChallengeRepository.get_by_id(challenge_id)
        challenge = result.get()

        units = challenge.units
        for unit in units:
            if unit.get("id") == unit_id:
                unit.get("lessons").append(lesson)
                break
        result.update(set__units=units)

    @staticmethod
    def get_by_id(challenge_id):
        result = Challenge.objects(challenge_id=challenge_id)
        if result.count() < 1:
            pass
        return result

    @staticmethod
    def delete(challenge_id):
        Challenge.objects(challenge_id=challenge_id).delete()

