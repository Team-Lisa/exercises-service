import mongoengine
from mongoengine import Document


class Challenge(Document):
    name = mongoengine.StringField()
    units = mongoengine.ListField()
    challenge_id = mongoengine.StringField()
    published = mongoengine.BooleanField()

    def to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result
