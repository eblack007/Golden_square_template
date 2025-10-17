from dateutil.parser import *
from datetime import datetime
from dateutil.relativedelta import relativedelta




def age_checker(some_DOB):
    today = datetime.now()

    # date_format = '%Y-%m-%d'
    DOB_datetime = parser().parse(some_DOB)
    # diff_today_DOB = today - DOB_datetime
    # years_diff = (diff_today_DOB.days) / 365
    # return years_diff
    age = relativedelta(today, DOB_datetime)

    if age.years >= 16:
        return "access granted"
    return f"access denied, you are {age.years}, the required age is 16"

    