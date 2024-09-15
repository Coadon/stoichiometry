from src.interf import Molecule, Mixture, StoicInterface


def molecule(formula: str) -> Molecule:
    from src.custom import MoleculeImpl
    return MoleculeImpl(formula)


def mixture(formula: str) -> Mixture:
    from src.custom import MixtureImpl
    return MixtureImpl(formula)


@property
def stoic(formula: str) -> StoicInterface:
    from src.custom import stoic
    return stoic


class ANSI:
    CYAN = "\033[96m"
    PINK = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
