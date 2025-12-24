import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    """
    Валидатор российских номеров телефонов
    Форматы: +7XXX..., 8XXX..., 7XXX...
    """
    pattern = r'^(\+7|7|8)?\d{10}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Введите корректный номер телефона (10 цифр после +7/8)'
        )
    return value
