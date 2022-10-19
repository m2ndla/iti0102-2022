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
    assert students_study(6, True) is True
    assert students_study(7, True) is True
    assert students_study(8, True) is True
    assert students_study(9, True) is True
    assert students_study(10, True) is True
    assert students_study(11, True) is True
    assert students_study(12, True) is True
    assert students_study(13, True) is True
    assert students_study(14, True) is True
    assert students_study(15, True) is True
    assert students_study(16, True) is True
    assert students_study(17, True) is True
    assert students_study(5, False) is False
    assert students_study(6, False) is False
    assert students_study(7, False) is False
    assert students_study(8, False) is False
    assert students_study(9, False) is False
    assert students_study(10, False) is False
    assert students_study(11, False) is False
    assert students_study(12, False) is False
    assert students_study(13, False) is False
    assert students_study(14, False) is False
    assert students_study(15, False) is False
    assert students_study(16, False) is False
    assert students_study(17, False) is False


def test_students_study__nighttime_no_study():
    """Test whether students study at night."""
    assert students_study(1, True) is False
    assert students_study(2, True) is False
    assert students_study(3, True) is False
    assert students_study(4, True) is False
    assert students_study(1, False) is False
    assert students_study(2, False) is False
    assert students_study(3, False) is False
    assert students_study(4, False) is False
