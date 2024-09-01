"""

Stoic implemented with custom-written algorithms.
Experimental.

"""
from interf import StoicInterface
from lookup import PT
import re


def do_stuff():
    RE_CHAR_NUM = re.compile("([a-zA-Z]+)([0-9]+)")
    RE_SPLIT_CAPS = re.compile("[A-Z][^A-Z]*")
    RE_SPLIT_PLUS = re.compile(" |, |\\+", )

    # Molar Mass Calculator

    R = RE_SPLIT_PLUS.split(input("Reactants: "))

    R = (v.strip() for v in R)

    # Remove ''s
    R = filter(None, R)
    R = filter(bool, R)
    R = filter(len, R)
    R = filter(lambda v: v, R)
    R = list(R)

    R_mass: float = 0

    c: str
    e: str
    for ic, c in enumerate(R):
        # Iteration: Compounds

        es = RE_SPLIT_CAPS.findall(c)
        print(es)

        for ie, e in enumerate(es):
            # Iteration: Compound Numbers
            res = RE_CHAR_NUM.findall(e)
            print(res)

        for e in es:
            if e in PT:
                # n =
                R_mass += PT[e][1]
            else:
                print(f"'{e}' is not a valid element.")

    print(f"Relative Molecular Mass: {R_mass}")


class CustomStoicImpl(StoicInterface):
    # TODO Stoic
    pass
