import re
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=3, year=2023)
samp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def find_numbers(text):
    matches = []
    for i, line in enumerate(text.splitlines()):
        for match in re.finditer(r"\d+", line):
            matches.append(
                {
                    "line": i,
                    "num": int(match.group()),
                    "start": match.start(),
                    "end": match.end(),
                }
            )
    return matches


def find_symbols(text):
    matches = []
    for i, line in enumerate(text.splitlines()):
        for match in re.finditer(r"[!@#$%^&*()_+={}\[\]:;\"'<>,?/\|`~-]", line):
            matches.append({"line": i, "start": match.start()})
    return matches


def is_adjacent(number, symbol):
    return (
        abs(number["line"] - symbol["line"]) <= 1
        and max(0, number["start"] - 1) <= symbol["start"] <= number["end"]
    )


def solve_a(text):
    numbers = find_numbers(text)
    symbols = find_symbols(text)
    parts_sum = 0
    for o in numbers:
        for p in symbols:
            if is_adjacent(o, p):
                parts_sum += o["num"]
    return parts_sum


print(f"sample a: {solve_a(samp)}")
print(f"solution a: {solve_a(data)}\n")


def solve_b(text):
    numbers = find_numbers(text)
    symbols = find_symbols(text)
    for o in numbers:
        for p in symbols:
            if is_adjacent(o, p):
                p.setdefault("nums", []).append(o["num"])
    gears = [v for v in symbols if len(v.get("nums", [])) == 2]
    return sum(g["nums"][0] * g["nums"][1] for g in gears)


print(f"sample b: {solve_b(samp)}")
print(f"solution b: {solve_b(data)}")
