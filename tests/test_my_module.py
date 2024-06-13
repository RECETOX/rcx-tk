"""Tests for the rcx_tk.my_module module."""
import pytest
import datetime
from rcx_tk.my_module import hello, get_todays_date


@pytest.fixture
def today() -> str:
    return datetime.datetime.date(datetime.datetime.now()).strftime("%d.%m.%Y")

def test_get_todays_date(today):
    assert get_todays_date() == today

@pytest.mark.parametrize("text, expected", [
    ["World", "Hello World!"],
    ["nlesc", "Hello nlesc!"],
    ["Jane Smith", "Hello Jane Smith!"]
])
def test_hello_prints_date(text, expected, today):
    assert hello(text) ==  f'{today}: {expected}'


def test_hello_with_error():
    """Example of testing for raised errors."""
    with pytest.raises(ValueError) as excinfo:
        hello('nobody')
    assert 'Can not say hello to nobody' in str(excinfo.value)