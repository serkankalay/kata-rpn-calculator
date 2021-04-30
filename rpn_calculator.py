from abc import ABC


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
