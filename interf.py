"""

Computational Interfaces.

"""
import re
from abc import ABCMeta, abstractmethod
from typing import List, Any

RE_SPLIT = re.compile(" |, |\\+", )
RE_SPLIT_CAPS = re.compile("[A-Z][^A-Z]*")


class StoicException(Exception):
    pass


class Molecule(metaclass=ABCMeta):
    """ Molecule. Substance """
    _formula: list[str]

    @abstractmethod
    def __init__(self, formula: str):
        self._formula = RE_SPLIT_CAPS.findall(formula)
        pass

    @property
    def molar_mass(self) -> float:
        raise NotImplementedError

    @property
    def formula(self) -> str:
        raise NotImplementedError

    def __repr__(self):
        return self.formula


class StoicInterface(metaclass=ABCMeta):
    """ Stoic interface """
    impl_type: int = 0

    def cal_molar_mass(self, c: Molecule) -> float:
        raise NotImplementedError

    def cal_moles(self, c: Molecule, mass) -> float:
        raise NotImplementedError

    def cal_mass(self, c: Molecule, moles) -> float:
        raise NotImplementedError

    """ Returns None if impossible """

    def balance(self, r: set[Molecule], p: set[Molecule]) \
            -> tuple[set[Molecule], set[Molecule]]:
        raise NotImplementedError

    """ Percentage Yield """

    def cal_p_y(self) -> float:
        raise NotImplementedError

    """ Atom Economy """

    def cal_a_e(self) -> float:
        raise NotImplementedError
