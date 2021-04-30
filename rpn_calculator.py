from abc import ABC
from typing import Sequence, Union

Expression = Sequence[Union[float, "Operator"]]


def parse_number(s: str) -> float:
    return float(s)


class Operator(ABC):
    def apply(self, n1: float, n2: float) -> float:
        raise NotImplementedError()


class Divide(Operator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 / n2


class Sum(Operator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 + n2


class Subtract(Operator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 - n2


class Multiply(Operator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 * n2


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


def calculate(exp: Expression) -> float:
    last_operator = exp[-1]
    if not isinstance(last_operator, Operator):
        if len(exp) == 1:
            return exp[0]
        else:
            raise ValueError()

    operator_predecessor = exp[-2]
    if isinstance(operator_predecessor, float):
        return last_operator.apply(calculate(exp[:-2]), operator_predecessor)

    raise ArithmeticError()
