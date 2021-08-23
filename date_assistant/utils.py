from datetime import datetime

from dateutil.relativedelta import relativedelta

from date_assistant.formats import YYYY_MM_DD


def get_days_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1 = cast_str_to_datetime(date1, date1_format)
    date2 = cast_str_to_datetime(date2, date2_format)
    return abs(date1 - date2).days


def get_months_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1 = cast_str_to_datetime(date1, date1_format)
    date2 = cast_str_to_datetime(date2, date2_format)
    diff = relativedelta(date1, date2)
    return abs(diff.months + (12 * diff.years))


def get_months_started_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1 = cast_str_to_datetime(date1, date1_format)
    date2 = cast_str_to_datetime(date2, date2_format)
    months_diff = date1.month - date2.month
    return abs((date1.year - date2.year) * 12 + months_diff)


def get_years_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1 = cast_str_to_datetime(date1, date1_format)
    date2 = cast_str_to_datetime(date2, date2_format)
    diff = relativedelta(date1, date2)
    return abs(diff.years)


def get_years_started_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1 = cast_str_to_datetime(date1, date1_format)
    date2 = cast_str_to_datetime(date2, date2_format)
    years_diff = date1.year - date2.year
    return abs(years_diff)


def cast_str_to_datetime(date: str, date_format: str) -> datetime:
    return datetime.strptime(date, date_format)
