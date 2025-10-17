from lib.age_checker import *

def test_age_checker():
    # age_checker_today = datetime.strptime('1960-10-21')
    assert age_checker('1960-10-21') == "access granted"

def test_age_checker_too_young():
    assert age_checker('2019-01-22') == "access denied, you are 6, the required age is 16"

def test_age_checker_also_too_young():
        assert age_checker('2015-01-22') == "access denied, you are 10, the required age is 16"

def test_age_checker_birthday():
     assert age_checker('2009-10-18') == "access denied, you are 15, the required age is 16"

