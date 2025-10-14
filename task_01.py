from datetime import datetime

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