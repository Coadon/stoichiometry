from custom import CustomStoicImpl
from interf import Compound, StoicInterface
from util import ANSI
import sys

VERSION = "v1.0"
print(f"Stoichiometry {VERSION} | MIT")

stoic: StoicInterface

intf = input("""
Choose your calculator. Choices---
    a. Custom-Written
    b. Chempy (recommended for accuracy but requires: chempy)
Please specify: [ """).lower().strip()

print("Selected interface--", end="")

# Python2 doesn't have switch statements :(
if intf == "a":
    stoic = CustomStoicImpl()
    print("CUSTOM WRITTEN")
elif intf == "b":
    # TODO Test for package
    stoic = None
    print("CHEMPY")
else:
    print(ANSI.RED + f"Unidentified '{intf}'")
    sys.exit(-1)

try:
    c = Compound("")
    print(c.formula)
except Exception as e:
    print(ANSI.RED + e.args[0])

