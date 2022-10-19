"""Testing solution."""


import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study__evening_coffee_doesnt_matter():
    """Test whether drinking coffee matters when studying in the evening."""
    assert students_study(18, True) is True
    assert students_study(19, True) is True
    assert students_study(20, True) is True
    assert students_study(21, True) is True
    assert students_study(22, True) is True
    assert students_study(23, True) is True
    assert students_study(24, True) is True
    assert students_study(18, False) is True
    assert students_study(19, False) is True
    assert students_study(20, False) is True
    assert students_study(21, False) is True
    assert students_study(22, False) is True
    assert students_study(23, False) is True
    assert students_study(24, False) is True


def test_students_study__daytime_coffee_matters():
    """Test if drinking coffee affects studying in the daytime."""
    assert students_study(5, True) is True
    assert students_study(17, False) is False


def test_students_study__nighttime_no_study():
    """Test whether students study at night."""
    assert students_study(1, True) is False
    assert students_study(4, False) is False
