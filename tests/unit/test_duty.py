import db
from duty import Duty

def test_duty_class_stores_identifier():
    new_duty = Duty("12", "Test description")
    assert new_duty.identifier == "12"

def test_duty_class_stores_description():
    new_duty = Duty("12", "Test description")
    assert new_duty.description == "Test description"

def test_add_duty_stores_a_duty_object():
    new_duty = {
        "identifier": "15",
        "description": "Object test"
    }

    db.add_duty(new_duty)
    duties = db.get_all_duties()
    assert isinstance(duties[-1], Duty)