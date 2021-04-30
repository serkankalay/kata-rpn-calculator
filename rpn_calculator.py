from abc import ABC
from typing import Sequence, Union

Expression = Sequence[Union[float, "Operator"]]


def parse_number(s: str) -> float:
    return float(s)


class Operator(ABC):
    pass


class Divide(Operator):
    pass


class Sum(Operator):
    pass


class Subtract(Operator):
    pass


class Multiply(Operator):
    pass


def parse_operator(s: str) -> Operator:
    if s == "/":
        return Divide()
    elif s == "+":
        return Sum()
    elif s == "-":
        return Subtract()
    elif s == "*":
        return Multiply()
    else:
        raise ArithmeticError()


def _parse_item(s: str) -> Union[float, Operator]:
    try:
        return parse_number(s)
    except ValueError:
        return parse_operator(s)
    except ArithmeticError:
        print("Unknown data")


def parse_expression(s: str) -> Expression:
    return [_parse_item(s) for s in s.split()]
