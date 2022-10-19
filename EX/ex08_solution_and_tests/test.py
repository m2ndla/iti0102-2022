"""Testing solution."""


import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order

def test_students_study__evening_coffee_doesnt_matter():
    assert students_study(19, True) is True
    assert students_study(19, False) is True


def test_students_study__daytime_coffee_matters():
    assert students_study(12, True) is True
    assert students_study(12, False) is False


def test_students_study__nighttime_no_study():
    assert students_study(1, True) is False
    assert students_study(4, False) is False
