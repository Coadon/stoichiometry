"""

Stoic implemented with custom-written algorithms.
Experimental.

"""
from parse import parse_formula, ChemFormulaException, count_mix
from interf import StoicInterface, Molecule, StoicException, Mixture
from src.lookup import PT

stoic: StoicInterface


class MoleculeImpl(Molecule):
    _molar_mass: float = None
    _formula: str = None
    _counts: dict[str, int] = None

    def __init__(self, formula: str):
        super().__init__()
        if not formula:
            raise StoicException("Formula empty. Not accepted.")

        self._counts = parse_formula(formula)
        self._formula = formula

    @property
    def formula(self) -> str:
        if not self._formula:
            pass
        return self._formula

    @property
    def counts(self) -> dict:
        return self._counts

    @property
    def molar_mass(self):
        if not self._molar_mass:
            self._molar_mass = stoic.cal_molar_mass(c=self)
        return self._molar_mass

    def to_mass(self, moles: float) -> float:
        return stoic.cal_mass(self, moles)

    def to_moles(self, mass: float) -> float:
        return stoic.cal_moles(self, mass)

    """ Make Hashable """

    def __str__(self):
        return str(self.counts)

    def __hash__(self):
        return hash(self._formula)


class MixtureImpl(Mixture):
    _counts: dict[str, int]

    def __init__(self, s: str):
        from src.parse import construct_mix

        super().__init__()
        self.values = construct_mix(s)
        self._counts = count_mix(self.values)

    @property
    def counts(self) -> dict[str, int]:
        return self._counts

    @property
    def raw(self) -> dict[Molecule, int]:
        return self.values


class StoicImpl(StoicInterface):
    # TODO Stoic

    def impl_type(self):
        return 0

    def cal_molar_mass(self, c: Molecule) -> float:
        total: float = 0

        for ele, cnt in c.counts.items():
            total += PT.get(ele).MOLAR_MASS * cnt

        return total

    def cal_moles(self, c: Molecule, mass: float) -> float:
        return mass / c.molar_mass

    def cal_mass(self, c: Molecule, moles: float) -> float:
        return moles * c.molar_mass

    def balance(self, reactants: Mixture, p: Mixture) -> tuple[Mixture, Mixture]:
        """ Returns None if impossible """
        raise NotImplementedError

    def cal_p_y(self) -> float:
        """ Percentage Yield """
        raise NotImplementedError

    def cal_a_e(self) -> float:
        """ Atom Economy """
        raise NotImplementedError


stoic = StoicImpl()
