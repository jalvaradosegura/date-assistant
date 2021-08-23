from datetime import datetime

import pytest

from date_assistant import (
    cast_str_to_datetime,
    get_days_diff_between,
    get_months_diff_between,
    get_months_started_between,
    get_years_diff_between,
    get_years_started_between,
)
from date_assistant.formats import (
    DD_MM_YYYY,
    MM_DD_YYYY,
    MM_YYYY,
    YYYY_MM,
    YYYY_MM_DD,
)


@pytest.mark.parametrize(
    'date, date_format, expected_result',
    [
        ('2021-01-01', YYYY_MM_DD, datetime(2021, 1, 1)),
        ('14-02-2000', DD_MM_YYYY, datetime(2000, 2, 14)),
        ('10-08-2015', DD_MM_YYYY, datetime(2015, 8, 10)),
        ('12-1994', MM_YYYY, datetime(1994, 12, 1)),
        ('1994-12', YYYY_MM, datetime(1994, 12, 1)),
    ],
)
def test_cast_str_to_datetime(date, date_format, expected_result):
    response = cast_str_to_datetime(date, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01-01', '2021-01-11', YYYY_MM_DD, YYYY_MM_DD, 10),
        ('2021-01-01', '11-01-2021', YYYY_MM_DD, DD_MM_YYYY, 10),
        ('2020-01-01', '11-01-2021', YYYY_MM_DD, DD_MM_YYYY, 376),
        ('01-01-2021', '21-01-2021', MM_DD_YYYY, DD_MM_YYYY, 20),
        ('01-01-2021', '01-01-2022', MM_DD_YYYY, DD_MM_YYYY, 365),
    ],
)
def test_get_days_diff_between(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_days_diff_between(date1, date2, date1_format, date2_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01-05', '2021-03-01', YYYY_MM_DD, YYYY_MM_DD, 1),
        ('2021-01-01', '02-01-2020', YYYY_MM_DD, DD_MM_YYYY, 11),
        ('2020-01-01', '01-01-2020', YYYY_MM_DD, DD_MM_YYYY, 0),
        ('01-01-2021', '21-01-2023', MM_DD_YYYY, DD_MM_YYYY, 24),
        ('01-2021', '01-2022', MM_YYYY, MM_YYYY, 12),
    ],
)
def test_get_months_diff_between(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_months_diff_between(
        date1, date2, date1_format, date2_format
    )
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01-05', '2021-03-01', YYYY_MM_DD, YYYY_MM_DD, 2),
        ('2021-01-01', '02-01-2020', YYYY_MM_DD, DD_MM_YYYY, 12),
        ('2020-01-01', '01-01-2020', YYYY_MM_DD, DD_MM_YYYY, 0),
        ('01-01-2021', '21-01-2023', MM_DD_YYYY, DD_MM_YYYY, 24),
        ('01-2021', '01-2022', MM_YYYY, MM_YYYY, 12),
    ],
)
def test_get_months_started_between(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_months_started_between(
        date1, date2, date1_format, date2_format
    )
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01', '2022-01', YYYY_MM, YYYY_MM, 1),
        ('2021-01-01', '02-01-2020', YYYY_MM_DD, DD_MM_YYYY, 0),
        ('2021-01-01', '01-01-2020', YYYY_MM_DD, DD_MM_YYYY, 1),
        ('01-01-2021', '21-01-2023', MM_DD_YYYY, DD_MM_YYYY, 2),
        ('2021-01-01', '31-12-2020', YYYY_MM_DD, DD_MM_YYYY, 0),
    ],
)
def test_get_years_diff_between(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_years_diff_between(date1, date2, date1_format, date2_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date1, date2, date1_format, date2_format, expected_result',
    [
        ('2021-01', '2022-01', YYYY_MM, YYYY_MM, 1),
        ('2021-01-01', '31-12-2020', YYYY_MM_DD, DD_MM_YYYY, 1),
        ('2021-01-01', '01-01-2020', YYYY_MM_DD, DD_MM_YYYY, 1),
        ('12-31-2021', '01-01-2023', MM_DD_YYYY, DD_MM_YYYY, 2),
        ('01-01-2021', '01-01-2022', MM_DD_YYYY, DD_MM_YYYY, 1),
    ],
)
def test_get_years_started_between(
    date1, date2, date1_format, date2_format, expected_result
):
    response = get_years_started_between(
        date1, date2, date1_format, date2_format
    )
    assert response == expected_result
