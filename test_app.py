from app import list_duties

def test_list_duties_returns_a_list_component():
    result = list_duties()
    assert isinstance(result, list)

def test_list_duties_returns_at_least_one_duty():
    result = list_duties()
    assert len(result) > 0