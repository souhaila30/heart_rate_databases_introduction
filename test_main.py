from main import calculate_hr, check_tachycardia
import pytest
from validate import validate_input_email,validate_input_hr, validate_input_age

def test_mean():
    data = [50,60,70,80,90]
    avg = calculate_hr(data)
    assert avg == 70

def test_tachycardia():
    assert check_tachycardia(12, 120) == "Tachycardia: True"
    assert check_tachycardia(24,60) == "Tachycardia: False"
    assert check_tachycardia(100,112) == "Tachycardia: True"

input1 = {"user.email": 10, "user.age": 24, "heart.rate":100}
input2 = {"user.email":"san@duke.edu", "user.age":2.5, "heart.rate":80}
input3 = {"user.email":"san@duke.edu", "user.age":10, "heart.rate":"80"}

def test_age():
    with pytest.raises(ValueError):
        validate_input_age(input3)
        validate_input_age(input2)

def test_email():
    with pytest.raises(TypeError):
        validate_input_email(input1)
        #validate_input_email(input2)

def test_heart_rate():
    with pytest.raises(ValueError):
        validate_input_hr(input1)
        validate_input_hr(input3)
