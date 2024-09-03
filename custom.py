"""

Stoic implemented with custom-written algorithms.
Experimental.

"""
from interf import StoicInterface, Molecule, StoicException
from lookup import PT
import re


class MoleculeCustomImpl(Molecule):
    def __init__(self, formula: str):
        super().__init__(formula)
        if not self.formula:
            raise StoicException("Formula empty. Not accepted.")

    @property
    def formula(self) -> str:
        return "".join(self._formula)


class StoicCustomImpl(StoicInterface):
    # TODO Stoic
    pass
