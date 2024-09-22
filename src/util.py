import math
from functools import reduce

from src.interf import Compound, Mixture, StoicInterface


def molecule(formula: str) -> Compound:
    from src.custom import CompoundImpl
    return CompoundImpl(formula)


def mixture(formula: str) -> Mixture:
    from src.custom import MixtureImpl
    return MixtureImpl(formula)


@property
def stoic() -> StoicInterface:
    from src.custom import stoic
    return stoic


def gcd(numbers: list) -> int:
    if len(numbers) > 2:
        return reduce(lambda x, y: gcd([x, y]), numbers)
    else:
        return math.gcd(numbers[0], numbers[1])


class ANSI:
    CYAN = "\033[96m"
    PINK = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
