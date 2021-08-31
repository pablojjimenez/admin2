import pytest
from src.utils import today_date, today_epoch, get_epoch


class TestDates:
    def test_epoch(self):
        t = today_date()
        assert today_epoch() == get_epoch(t[0], t[1], t[2])
