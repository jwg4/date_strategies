class DateStrategy(SearchStrategy):

    def __init__(self, min_value, max_value):
        assert isinstance(min_value, dt.date)
        assert isinstance(max_value, dt.date)
        assert min_value < max_value
        self.min_value = min_value
        self.days_apart = (max_value - min_value).days
        self.center = (dt.date(2000, 1, 1) - min_value).days

    def do_draw(self, data):
        return self.min_value + dt.timedelta(days=utils.centered_integer_range(
            data, 0, self.days_apart, center=self.center))
