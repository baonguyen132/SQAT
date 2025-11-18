import pytest

def test_mod_2(input_value):
    assert input_value % 2 == 0, "input_value is not divisible by 2"

def test_mod_3(input_value):
    assert input_value % 3 == 0, "input_value is not divisible by 3"
