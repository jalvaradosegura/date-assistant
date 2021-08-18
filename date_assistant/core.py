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

    def add_months(self, num_months: int) -> str:
        self._date += relativedelta(months=num_months)
        self.date = self._date.strftime('%Y-%m-%d')
        return self.date

    def months_diff_with(self, date_to_compare: str) -> int:
        date_to_compare = datetime.strptime(date_to_compare, '%Y-%m-%d')
        diff = relativedelta(self._date, date_to_compare)
        return abs(diff.months + (12 * diff.years))

    def months_started_since(self, date_to_compare: str) -> int:
        date_to_compare = datetime.strptime(date_to_compare, '%Y-%m-%d')
        months_diff = self._date.month - date_to_compare.month
        return abs((self._date.year - date_to_compare.year) * 12 + months_diff)

    def months_started_until(self, date_to_compare: str) -> int:
        return self.months_started_since(date_to_compare)

    def add_years(self, num_years: int) -> str:
        self._date += relativedelta(years=num_years)
        self.date = self._date.strftime('%Y-%m-%d')
        return self.date

    def years_diff_with(self, date_to_compare: str) -> int:
        date_to_compare = datetime.strptime(date_to_compare, '%Y-%m-%d')
        diff = relativedelta(self._date, date_to_compare)
        return abs(diff.years)

    def years_started_since(self, date_to_compare: str) -> int:
        date_to_compare = datetime.strptime(date_to_compare, '%Y-%m-%d')
        years_diff = self._date.year - date_to_compare.year
        return abs(years_diff)

    def years_started_until(self, date_to_compare: str) -> int:
        return self.years_started_since(date_to_compare)
