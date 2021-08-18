import pytest

from date_assistant import __version__, DateAssistant


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def example_date():
    return DateAssistant(date='2021-01-01')


def test_date_assistant_repr(example_date):
    assert repr(example_date) == "DateAssistant('2021-01-01')"


def test_date_assistant_str(example_date):
    assert str(example_date) == '2021-01-01'


@pytest.mark.parametrize(
    'num_days, expected_result',
    [
        (-1, '2020-12-31'),
        (31, '2021-02-01'),
        (365, '2022-01-01'),
        (-366, '2020-01-01'),
        (0, '2021-01-01'),
    ],
)
def test_date_assistant_add_days(example_date, num_days, expected_result):
    response = example_date.add_days(num_days)
    assert response == expected_result


@pytest.mark.parametrize(
    'date_to_compare, expected_result',
    [
        ('2020-12-31', 1),
        ('2021-02-01', 31),
        ('2022-01-01', 365),
        ('2020-01-01', 366),
        ('2021-01-01', 0),
    ],
)
def test_date_assistant_days_diff_with(
    example_date, date_to_compare, expected_result
):
    response = example_date.days_diff_with(date_to_compare)
    assert response == expected_result
