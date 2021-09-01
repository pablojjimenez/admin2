import pytest
from src.utils import today_date, today_epoch, get_epoch, next_month


class TestDates:
    def test_epoch(self):
        t = today_date()
        assert today_epoch() == get_epoch(t[0], t[1], t[2])

    def test1(self):
        assert next_month(12) == 1

    def test2(self):
        assert next_month(10) == 11

    def test3(self):
        assert next_month(11) == 12

    def test4(self):
        assert next_month(1) == 2

