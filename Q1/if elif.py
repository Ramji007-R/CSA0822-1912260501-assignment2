def subsidy(units, ration, senior):
    if units <= 100:
        return "Full Subsidy"

    elif 101 <= units <= 200 and ration:
        return "Partial Subsidy"

    elif units > 200 and senior:
        return "Senior Subsidy"

    else:
        return "No Subsidy"


households = [
    (100, False, False),
    (101, True, False),
    (150, True, False),
    (200, True, False),
    (201, False, True),
    (250, False, False),
    (80, True, True),
    (180, False, True)
]

for h in households:
    print(h, "->", subsidy(*h))
