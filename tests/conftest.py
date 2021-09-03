import pytest

from date_assistant import DateAssistant


@pytest.fixture
def example_date():
    return DateAssistant(date="2021-01-01")
