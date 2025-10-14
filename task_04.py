from datetime import datetime, timedelta
from typing import List, Dict
    

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
