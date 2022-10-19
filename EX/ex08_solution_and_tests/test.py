"""Testing solution."""


import pytest
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study__evening_coffee_doesnt_matter():
    """Test whether drinking coffee matters when studying in the evening."""
    assert students_study(18, True) is True
    assert students_study(24, True) is True
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test_students_study__daytime_coffee_matters():
    """Test if drinking coffee affects studying in the daytime."""
    assert students_study(5, True) is True
    assert students_study(17, True) is True
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test_students_study__nighttime_no_study():
    """Test whether students study at night."""
    assert students_study(1, True) is False
    assert students_study(4, True) is False
    assert students_study(1, False) is False
    assert students_study(4, False) is False


def test_lottery__winning_numbers():
    """Test if winning numbers are correct."""
    assert lottery(5, 5, 5) == 10


def test_lottery__middle_win():
    """Test if matching 3 numbers guarantee middle win."""
    assert lottery(1, 1, 1) == 5
    assert lottery(10, 10, 10) == 5
    assert lottery(-1, -1, -1) == 5
    assert lottery(0, 0, 0) == 5


def test_lottery__b_and_c_diff():
    """Test if b and c are different from "a"."""
    assert lottery(1, 5, 5) == 1
    assert lottery(10, 1, 1) == 1
    assert lottery(1, 2, 3) == 1


def test_lottery__b_or_c_match_a():
    """Test results when b or c match "a"."""
    assert lottery(1, 1, 5) == 0
    assert lottery(1, 5, 1) == 0


def test_fruit_order__not_enough_baskets():
    """Test results for not enough baskets."""
    assert fruit_order(1, 1, 7) == -1
    assert fruit_order(5, 5, 32) == -1


def test_fruit_order__consider_big_baskets_first():
    """Test if function considers big baskets before small baskets."""
    assert fruit_order(10, 1, 10) == 5
    assert fruit_order(4, 5, 21) == 1


def test_fruit_order__zero_amount():
    """Test results when the amount is zero."""
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(5, 4, 0) == 0
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order__only_big():
    """Test results with only big baskets."""
    assert fruit_order(0, 5, 25) == 0
    assert fruit_order(0, 5, 30) == -1
    assert fruit_order(5, 5, 30) == 5
    assert fruit_order(0, 4, 28) == -1
    assert fruit_order(0, 8, 20) == 0
    assert fruit_order(0, 5, 23) == -1


def test_fruit_order__only_small():
    """Test results with only small baskets."""
    assert fruit_order(6, 0, 6) == 6
    assert fruit_order(6, 0, 8) == -1
    assert fruit_order(3, 0, 3) == 3
    assert fruit_order(2, 0, 4) == -1
    assert fruit_order(6, 2, 9) == 4


def test_fruit_order__other():
    """Test other results."""
    assert fruit_order(3, 3, 18) == 3
    assert fruit_order(4, 5, 19) == 4
    assert fruit_order(2, 4, 24) == -1
    assert fruit_order(9, 2, 21) == -1
    assert fruit_order(2, 42, 214) == -1
    assert fruit_order(12, 44, 232) == 12
