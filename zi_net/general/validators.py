import re

def validate_ethiopian_phone_number(value):
    pattern = r'^[971]\d{8}$'
    if not re.match(pattern, value):
        raise ValueError("Invalid Ethiopian Phone Number.")
    return value
