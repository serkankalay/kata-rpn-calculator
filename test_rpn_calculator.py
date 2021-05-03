import pytest

from rpn_calculator import (Divide, Max, Multiply, SquareRoot, Subtract, Sum,
                            calculate, parse_expression, parse_number,
                            parse_operator)


def test_parse_number():
    assert parse_number("5") == 5
    with pytest.raises(ValueError):
        parse_number("A")


def test_operator():
    assert isinstance(parse_operator("/"), Divide)
    assert isinstance(parse_operator("+"), Sum)
    assert isinstance(parse_operator("-"), Subtract)
    assert isinstance(parse_operator("*"), Multiply)
    assert isinstance(parse_operator("SQRT"), SquareRoot)
    assert isinstance(parse_operator("MAX"), Max)
    with pytest.raises(ArithmeticError):
        parse_operator("5")


def test_simple_expression():
    exp = parse_expression("20 5 /")
    assert exp[0] == 20
    assert exp[1] == 5
    assert isinstance(exp[2], Divide)


def test_calculate_simple_expression():
    assert calculate(parse_expression("20 5 /")) == 4


def test_double_expression():
    exp = parse_expression("4 2 + 3 -")
    assert exp[0] == 4
    assert exp[1] == 2
    assert isinstance(exp[2], Sum)
    assert exp[3] == 3
    assert isinstance(exp[4], Subtract)


def test_calculate_double_expression():
    assert calculate(parse_expression("4 2 + 3 -")) == 3


def test_triple_expression():
    exp = parse_expression("3 5 8 * 7 + *")
    assert exp[0] == 3
    assert exp[1] == 5
    assert exp[2] == 8
    assert isinstance(exp[3], Multiply)
    assert exp[4] == 7
    assert isinstance(exp[5], Sum)
    assert isinstance(exp[6], Multiply)


def test_calculate_triple_expression():
    assert calculate(parse_expression("3 5 8 * 7 + *")) == 141


def test_simple_square_root():
    assert calculate(parse_expression("9 SQRT")) == 3


def test_double_expression_with_square_root():
    assert calculate(parse_expression("9 SQRT 5 *")) == 15


def test_triple_expression_with_square_root():
    assert calculate(parse_expression("20 9 SQRT 5 * +")) == 35


def test_simple_max_expression():
    assert calculate(parse_expression("5 3 4 2 9 1 MAX")) == 9


# def test_double_max_expression():
#     assert calculate(parse_expression("4 5 MAX 1 2 MAX *")) == 10
