from duty import Duty

def test_duty_class_stores_identifier():
    new_duty = Duty("12", "Test description")
    assert new_duty.identifier == "12"