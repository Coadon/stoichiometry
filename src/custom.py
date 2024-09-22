"""

Stoic implemented with custom-written algorithms.
Experimental.

"""
import math

from interf import StoicInterface, Compound, StoicException, Mixture
from parse import parse_formula, count_mix
from src import util
from src.lookup import PT

stoic: StoicInterface


class CompoundImpl(Compound):
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
    def cnt(self) -> dict:
        return self._counts

    @property
    def molar_mass(self):
        return stoic.cal_molar_mass(c=self)

    def to_mass(self, moles: float) -> float:
        return stoic.cal_mass(self, moles)

    def to_moles(self, mass: float) -> float:
        return stoic.cal_moles(self, mass)

    """ Make Hashable """

    def __str__(self):
        # return str(dict(self.cnt))
        return self._formula

    def __hash__(self):
        return hash(self._formula)


class MixtureImpl(Mixture):

    def __init__(self, s: str):
        from src.parse import construct_mix

        super().__init__()
        self.values = construct_mix(s)

    @property
    def cnt(self) -> dict[Compound, int]:
        return self.values

    @property
    def element_cnt(self) -> dict[str, int]:
        return count_mix(self.values)

    def __str__(self):
        # full: str
        # for (self )
        return str(dict(self.cnt))


class StoicImpl(StoicInterface):
    # TODO Stoic

    def impl_type(self):
        return 0

    def cal_molar_mass(self, c: Compound) -> float:
        total: float = 0

        for ele, cnt in c.cnt.items():
            total += PT.get(ele).MOLAR_MASS * cnt

        return total

    def cal_moles(self, c: Compound, mass: float) -> float:
        return mass / c.molar_mass

    def cal_mass(self, c: Compound, moles: float) -> float:
        return moles * c.molar_mass

    def is_balanced(self, r: Mixture, p: Mixture) -> bool:
        return r.element_cnt == p.element_cnt

    def can_balance(self, r: Mixture, p: Mixture) -> bool:
        return r.element_cnt.keys() == p.element_cnt.keys()

    def balance(self, r: Mixture, p: Mixture) -> bool:
        if not self.can_balance(r, p):
            raise StoicException("Impossible")
        if self.is_balanced(r, p):
            return True
        gcd = math.gcd(
            util.gcd(list(r.cnt.values())),
            util.gcd(list(p.cnt.values())))
        for (cpd, cnt) in r.cnt.items():
            r.cnt[cpd] = cnt / gcd
        for (cpd, cnt) in p.cnt.items():
            p.cnt[cpd] = cnt / gcd
        return True

    def cal_p_y(self) -> float:
        """ Percentage Yield """
        raise NotImplementedError

    def cal_a_e(self) -> float:
        """ Atom Economy """
        raise NotImplementedError


stoic = StoicImpl()
