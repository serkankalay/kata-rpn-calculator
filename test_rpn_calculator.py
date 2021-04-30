import pytest

from rpn_calculator import Divide, parse_number, parse_operator, Subtract, Sum, Multiply


def test_parse_number():
    assert parse_number("5") == 5
    with pytest.raises(ValueError):
        parse_number("A")


def test_operator():
    assert isinstance(parse_operator("/"), Divide)
    assert isinstance(parse_operator("+"), Sum)
    assert isinstance(parse_operator("-"), Subtract)
    assert isinstance(parse_operator("*"), Multiply)
    with pytest.raises(ArithmeticError):
        parse_operator("5")
