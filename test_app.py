from app import list_duties

def test_list_duties_returns_a_list_component():
    list_duties()
    assert list_duties() == []