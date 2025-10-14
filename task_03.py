import re

def normalize_phone(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        raise ValueError("phone_number must be a string")

    stripped_number = phone_number.strip()
    digits = re.sub(r"\D", '', stripped_number)

    if not digits:
        return ""

    if phone_number.startswith('+') or digits.startswith('380'):
        return '+' + digits
    
    return "+38" + digits