import re
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=4, year=2024).splitlines()
samp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()


def get_vertical(text):
    strings = []
    for i in range(0, len(text)):
        vertical = [o[i] for o in text]
        vertical = "".join(vertical)
        strings.append(vertical)
    return strings


def get_diag(lines, row, col):
    chars = []
    while row < len(lines) and col < len(lines[0]):
        chars.append(lines[row][col])
        row += 1
        col += 1
    return "".join(chars)


def get_all_diag(lines):
    diagonals = []

    # Down-right for each char in first row
    for col in range(len(lines[0])):
        diag = get_diag(lines, row=0, col=col)
        if len(diag) >= 4:
            diagonals.append(diag)

    # Down-right for each char in first column
    for row in range(1, len(lines)):
        diag = get_diag(lines, row=row, col=0)
        if len(diag) >= 4:
            diagonals.append(diag)

    return diagonals


def solve_a(lines):
    matches = []

    # Check horizontal
    for row, line in enumerate(lines):
        for m in re.finditer(r"XMAS", line):
            matches.append(("hor", row, m.start(), "XMAS"))
        for m in re.finditer(r"SAMX", line):
            matches.append(("hor", row, m.start(), "SAMX"))

    # Check vertical
    vert = get_vertical(lines)
    for col, line in enumerate(vert):
        for m in re.finditer(r"XMAS", line):
            matches.append(("vert", m.start(), col, "XMAS"))
        for m in re.finditer(r"SAMX", line):
            matches.append(("vert", m.start(), col, "SAMX"))

    # Check diagonals (down-right)
    dr = get_all_diag(lines)
    for diag in dr:
        for m in re.finditer(r"XMAS", diag):
            matches.append(("diag-right", diag, m.start(), "XMAS"))
        for m in re.finditer(r"SAMX", diag):
            matches.append(("diag-right", diag, m.start(), "SAMX"))

    # Check diagonals (down-left)
    rev = [o[::-1] for o in lines]
    dl = get_all_diag(rev)
    for diag in dl:
        for m in re.finditer(r"XMAS", diag):
            matches.append(("diag-left", diag, m.start(), "XMAS"))
        for m in re.finditer(r"SAMX", diag):
            matches.append(("diag-left", diag, m.start(), "SAMX"))

    # DEBUG: Print all matches
    # for match in matches:
    #     print(match)

    return len(matches)


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(text):
    return 0


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
