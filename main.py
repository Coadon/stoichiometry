from custom import StoicCustomImpl, MoleculeCustomImpl
from formula_parse import ChemFormulaException
from interf import Molecule, StoicInterface
from util import ANSI
import sys

VERSION = "v1.0"
print(f"Stoichiometry {VERSION} | MIT")

stoic: StoicInterface = StoicCustomImpl()


def molecule(formula: str):
    return MoleculeCustomImpl(formula) if stoic.impl_type == 0 else MoleculeCustomImpl(formula)


try:
    c = molecule("NaCl((Na))kkk")
    print(c)
except ChemFormulaException as e:
    print(ANSI.RED + "Error parsing: " + e.args[0])
except Exception as e:
    print(ANSI.RED + e.args[0])
