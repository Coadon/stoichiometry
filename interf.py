"""

Computational Interfaces.

"""
from abc import ABCMeta, abstractmethod


class StoicException(Exception):
    pass


class Molecule(dict[str, int]):
    """ Molecule. Substance """

    @abstractmethod
    def __init__(self):
        super().__init__()

    @property
    def molar_mass(self) -> float:
        raise NotImplementedError

    @property
    def formula(self) -> str:
        raise NotImplementedError

    @property
    def counts(self) -> dict[str, int]:
        raise NotImplementedError


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
