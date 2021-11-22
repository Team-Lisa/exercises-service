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

    @staticmethod
    def delete_unit(challenge_id, unit_id):
        index_to_delete = ""
        result = ChallengeRepository.get_by_id(challenge_id)
        challenge = result.get()
        units = challenge.units
        for i in range(len(units)):
            if units[i].get("id") == unit_id:
                index_to_delete = i
                break
        if index_to_delete != "":
            units.pop(index_to_delete)
            result.update(set__units=units)

    @staticmethod
    def delete_lesson(challenge_id, unit_id, lesson_id):
        result = ChallengeRepository.get_by_id(challenge_id)
        challenge = result.get()
        units = challenge.units
        for i in range(len(units)):
            if units[i].get("id") == unit_id:
                lessons = units[i].get("lessons")
                for j in range(len(lessons)):
                    if lessons[j].get("id") == lesson_id:
                        lessons.pop(j)
                        units[i]["lessons"] = lessons
                        result.update(set__units=units)
                        return

    @staticmethod
    def get_next_id():
        challenges = Challenge.objects.filter().order_by('-challenge_id')
        if len(challenges) == 0:
            return "C" + str(1)
        else:
            next_id = int(challenges[0].challenge_id.split('C')[1]) + 1
            return "C" + str(next_id)
