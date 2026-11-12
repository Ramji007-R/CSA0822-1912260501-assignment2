def normalise(text):
    text = text.strip().upper()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (
        state.isalpha()
        and district.isdigit()
        and len(series) in (1, 2)
        and series.isalpha()
        and number.isdigit()
    )


def format_number(reg):
    if not is_valid(reg):
        return "Invalid Registration"

    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 CD 4567",
    "KL-07-A-1234"
]

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", format_number(reg))
    else:
        print(raw, "-> INVALID")
