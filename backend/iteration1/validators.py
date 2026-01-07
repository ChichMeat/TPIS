def validate_phone_number(phone):
    """
    Валидация российского номера телефона
    Возвращает True если номер корректен
    """
    import re
    pattern = r'^(\+7|7|8)\d{10}$'
    return bool(re.match(pattern, str(phone)))

def validate_email(email):
    """Простая валидация email"""
    return '@' in email and '.' in email
