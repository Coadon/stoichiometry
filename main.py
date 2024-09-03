from custom import StoicCustomImpl, MoleculeCustomImpl
from interf import Molecule, StoicInterface
from util import ANSI
import sys

VERSION = "v1.0"
print(f"Stoichiometry {VERSION} | MIT")

stoic: StoicInterface = StoicCustomImpl()


def molecule(formula: str):
    return MoleculeCustomImpl(formula) if stoic.impl_type == 0 else MoleculeCustomImpl(formula)


try:
    c = molecule("NaCl")
    print(c)
except Exception as e:
    print(ANSI.RED + e.args[0])
