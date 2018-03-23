from main import calculate_hr, check_tachycardia
def test_mean():
    data = [50,60,70,80,90]
    avg = calculate_hr(data)
    assert avg == 70

def test_tachycardia():
    assert check_tachycardia(12, 120) == "Tachycardia: True"
    assert check_tachycardia(24,60) == "Tachycardia: False"
    assert check_tachycardia(100,112) == "Tachycardia: True"

def test_value_age('san33@duke.edu'):
    age = return_age(email)
    asset age == 24
