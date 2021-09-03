import pytest


@pytest.mark.parametrize(
    "num_days, expected_result",
    [
        (-1, "2020-12-31"),
        (31, "2021-02-01"),
        (365, "2022-01-01"),
        (-366, "2020-01-01"),
        (0, "2021-01-01"),
    ],
)
def test_add_days(example_date, num_days, expected_result):
    response = example_date.add_days(num_days)
    assert response == expected_result


@pytest.mark.parametrize(
    "num_days, expected_result, date_format",
    [
        (-1, "31-12-2020", "%d-%m-%Y"),
        (31, "01/02/2021", "%d/%m/%Y"),
        (365, "01-01-2022", "%m-%d-%Y"),
        (-366, "01/01/2020", "%m/%d/%Y"),
        (1, "01-02-2021", "%m-%d-%Y"),
    ],
)
def test_add_days_using_non_default_date_format(
    example_date, num_days, expected_result, date_format
):
    response = example_date.add_days(num_days, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result",
    [
        ("2020-12-31", 1),
        ("2021-02-01", 31),
        ("2022-01-01", 365),
        ("2020-01-01", 366),
        ("2021-01-01", 0),
    ],
)
def test_days_diff_with(example_date, date_to_compare, expected_result):
    response = example_date.days_diff_with(date_to_compare)
    assert response == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result, date_format",
    [
        ("31-12-2020", 1, "%d-%m-%Y"),
        ("02-01-2021", 31, "%m-%d-%Y"),
        ("01-01-2022", 365, "%m-%d-%Y"),
        ("01-01-2020", 366, "%d-%m-%Y"),
        ("01/01/2021", 0, "%d/%m/%Y"),
    ],
)
def test_days_diff_with_using_non_default_date_format(
    example_date, date_to_compare, expected_result, date_format
):
    response = example_date.days_diff_with(date_to_compare, date_format)
    assert response == expected_result
