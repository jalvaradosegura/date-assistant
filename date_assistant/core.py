from datetime import datetime

from dateutil.relativedelta import relativedelta


class DateAssistant:
    def __init__(self, date: str):
        self.date = date
        self._date = datetime.strptime(date, '%Y-%m-%d')

    def __repr__(self):
        return f'DateAssistant({self.date!r})'

    def __str__(self):
        return self.date

    def add_days(self, num_days: int) -> str:
        self._date += relativedelta(days=num_days)
        self.date = self._date.strftime('%Y-%m-%d')
        return self.date

    def days_diff_with(self, date_to_compare: str) -> int:
        date_to_compare = datetime.strptime(date_to_compare, '%Y-%m-%d')
        return abs(self._date - date_to_compare).days
