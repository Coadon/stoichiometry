"""

Computational Interfaces.

"""

class StoicException(Exception):
    pass


class Molecule:
    """ Molecule. Substance """

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
    if_type: int = 0

    def cal_molar_mass(self, c: Molecule) -> float:
        pass

    def cal_moles(self, c: Molecule, mass) -> float:
        pass

    def cal_mass(self, c: Molecule, moles) -> float:
        pass

    """ Returns None if impossible """

    def balance(self, r: set[Molecule], p: set[Molecule]) \
            -> tuple[set[Molecule], set[Molecule]]:
        pass

    """ Percentage Yield """

    def cal_p_y(self) -> float:
        pass

    """ Atom Economy """

    def cal_a_e(self) -> float:
        pass
