def subsidy_match(units, ration, senior):
    match True:
        case _ if units <= 100:
            return "Full Subsidy"
        case _ if 101 <= units <= 200 and ration:
            return "Partial Subsidy"
        case _ if units > 200 and senior:
            return "Senior Subsidy"
        case _:
            return "No Subsidy"


print(subsidy_match(150, True, False))
