from datetime import datetime


def get_days_diff(
    date1: str,
    date2: str,
    date_format1: str = '%Y-%m-%d',
    date_format2: str = '%Y-%m-%d',
):
    date1 = cast_str_to_datetime(date1, date_format1)
    date2 = cast_str_to_datetime(date2, date_format2)
    return abs(date1 - date2).days


def cast_str_to_datetime(date: str, date_format: str) -> datetime:
    return datetime.strptime(date, date_format)
