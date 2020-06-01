from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(val):
    validate_it = URLValidator()
    try:
        validate_it(val)
    except:
        raise ValidationError('Invalid URL provided')
    return val

def validate_dot_com(val):
    if not "com" in val:
        raise ValidationError("Invalid URL, as suffix is not .com")
    return val
