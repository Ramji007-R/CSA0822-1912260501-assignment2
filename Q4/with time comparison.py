import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    return "".join(f"{p};" for p in parts)


for size in [1000, 10000, 200000]:
    data = items[:size]

    for name, function in [
        ("Plus", build_plus),
        ("Join", build_join),
        ("F-string", build_fstring)
    ]:
        times = []

        for i in range(3):
            start = time.perf_counter()
            result = function(data)
            elapsed = time.perf_counter() - start
            times.append(elapsed)

        average = sum(times) / 3

        print(name, size, "Average:", average, "seconds")
