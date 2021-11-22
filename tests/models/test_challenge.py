from api.models.challenge import Challenge


def test_model_with_empty_units_to_json():
    name = "mock_name"
    units = []
    challenge_id = "d1"
    published = True
    challenge = Challenge(name=name, units=units, challenge_id=challenge_id, published=published)
    assert challenge.to_json() == {
        "name": name,
        "units": units,
        "challenge_id": challenge_id,
        "published": published
    }


