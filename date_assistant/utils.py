from datetime import datetime

from dateutil.relativedelta import relativedelta  # type: ignore

from date_assistant.date_formats import YYYY_MM_DD


def get_days_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1_as_datetime = cast_str_to_datetime(date1, date1_format)
    date2_as_datetime = cast_str_to_datetime(date2, date2_format)
    return abs(date1_as_datetime - date2_as_datetime).days


def get_months_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1_as_datetime = cast_str_to_datetime(date1, date1_format)
    date2_as_datetime = cast_str_to_datetime(date2, date2_format)
    diff = relativedelta(date1_as_datetime, date2_as_datetime)
    return abs(diff.months + (12 * diff.years))


def get_months_started_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1_as_datetime = cast_str_to_datetime(date1, date1_format)
    date2_as_datetime = cast_str_to_datetime(date2, date2_format)
    months_diff = date1_as_datetime.month - date2_as_datetime.month
    return abs((date1_as_datetime.year - date2_as_datetime.year) * 12 + months_diff)


def get_years_diff_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1_as_datetime = cast_str_to_datetime(date1, date1_format)
    date2_as_datetime = cast_str_to_datetime(date2, date2_format)
    diff = relativedelta(date1_as_datetime, date2_as_datetime)
    return abs(diff.years)


def get_years_started_between(
    date1: str,
    date2: str,
    date1_format: str = YYYY_MM_DD,
    date2_format: str = YYYY_MM_DD,
) -> int:
    date1_as_datetime = cast_str_to_datetime(date1, date1_format)
    date2_as_datetime = cast_str_to_datetime(date2, date2_format)
    years_diff = date1_as_datetime.year - date2_as_datetime.year
    return abs(years_diff)


def cast_str_to_datetime(date: str, date_format: str) -> datetime:
    return datetime.strptime(date, date_format)


def cast_datetime_to_str(date: datetime, output_format: str) -> str:
    return date.strftime(output_format)
