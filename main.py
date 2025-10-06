from datetime import datetime, timedelta
import random
import re
from typing import List, Dict

#Task 1
def get_days_from_today(date_string: str) -> int:
    try:
        parsed_date = datetime.strptime(date_string.strip(), '%Y-%m-%d').date()
    except (AttributeError, TypeError) as e:
        raise ValueError("Expected 'YYYY-MM-DD' string.") from e
    except ValueError as e:
        raise ValueError(
            f"Invalid date {date_string}: expected 'YYYY-MM-DD' (e.g., '2025-10-05')."
        ) from e
        
    actual_date = datetime.today().date()

    return (actual_date - parsed_date).days
    
#Task2
def get_numbers_ticket(min_value: int, max_value:int, quantity:int) -> list[int]:
    return_value = []

    if not all(type(x) is int for x in (min_value, max_value, quantity)):
        return return_value

    if min_value < 1 or max_value > 1000 or min_value > max_value:
        return return_value
    
    quantity_range_size = max_value - min_value + 1
    if not (1 <= quantity <= quantity_range_size):
        return return_value
    
    return_value = sorted(random.sample(range(min_value, max_value + 1), k=quantity))

    return return_value

#Task3
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

#Task4
def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today_date = datetime.today().date()
    end_date = today_date + timedelta(days=7)
    res = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today_date.year)

        if birthday_this_year < today_date:
            birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

        if today_date <= birthday_this_year <= end_date:
            week_day = birthday_this_year.weekday()
            if week_day == 5:
                birthday_this_year += timedelta(days=2)
            elif week_day == 6:
                birthday_this_year += timedelta(days=1)

            res.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
            })

    return res
