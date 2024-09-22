import sys

from src.custom import stoic
from util import molecule, mixture

VERSION = "v1.02"
print(f"Stoichiometry {VERSION} | MIT")


def feed_in(feed: str):
    if len(feed) == 0:
        return
    elif feed == "quit":
        return -1
    elif feed == "help":
        pass

    feed = feed.split(" ")

    if feed[0][0].isupper():
        m = molecule(feed[0])
        print(f"Molar Mass: {m.molar_mass}")
        if len(feed) <= 1:
            return
        elif feed[1].endswith("g"):
            pass
        elif feed[1].endswith("mol"):
            pass
    else:
        print("What? Use 'help' or 'quit'")

# TODO Stop using DICT for MIXTURES. Use two LISTS. One with ELEMENTS, another for count.
# TODO Overhaul STOIC for the aforesaid


if __name__ == "__main__":
    # TESTS
    r = mixture("2NaCl + 6NaCl")
    p = mixture("2NaCl + 4NaCl")
    print(r.element_cnt)
    print(p.element_cnt)
    print(p.element_cnt.values())
    print("Is " + str(stoic.is_balanced(r, p)))
    print("Can " + str(stoic.can_balance(r, p)))
    stoic.balance(r, p)
    print("Into " + str(r.cnt) + " = " + str(p.cnt))
    sys.exit(0)

    try:
        while True:
            if feed_in(input("> ")) == -1:
                break
    except KeyboardInterrupt:
        pass
    sys.exit(0)
