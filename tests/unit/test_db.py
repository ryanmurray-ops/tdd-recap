import pytest
import db
from duty import Duty

@pytest.fixture(autouse=True)
def reset_duties():
    db.duties.clear()
    db.duties.extend([
        Duty(
            5,
            "Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts"
        ),
        Duty(
            7,
            "Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)"
        ),
        Duty(
            10,
            "Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable"
        ),
        
    ])

    db.error_message = None

def test_add_duty_adds_new_duty_to_duties_variable():
    new_duty = {
        "identifier": "12",
        "description": "Stored duty"
    }

    db.add_duty(new_duty)

    duties = db.get_all_duties()

    found_duty = False

    for duty in duties:
        if duty.identifier == "12" and duty.description == "Stored duty":
            found_duty = True
    assert found_duty is True

def test_identifier_is_unique_returns_false_for_duplicate_identifier():
    db.add_duty({
        "identifier": "12",
        "description": "First duty"
    })

    result = db.identifier_is_unique("12")

    assert result is False

def test_validate_duty_returns_false_for_empty_identifier():
    new_duty = {
        "identifier": "",
        "description": "Valid description"
    }

    result =  db.validate_duty(new_duty)

    assert result == "Please enter a duty number"

def test_validate_duty_returns_false_for_empty_description():
    new_duty = {
        "identifier": "12",
        "description": ""
    }

    result =  db.validate_duty(new_duty)

    assert result == "Please enter a duty description"

def test_validate_duty_returns_none_for_valid_duty():
    new_duty = {
        "identifier": "12",
        "description": "Valid duty"
    }
    result = db.validate_duty(new_duty)

    assert result is None

