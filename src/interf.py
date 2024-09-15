"""

Computational Interfaces.

"""
from abc import ABCMeta, abstractmethod



class StoicException(Exception):
    pass


class Molecule(metaclass=ABCMeta):
    # NOTE Do not inherit Molecule from dict[str, int].
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

    def to_mass(self, moles: float) -> float:
        raise NotImplementedError

    def to_moles(self, mass: float) -> float:
        raise NotImplementedError

    def __expr__(self):
        return self.counts

    # TODO Iteration
    def __iter__(self):
        pass

    def __next__(self):
        pass


class Mixture(dict[Molecule, int]):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @property
    def counts(self) -> dict[str, int]:
        raise NotImplementedError

    @property
    def raw(self) -> dict[Molecule, int]:
        raise NotImplementedError


class StoicInterface(metaclass=ABCMeta):
    """ Stoic interface """

    @property
    def impl_type(self):
        raise NotImplementedError

    def cal_molar_mass(self, c: Molecule) -> float:
        raise NotImplementedError

    def cal_moles(self, c: Molecule, mass) -> float:
        raise NotImplementedError

    def cal_mass(self, c: Molecule, moles) -> float:
        raise NotImplementedError

    def balance(self, reactants: Mixture, p: Mixture) -> tuple[Mixture, Mixture]:
        """ Returns None if impossible """
        raise NotImplementedError

    def cal_p_y(self) -> float:
        """ Percentage Yield """
        raise NotImplementedError

    def cal_a_e(self) -> float:
        """ Atom Economy """
        raise NotImplementedError
