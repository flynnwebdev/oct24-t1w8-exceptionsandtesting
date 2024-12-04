import pytest
from src.errors import convert_to_integer

def test_string():
    assert convert_to_integer('123') == 123

def test_float():
    # should raise a ValueError
    with pytest.raises(ValueError):
        convert_to_integer('123.45')

def test_word():
    with pytest.raises(ValueError):
        convert_to_integer('Hello')
        