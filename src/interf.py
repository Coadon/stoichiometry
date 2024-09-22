"""

Computational Interfaces.

"""
from abc import ABCMeta, abstractmethod


class StoicException(Exception):
    pass


class Compound(metaclass=ABCMeta):
    # NOTE Do not inherit Molecule from dict[str, int].
    """
    Interface: Molecule. Substance
    Uses
    """

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
    def cnt(self) -> dict[str, int]:
        """ Element counts """
        raise NotImplementedError

    def to_mass(self, moles: float) -> float:
        raise NotImplementedError

    def to_moles(self, mass: float) -> float:
        raise NotImplementedError

    def __expr__(self):
        return self.cnt

    # TODO Iteration
    def __iter__(self):
        pass

    def __next__(self):
        pass


class Mixture(metaclass=ABCMeta):
    """ Interface: A Mixture"""

    @abstractmethod
    def __init__(self):
        super().__init__()

    @property
    def cnt(self) -> dict[Compound, int]:
        """ Compound counts """
        raise NotImplementedError

    @property
    def element_cnt(self) -> dict[str, int]:
        """ Total element counts """
        raise NotImplementedError


class StoicInterface(metaclass=ABCMeta):
    """ Stoic interface """

    @property
    def impl_type(self):
        raise NotImplementedError

    def cal_molar_mass(self, c: Compound) -> float:
        raise NotImplementedError

    def cal_moles(self, c: Compound, mass) -> float:
        raise NotImplementedError

    def cal_mass(self, c: Compound, moles) -> float:
        raise NotImplementedError

    def is_balanced(self, r: Mixture, p: Mixture) -> bool:
        """ Returns if balanced. """
        raise NotImplementedError

    def can_balance(self, r: Mixture, p: Mixture) -> bool:
        """ Returns two bools. """
        raise NotImplementedError

    def balance(self, r: Mixture, p: Mixture) -> bool:
        """ Returns failure """
        raise NotImplementedError

    def cal_p_y(self) -> float:
        """ Percentage Yield """
        raise NotImplementedError

    def cal_a_e(self) -> float:
        """ Atom Economy """
        raise NotImplementedError
