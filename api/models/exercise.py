import mongoengine
from mongoengine import Document


class Exercise(Document):
    exercise_type = mongoengine.StringField()
    question = mongoengine.StringField()
    options = mongoengine.ListField()
    correct_answer = mongoengine.StringField()
    lesson_id = mongoengine.StringField()
    exercise_id = mongoengine.StringField()

    def to_json(self):
        result = self.to_mongo().to_dict()
        if "_id" in result:
            del result["_id"]
        return result