from date_assistant import __version__


def test_version():
    assert __version__ == '0.9.1'


def test_repr(example_date):
    assert repr(example_date) == "DateAssistant('2021-01-01')"


def test_str(example_date):
    assert str(example_date) == '2021-01-01'
