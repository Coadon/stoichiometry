import sys

from parse import ChemFormulaException
from util import ANSI, mixture

VERSION = "v1.0"
print(f"Stoichiometry {VERSION} | MIT")


def main():
    try:
        c = mixture("2Cl2 + Na")
        print(c.counts)
        print(list(c.raw)[0].molar_mass)
    except ChemFormulaException as e:
        print(ANSI.RED + "Error parsing: " + e.args[0] + ANSI.RESET)
    # except Exception as e:
    #     print(ANSI.RED + e.args[0] + ANSI.RESET)

    while True:
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    sys.exit(0)
