from hypothesis.internal.compat import hrange
from hypothesis.tests.common.debug import minimal, find_any

from date_strategies import dates


def test_can_find_after_the_year_2000():
    assert minimal(dates(), lambda x: x.year > 2000).year == 2001


def test_can_find_before_the_year_2000():
    assert minimal(dates(), lambda x: x.year < 2000).year == 1999


def test_can_find_each_month():
    for month in hrange(1, 13):
        find_any(dates(), lambda x: x.month == month)


def test_min_year_is_respected():
    assert minimal(dates(min_year=2003)).year == 2003


def test_max_year_is_respected():
    assert minimal(dates(max_year=1998)).year == 1998
