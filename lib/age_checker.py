from dateutil.parser import *
from datetime import datetime
from dateutil.relativedelta import relativedelta




def age_checker(some_DOB):
    if not isinstance(some_DOB, str):
        raise TypeError('DOB must be a string in format YYYY-MM-DD')


    today = datetime.now()

    # date_format = '%Y-%m-%d'
    try:
        DOB_datetime = parser().parse(some_DOB)
    except ParserError:
        raise ValueError('Invalid DOB format, must be YYYY-MM-DD')
    
    if DOB_datetime > today:
        raise Exception('Cannot be date in the future')

    # diff_today_DOB = today - DOB_datetime
    # years_diff = (diff_today_DOB.days) / 365
    # return years_diff
    age = relativedelta(today, DOB_datetime)


    if age.years >= 16:
        return "access granted"
    return f"access denied, you are {age.years}, the required age is 16"
    

    