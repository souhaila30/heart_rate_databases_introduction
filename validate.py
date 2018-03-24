def validate_input_email(POST):
    """raises a value error if email is not a string"""
    if isinstance("user_email", int):
        pass
    else:
        raise TypeError("Email must be a string")

def validate_input_hr(POST):
    """raises value error if heart rate is not a number"""
    if isinstance("heart_rate", float):
        pass
    else:
        raise ValueError("heart rate must be a number")

def validate_input_age(POST):
    """raises a value error if age is not an integer"""
    if isinstance("user_age", int):
        pass
    else:
        raise ValueError("Age must be an integer")



