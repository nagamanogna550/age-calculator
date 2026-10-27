import datetime as dt
from age_calculator import calculate_age


def test_basic():
    assert calculate_age(dt.date(2000, 1, 15), dt.date(2026, 10, 22)) == (26, 9, 7)


def test_day_borrow():
    assert calculate_age(dt.date(2000, 1, 31), dt.date(2026, 3, 1)) == (26, 1, 1)


def test_leap_day_birth():
    assert calculate_age(dt.date(2000, 2, 29), dt.date(2024, 2, 29)) == (24, 0, 0)


def test_same_day():
    assert calculate_age(dt.date(2026, 10, 22), dt.date(2026, 10, 22)) == (0, 0, 0)


if __name__ == "__main__":
    test_basic()
    test_day_borrow()
    test_leap_day_birth()
    test_same_day()
    print("All tests passed!")