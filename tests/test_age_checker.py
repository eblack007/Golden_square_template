from lib.age_checker import age_checker

def test_age_checker():
    # age_checker_today = datetime.strptime('1960-10-21')
    assert age_checker('1960-10-21') == "access granted"

def test_age_checker_too_young():
    assert age_checker('2019-01-22') == "access denied"