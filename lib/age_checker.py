from dateutil.parser import *
from datetime import datetime



def age_checker(some_DOB):
    # return datetime.strptime('1960-10-21')
    # return "access granted"
    today = datetime.now()
    # formatted_today = datetime.strptime(today, "%Y-%m-%d")
    DOB_datetime = parser.parse(some_DOB)
    diff_today_DOB = today - DOB_datetime
    # years_diff = int((diff_today_DOB.days) / 365)
    if diff_today_DOB >= 16:
        return "access granted"
    return f"access denied, you are {diff_today_DOB}, the required age is 16"
    