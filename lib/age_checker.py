from datetime import datetime
import dateutil


def age_checker(some_DOB):
    # return datetime.strptime('1960-10-21')
    # return "access granted"
    today = datetime.now().date()
    # formatted_today = datetime.strptime(today, "%Y-%m-%d")
    DOB_datetime = datetime.strptime(some_DOB, "%Y-%m-%d").date()
    diff_today_DOB = today - DOB_datetime
    years_diff = int((diff_today_DOB.days) / 365)
    if years_diff >= 16:
        return "access granted"
    return f"access denied, you are {years_diff}, the required age is 16"