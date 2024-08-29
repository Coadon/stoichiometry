from collections import OrderedDict
from enum import Enum, auto


# Element Series
class Series(Enum):
    NonMetal = auto()
    Metalloid = auto()
    Metal = auto()
    NobleGas = auto()


# Periodic Table of Elements -- Lookup Table
# Key: Element Name
# Value: (Atomic Number, Relative Atomic Mass, Full Name, Series)
PT = OrderedDict({
    "_n":   (0, 0,      "Neutronium", None),
    # Series 1
    "H":    (1, 1.008,  "Hydrogen",     Series.NonMetal),
    "He":   (2, 4.0026, "Helium",       Series.NobleGas),
    # Series 2
    "Li":   (3, 6.94,   "Lithium",      Series.Metal),
    "Be":   (4, 9.0122, "Beryllium",    Series.Metal),
    "B":    (5, 10.81,  "Boron",        Series.Metalloid),
    "C":    (6, 12.011, "Carbon",       Series.NonMetal),
    "N":    (7, 14.007, "Nitrogen",     Series.NonMetal),
    "O":    (8, 15.999, "Oxygen",       Series.NonMetal),
    "F":    (9, 18.998, "Fluorine",     Series.NonMetal),
    "Ne":   (10, 20.180, "Neon",        Series.NobleGas),
    # Series 3
    "Na":   (11, 22.990, "Sodium",      Series.Metal),
    "Mg":   (12, 24.305, "Magnesium",   Series.Metal),
    "Al":   (13, 26.982, "Aluminum",    Series.Metal),
    "Si":   (14, 28.085, "Silicon",     Series.Metalloid),
    "P":    (15, 30.974, "Phosphorus",  Series.NonMetal),
    "S":    (16, 32.06, "Sulfur",       Series.NonMetal),
    "Cl":   (17, 35.45, "Chlorine",     Series.NonMetal),
    "Ar":   (18, 39.948, "Argon",       Series.NobleGas),
    # More to come.
})
