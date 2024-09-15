"""

Stoic implemented with custom-written algorithms.
Experimental.

"""
from formula_parse import parse_formula, ChemFormulaException
from interf import StoicInterface, Molecule, StoicException
from lookup import PT
import re


class MoleculeCustomImpl(Molecule):
    _formula: str = None

    def __init__(self, formula: str):
        super().__init__()
        if not formula:
            raise StoicException("Formula empty. Not accepted.")

        self.values = parse_formula(formula)
        self._formula = formula

    @property
    def formula(self) -> str:
        if not self._formula:
            pass
        return ""

    @property
    def counts(self) -> dict:
        return self.values


class StoicCustomImpl(StoicInterface):
    # TODO Stoic
    pass
