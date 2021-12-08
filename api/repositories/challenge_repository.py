from api.models.challenge import Challenge


class ChallengeRepository:

    @staticmethod
    def add(challenge):
        return challenge.save()

    @staticmethod
    def delete_all():
        Challenge.objects().delete()

    @staticmethod
    def get_all(published=None):
        if published is None:
            return Challenge.objects()
        else:
            return Challenge.objects(published=published == 'true')

    @staticmethod
    def add_unit(challenge_id, new_unit):
        result = ChallengeRepository.get_by_id(challenge_id)
        challenge = result.get()
        units = challenge.units
        for unit in units:
            if unit["name"] == new_unit["name"]:
                return "Nombre de la unidad ya utilizado"
        units.append(new_unit)
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
    def get_challenge_by_name(challenge_name):
        result = Challenge.objects(name=challenge_name)
        if result.count() < 1:
            pass
        return result


    @staticmethod
    def edit_challenge(challenge_id, new_challenge):
        challenge = Challenge.objects(challenge_id=challenge_id)
        if len(challenge) == 0:
            return
        else:

            challenge = challenge.get()
            new_units = list(map(lambda unit: unit.dict(), new_challenge.units))
            challenge.units = new_units
            challenge.name = new_challenge.name
            challenge.published = new_challenge.published
            challenge.save()
            return challenge

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
        challenges = Challenge.objects.filter()
        if len(challenges) == 0:
            return "C" + str(1)
        else:
            ids = [int(challenge.challenge_id.split('C')[1]) for challenge in challenges]
            max_id = max(ids)
            next_id = max_id + 1
            return "C" + str(next_id)
