from lib.age_checker import *
import pytest

def test_age_checker():
    # age_checker_today = datetime.strptime('1960-10-21')
    assert age_checker('1960-10-21') == "access granted"

def test_age_checker_too_young():
    assert age_checker('2019-01-22') == "access denied, you are 6, the required age is 16"

def test_age_checker_also_too_young():
        assert age_checker('2015-01-22') == "access denied, you are 10, the required age is 16"

def test_age_checker_birthday():
    assert age_checker('2009-10-18') == "access denied, you are 15, the required age is 16"

def test_age_check_wrong_type():
    with pytest.raises(Exception) as e:
        age_checker(6)
    error_message = str(e.value)
    assert error_message == 'DOB must be a string in format YYYY-MM-DD'

def test_age_checker_wrong_format():
    with pytest.raises(ValueError) as e:
        age_checker('hello')
    error_message = str(e.value)
    assert error_message == 'Invalid DOB format, must be YYYY-MM-DD'


def test_age_checker_future():
    with pytest.raises(Exception) as e:
        age_checker('3000-10-10')
    error_message = str(e.value)
    assert error_message == 'Cannot be date in the future'

