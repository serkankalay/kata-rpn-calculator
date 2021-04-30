import pytest

from rpn_calculator import (Divide, Multiply, Subtract, Sum, parse_expression,
                            parse_number, parse_operator)


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


def test_simple_expression():
    exp = parse_expression("20 5 /")
    assert exp[0] == 20
    assert exp[1] == 5
    assert isinstance(exp[2], Divide)


def test_double_expression():
    exp = parse_expression("4 2 + 3 -")
    assert exp[0] == 4
    assert exp[1] == 2
    assert isinstance(exp[2], Sum)
    assert exp[3] == 3
    assert isinstance(exp[4], Subtract)


def test_triple_expression():
    exp = parse_expression("3 5 8 * 7 + *")
    assert exp[0] == 3
    assert exp[1] == 5
    assert exp[2] == 8
    assert isinstance(exp[3], Multiply)
    assert exp[4] == 7
    assert isinstance(exp[5], Sum)
    assert isinstance(exp[6], Multiply)
