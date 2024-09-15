from collections import OrderedDict
from enum import Enum, auto
from typing import Optional, Final


# Element Series
class Series(Enum):
    NonMetal = auto()
    Metalloid = auto()
    Metal = auto()
    NobleGas = auto()


class Element():
    def __init__(self,
                 atomic_number: int,
                 molar_mass: float,
                 name: str,
                 series: Optional[Series]):
        self.SERIES: Final[Series] = series
        self.NAME: Final[str] = name
        self.MOLAR_MASS: Final[float] = molar_mass
        self.ATOMIC_NUMBER: Final[int] = atomic_number


# Periodic Table of Elements -- Lookup Table
# Key: Element Name
# Value: (Atomic Number, Relative Atomic Mass, Full Name, Series)
PT = OrderedDict({
    "_n":   Element(0, 0, "Neutronium", None),
    # Series 1
    "H":    Element(1, 1.008, "Hydrogen", Series.NonMetal),
    "He":   Element(2, 4.0026, "Helium", Series.NobleGas),
    # Series 2
    "Li":   Element(3, 6.94, "Lithium", Series.Metal),
    "Be":   Element(4, 9.0122, "Beryllium", Series.Metal),
    "B":    Element(5, 10.81, "Boron", Series.Metalloid),
    "C":    Element(6, 12.011, "Carbon", Series.NonMetal),
    "N":    Element(7, 14.007, "Nitrogen", Series.NonMetal),
    "O":    Element(8, 15.999, "Oxygen", Series.NonMetal),
    "F":    Element(9, 18.998, "Fluorine", Series.NonMetal),
    "Ne":   Element(10, 20.180, "Neon", Series.NobleGas),
    # Series 3
    "Na":   Element(11, 22.990, "Sodium", Series.Metal),
    "Mg":   Element(12, 24.305, "Magnesium", Series.Metal),
    "Al":   Element(13, 26.982, "Aluminum", Series.Metal),
    "Si":   Element(14, 28.085, "Silicon", Series.Metalloid),
    "P":    Element(15, 30.974, "Phosphorus", Series.NonMetal),
    "S":    Element(16, 32.06, "Sulfur", Series.NonMetal),
    "Cl":   Element(17, 35.45, "Chlorine", Series.NonMetal),
    "Ar":   Element(18, 39.948, "Argon", Series.NobleGas),
    # TODO Finish all
})
