import math
from abc import ABC
from typing import Sequence, Union

Expression = Sequence[Union[float, "Operator"]]


def parse_number(s: str) -> float:
    return float(s)


class Operator(ABC):
    def apply(self, *args) -> float:
        raise NotImplementedError()


class DoubleOperator(Operator):
    def apply(self, n1: float, n2: float) -> float:
        raise NotImplementedError()


class Divide(DoubleOperator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 / n2


class Sum(DoubleOperator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 + n2


class Subtract(DoubleOperator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 - n2


class Multiply(DoubleOperator):
    def apply(self, n1: float, n2: float) -> float:
        return n1 * n2


class SingleOperator(Operator):
    def apply(self, n1: float) -> float:
        raise NotImplementedError


class SquareRoot(SingleOperator):
    def apply(self, n1: float) -> float:
        return math.sqrt(n1)


class MultiOperator(Operator):
    def apply(self, *args) -> float:
        raise NotImplementedError()


class Max(MultiOperator):
    def apply(self, *args) -> float:
        return max(*args)


def parse_operator(s: str) -> Operator:
    if s == "/":
        return Divide()
    elif s == "+":
        return Sum()
    elif s == "-":
        return Subtract()
    elif s == "*":
        return Multiply()
    elif s == "SQRT":
        return SquareRoot()
    elif s == "MAX":
        return Max()
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


def calculate(exp: Expression) -> Union[float, Expression]:
    last_operator = exp[-1]
    if not isinstance(last_operator, Operator):
        if len(exp) == 1:
            return exp[0]
        else:
            return exp

    if isinstance(last_operator, SingleOperator):
        return last_operator.apply(calculate(exp[:-1]))

    if isinstance(last_operator, MultiOperator):
        current = -2
        args = []
        while len(exp) + current >= 0 and not isinstance(
            exp[current], Operator
        ):
            args.append(exp[current])
            current -= 1
        return calculate(list(exp[:current]) + [last_operator.apply(args)])

    operator_predecessor = exp[-2]
    if isinstance(operator_predecessor, float):
        return last_operator.apply(calculate(exp[:-2]), operator_predecessor)
    elif isinstance(exp[0], float):
        return last_operator.apply(calculate(exp[1:-1]), exp[0])

    raise ArithmeticError()
