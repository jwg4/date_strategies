```
>>> from date_strategies import dates
>>> from hypothesis import given

>>> def is_leap_day(d):
...     return True

>>> @given(dates())
... def test_leap_day_function(d)
...     assertIsNotNone(is_leap_day(d))

```
