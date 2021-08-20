import pytest


@pytest.mark.parametrize(
    'years_to_add, expected_result',
    [
        (0, '2021-01-01'),
        (1, '2022-01-01'),
        (-2, '2019-01-01'),
        (12, '2033-01-01'),
        (-12, '2009-01-01'),
    ],
)
def test_add_years(example_date, years_to_add, expected_result):
    response = example_date.add_years(years_to_add)
    assert response == expected_result


@pytest.mark.parametrize(
    'years_to_add, expected_result, date_format',
    [
        (0, '2021-01', '%Y-%m'),
        (1, '2022', '%Y'),
        (-2, '01-2019', '%m-%Y'),
        (12, '2033/01/01', '%Y/%m/%d'),
        (-12, '2009-01-01', '%Y-%d-%m'),
    ],
)
def test_add_years_until_using_non_default_date_format(
    example_date, years_to_add, expected_result, date_format
):
    response = example_date.add_years(years_to_add, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date_to_compare, expected_result',
    [
        ('2021-12-31', 0),
        ('2020-12-01', 0),
        ('2021-11-11', 0),
        ('2020-01-01', 1),
        ('2022-04-20', 1),
    ],
)
def test_years_diff_with(example_date, date_to_compare, expected_result):
    response = example_date.years_diff_with(date_to_compare)
    assert response == expected_result


@pytest.mark.parametrize(
    'date_to_compare, expected_result, date_format',
    [
        ('2021', 0, '%Y'),
        ('2020/12/01', 0, '%Y/%m/%d'),
        ('2100', 79, '%Y'),
        ('20200101', 1, '%Y%m%d'),
        ('2022', 1, '%Y'),
    ],
)
def test_years_diff_with_using_non_default_date_format(
    example_date, date_to_compare, expected_result, date_format
):
    response = example_date.years_diff_with(date_to_compare, date_format)
    assert response == expected_result


@pytest.mark.parametrize(
    'date_to_compare, expected_result',
    [
        ('2020-11-01', 1),
        ('2020-12-11', 1),
        ('2016-11-11', 5),
        ('2021-12-31', 0),
        ('2021-04-20', 0),
    ],
)
def test_years_started_since(example_date, date_to_compare, expected_result):
    response_since = example_date.years_started_since(date_to_compare)
    response_until = example_date.years_started_until(date_to_compare)

    assert response_since == expected_result
    assert response_until == expected_result


@pytest.mark.parametrize(
    'date_to_compare, expected_result, date_format',
    [
        ('2021', 0, '%Y'),
        ('2020/12/01', 1, '%Y/%m/%d'),
        ('2100', 79, '%Y'),
        ('2020-01-01', 1, '%Y-%m-%d'),
        ('2022', 1, '%Y'),
    ],
)
def test_years_started_since_using_non_default_date_format(
    example_date, date_to_compare, expected_result, date_format
):
    response_since = example_date.years_started_since(
        date_to_compare, date_format
    )
    response_until = example_date.years_started_until(
        date_to_compare, date_format
    )

    assert response_since == expected_result
    assert response_until == expected_result
