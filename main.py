from custom import CustomStoicImpl
from interf import Molecule, StoicInterface
from util import ANSI
import sys

VERSION = "v1.0"
print(f"Stoichiometry {VERSION} | MIT")

stoic: StoicInterface


def molecule(formula: str):
    return Molecule(formula) if stoic.if_type == 0 else Molecule(formula)


INT_F = input("""
Choose your calculator. Choices---
    a. Custom-Written
    b. Chem-py (recommended for accuracy but requires: chem-py)
Please specify: [ """).lower().strip()

print("Selected interface--", end="")

# Python2 doesn't have switch statements :(
if INT_F == "a":
    stoic = CustomStoicImpl()
    print("CUSTOM WRITTEN")
elif INT_F == "b":
    # TODO Test for package
    stoic = None
    print("CHEMPY")
else:
    print(ANSI.RED + f"Unidentified '{INT_F}'")
    sys.exit(-1)

try:
    c = molecule("NaCl")
    print(c.formula)
except Exception as e:
    print(ANSI.RED + e.args[0])
