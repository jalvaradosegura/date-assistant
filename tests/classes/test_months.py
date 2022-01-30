import pytest


@pytest.mark.parametrize(
    "months_to_add, expected_result",
    [
        (0, "2021-01-01"),
        (1, "2021-02-01"),
        (-1, "2020-12-01"),
        (12, "2022-01-01"),
        (-12, "2020-01-01"),
    ],
)
def test_add_months(example_date, months_to_add, expected_result):
    response = example_date.add_months(months_to_add)
    assert response == expected_result


@pytest.mark.parametrize(
    "months_to_add, expected_result, date_format",
    [
        (0, "2021/01/01", "%Y/%m/%d"),
        (1, "01-02-2021", "%d-%m-%Y"),
        (-1, "2020/01/12", "%Y/%d/%m"),
        (12, "2022_01:01", "%Y_%m:%d"),
        (-12, "2020-01-01", "%Y-%m-%d"),
    ],
)
def test_add_months_using_non_default_date_format(
    example_date, months_to_add, expected_result, date_format
):
    response = example_date.add_months(months_to_add, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result",
    [
        ("2020-12-31", 0),
        ("2020-12-11", 0),
        ("2021-11-11", 10),
        ("2020-12-01", 1),
        ("2021-04-20", 3),
    ],
)
def test_months_diff_with(example_date, date_to_compare, expected_result):
    response = example_date.months_diff_with(date_to_compare)
    assert response == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result, date_format",
    [
        ("2021/01/01", 0, "%Y/%m/%d"),
        ("01-02-2021", 1, "%d-%m-%Y"),
        ("2020/01/12", 1, "%Y/%d/%m"),
        ("2022_01:01", 12, "%Y_%m:%d"),
        ("2020-01-01", 12, "%Y-%m-%d"),
    ],
)
def test_months_diff_with_using_non_default_date_format(
    example_date, date_to_compare, expected_result, date_format
):
    response = example_date.months_diff_with(date_to_compare, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result",
    [
        ("2020-12-31", 1),
        ("2020-12-11", 1),
        ("2021-11-11", 10),
        ("2020-12-01", 1),
        ("2021-04-20", 3),
    ],
)
def test_months_started_since_and_until(example_date, date_to_compare, expected_result):
    response_since = example_date.months_started_since(date_to_compare)
    response_until = example_date.months_started_until(date_to_compare)

    assert response_since == expected_result
    assert response_until == expected_result


@pytest.mark.parametrize(
    "date_to_compare, expected_result, date_format",
    [
        ("2021/01/01", 0, "%Y/%m/%d"),
        ("01-02-2021", 1, "%d-%m-%Y"),
        ("2020/01/12", 1, "%Y/%d/%m"),
        ("2022_01:01", 12, "%Y_%m:%d"),
        ("2020-01-01", 12, "%Y-%m-%d"),
    ],
)
def test_months_started_since_and_until_using_non_default_date_format(
    example_date, date_to_compare, expected_result, date_format
):
    response_since = example_date.months_started_since(date_to_compare, date_format)
    response_until = example_date.months_started_until(date_to_compare, date_format)

    assert response_since == expected_result
    assert response_until == expected_result
