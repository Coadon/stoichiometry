import re
from collections import defaultdict

from interf import Compound
from lookup import PT

RE_LETTER = re.compile(r"([A-Z][a-z]*)")
RE_NUMBER = re.compile(r"(\d+)")
RE_OPEN = re.compile(r"([(\[{])")
RE_CLOSE = re.compile(r"([)\]}])")
RE_SPACE = re.compile(r" |, |\+")


class ChemFormulaException(Exception):
    pass


def parse_formula(formula: str) -> dict:
    """Returns a dict showing the count of every present element. """
    counts: defaultdict = defaultdict(int)
    nests = []  # a stack

    i = 0  # char pointer

    while i < len(formula):
        # Handle element and its count
        if match := RE_LETTER.match(formula, i):
            element = match.group(1)  # stuff like "Na", "Cl"
            if not PT.get(element):
                raise ChemFormulaException(f"Unknown element--'{element}'")
            i += len(element)
            if number := RE_NUMBER.match(formula, i):
                count = int(number.group(1))
                i += len(number.group(1))
            else:
                count = 1
            counts[element] += count

        # Handle open parentheses
        elif RE_OPEN.match(formula, i):
            nests.append(counts.copy())
            counts.clear()
            i += 1

        # Handle close parentheses
        elif RE_CLOSE.match(formula, i):
            i += 1

            # Extract multiplier after closing parenthesis
            if number := RE_NUMBER.match(formula, i):
                paren_mult = int(number.group(1))
                i += len(number.group(1))
            else:
                paren_mult = 1

            # Combine with previous element counts
            try:
                (prev_counts) = nests.pop()
            except IndexError:
                raise ChemFormulaException("Over-closed parenthesis!")

            # Element and Count
            for el, cnt in counts.items():
                prev_counts[el] += cnt * paren_mult
            counts = prev_counts

        else:
            # i += 1  # Move forward if no match found
            raise ChemFormulaException(f"Not parsed––'{formula[i]}'")

    if len(nests) != 0:
        raise ChemFormulaException("Unclosed parenthesis!")

    return dict(counts)


def count_mix(mix: dict[Compound, int]) -> dict[str, int]:
    """ Calculate a mix of molecules """
    counts: defaultdict = defaultdict(int)

    for mole, mole_cnt in mix.items():
        for ele, ele_cnt in mole.cnt.items():
            counts[ele] += mole_cnt * ele_cnt

    return dict(counts)


def construct_mix(s: str) -> dict[Compound, int]:
    from src.custom import CompoundImpl

    parts: list[str] = RE_SPACE.split(s)
    full: defaultdict = defaultdict(int)

    parts = list(filter(None, parts))
    parts = list(filter(bool, parts))
    parts = list(filter(len, parts))
    parts = list(filter(lambda item: item, parts))

    for part in parts:
        count: int
        i: int = 0
        if number := RE_NUMBER.match(part, i):
            count = int(number.group(1))
            i += len(number.group(1))
        else:
            count = 1

        full[CompoundImpl(part[i:])] += count

    return dict(full)
