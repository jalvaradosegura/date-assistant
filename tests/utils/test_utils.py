from datetime import datetime

import pytest

from date_assistant import cast_str_to_datetime, get_days_diff
from date_assistant.formats import (
    YYYY_mm,
    YYYY_mm_dd,
    dd_mm_YYYY,
    mm_dd_YYYY,
    mm_YYYY,
)


@pytest.mark.parametrize(
    'date, date_format, expected_result',
    [
        ('2021-01-01', YYYY_mm_dd, datetime(2021, 1, 1)),
        ('14-02-2000', dd_mm_YYYY, datetime(2000, 2, 14)),
        ('10-08-2015', dd_mm_YYYY, datetime(2015, 8, 10)),
        ('12-1994', mm_YYYY, datetime(1994, 12, 1)),
        ('1994-12', YYYY_mm, datetime(1994, 12, 1)),
    ],
)
def test_cast_str_to_datetime(date, date_format, expected_result):
    response = cast_str_to_datetime(date, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01-01', '2021-01-11', YYYY_mm_dd, YYYY_mm_dd, 10),
        ('2021-01-01', '11-01-2021', YYYY_mm_dd, dd_mm_YYYY, 10),
        ('2020-01-01', '11-01-2021', YYYY_mm_dd, dd_mm_YYYY, 376),
        ('01-01-2021', '21-01-2021', mm_dd_YYYY, dd_mm_YYYY, 20),
        ('01-01-2021', '01-01-2022', mm_dd_YYYY, dd_mm_YYYY, 365),
    ],
)
def test_get_days_diff(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_days_diff(date1, date2, date1_format, date2_format)
    assert response == expected_result
