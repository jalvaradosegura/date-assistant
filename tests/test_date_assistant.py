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
