def subsidy_separate(units, ration, senior):
    result = []

    if units <= 100:
        result.append("Full Subsidy")

    # Incorrect: missing the lower boundary (101)
    if units <= 200 and ration:
        result.append("Partial Subsidy")

    if units > 200 and senior:
        result.append("Senior Subsidy")

    if not result:
        result.append("No Subsidy")

    return result


print(subsidy_separate(100, True, False))
