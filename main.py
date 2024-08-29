from lookup import PT
import re

RE_CHAR_NUM = re.compile("([a-zA-Z]+)([0-9]+)")
# https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string/

# Molar Mass Calculator

R = re.split(" |, |\\+",
             input("Reactants: "))

R = (v.strip() for v in R)

# Remove ''s
R = filter(None, R)
R = filter(bool, R)
R = filter(len, R)
R = filter(lambda v: v, R)
R = list(R)

R_mass: float = 0

c: str
e: str
for (i, c) in enumerate(R):
    res = RE_CHAR_NUM.match(c).groups()
    es = re.findall("[A-Z][^A-Z]*", c)
    print(es)


    for e in es:
        if e in PT:
            # n =
            R_mass += PT[e][1]
        else:
            print(f"'{e}' is not a valid element.")

print(f"Relative Molecular Mass: {R_mass}")



