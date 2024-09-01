"""

Computational Interfaces.

"""


class StoicException(Exception):
    pass


class Compound:
    """ Compound """

    def __init__(self, formula: str):
        self._formula = formula
        if self._formula == "":
            raise StoicException("Formula empty. Not accepted.")
        pass

    @property
    def molar_mass(self) -> float:
        return 0
        pass

    @property
    def formula(self) -> str:
        return self._formula
        pass


class StoicInterface:
    """ Stoic interface """

    def cal_molar_mass(self, c: Compound) -> float:
        pass

    def cal_moles(self, c: Compound, mass) -> float:
        pass

    def cal_mass(self, c: Compound, moles) -> float:
        pass

    """ Returns None if impossible """

    def balance(self, r: set[Compound], p: set[Compound]) \
            -> tuple[set[Compound], set[Compound]]:
        pass

    """ Percentage Yield """

    def cal_p_y(self) -> float:
        pass

    """ Atom Economy """

    def cal_a_e(self) -> float:
        pass
