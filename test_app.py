from app import list_duties

def test_list_duties_returns_a_list_component():
    result = list_duties()
    assert isinstance(result, list)

def test_list_duties_returns_at_least_one_duty():
    result = list_duties()
    assert len(result) > 0
    assert 'duty1' in result

def test_list_duties_returns_at_least_two_duties():
    result = list_duties()
    assert len(result) > 1
    assert 'duty2' in result

def test_list_duties_returns_all_duties():
    duty_list = ['duty1', 'duty2', 'duty3', 'duty4', 'duty5', 'duty6', 'duty7', 'duty8', 'duty9', 'duty10', 'duty11', 'duty12', 'duty13']
    result = list_duties() 

    for duty in duty_list:
        assert duty in result