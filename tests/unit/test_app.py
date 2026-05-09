import pytest
from app import list_duties
import db

@pytest.fixture(autouse=True)
def reset_duties():
    db.duties.clear()
    db.duties.extend([
        {
        "identifier": 5, 
        "description": "Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts"
    },
    {
        "identifier": 7, 
        "description": "Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)"
    },
    {
        "identifier": 10, 
        "description": "Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable"
    }
    ])

    db.error_message = None
# def test_list_duties_returns_a_list_component():
#     result = list_duties()
#     assert isinstance(result, list)

# def test_list_duties_returns_at_least_one_duty():
#     result = list_duties()
#     assert len(result) > 0
#     # assert 'duty1' in result

# def test_list_duties_returns_at_least_two_duties():
#     result = list_duties()
#     assert len(result) > 1
    # assert 'duty2' in result

# def test_list_duties_returns_all_duties():
#     duty_list = ['duty1', 'duty2', 'duty3', 'duty4', 'duty5', 'duty6', 'duty7', 'duty8', 'duty9', 'duty10', 'duty11', 'duty12', 'duty13']
#     result = list_duties() 

#     for duty in duty_list:
#         assert duty in result

# def test_list_duties_returns_a_dictionary_of_duties_with_duty_number_and_description():
#     result = list_duties() 
#     duty_list = [
#                     {"Duty Number": 1, "Description": "Duty 1 description"},
#                     {"Duty Number": 2, "Description": "Duty 2 description"},
#                     {"Duty Number": 3, "Description": "Duty 3 description"},
#                     {"Duty Number": 4, "Description": "Duty 4 description"},
#                     {"Duty Number": 5, "Description": "Duty 5 description"},
#                     {"Duty Number": 6, "Description": "Duty 6 description"},
#                     {"Duty Number": 7, "Description": "Duty 7 description"},
#                     {"Duty Number": 8, "Description": "Duty 8 description"},
#                     {"Duty Number": 9, "Description": "Duty 9 description"},
#                     {"Duty Number": 10, "Description": "Duty 10 description"},
#                     {"Duty Number": 11, "Description": "Duty 11 description"},
#                     {"Duty Number": 12, "Description": "Duty 12 description"},
#                     {"Duty Number": 13, "Description": "Duty 13 description"} 
#                 ]
    
#     assert result == duty_list
#     for duty in duty_list:
#          assert duty in result

# @pytest.fixture
# def list_duties():
#     duty_list = [
#                     {"Duty Number": 1, "Description": "Duty 1 description"},
#                     {"Duty Number": 2, "Description": "Duty 2 description"},
#                     {"Duty Number": 3, "Description": "Duty 3 description"},
#                     {"Duty Number": 4, "Description": "Duty 4 description"},
#                     {"Duty Number": 5, "Description": "Duty 5 description"},
#                     {"Duty Number": 6, "Description": "Duty 6 description"},
#                     {"Duty Number": 7, "Description": "Duty 7 description"},
#                     {"Duty Number": 8, "Description": "Duty 8 description"},
#                     {"Duty Number": 9, "Description": "Duty 9 description"},
#                     {"Duty Number": 10, "Description": "Duty 10 description"},
#                     {"Duty Number": 11, "Description": "Duty 11 description"},
#                     {"Duty Number": 12, "Description": "Duty 12 description"},
#                     {"Duty Number": 13, "Description": "Duty 13 description"} 
#                 ]
#     return duty_list

# def test_duty_has_identifier(mocker):

#     mock_data = {
#         'identifier': 1,
#         'description': 'duty 1 description' 
#     }

#     mocker.patch('db.get_all_duties', return_value = mock_data)
#     duty_1 = db.get_all_duties()
#     assert 'identifier' in duty_1

# def xtest_duty_has_description():
#     duty_1 = db.get_duty(1)
#     assert hasattr(duty_1, 'description')

# def xtest_duty_1_description_has_correct_identifier():
#     duty_1 = db.get_duty(1)
#     assert duty_1.identifier == 1

def test_add_duty_adds_new_duty_to_duties_variable():
    new_duty = {
        "identifier": "12",
        "description": "Stored duty"
    }

    db.add_duty(new_duty)

    duties = db.get_all_duties()

    assert new_duty in duties

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

def test_validate_duty_returns_None_for_valid_duty():
    new_duty = {
        "identifier": "12",
        "description": "Valid duty"
    }
    result = db.validate_duty(new_duty)

    assert result is None

