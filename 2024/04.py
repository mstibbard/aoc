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


def get_diagonal(lines, row, col, right):
    chars = []
    while row < len(lines) and 0 <= col < len(lines[0]):
        chars.append(lines[row][col])
        row += 1
        col += 1 if right else -1
    return "".join(chars)


def find_matches(string, pos, label):
    matches = []
    for match in re.finditer(pattern=r"MAS", string=string):
        matches.append(
            {
                "dir": label,
                "string": string,
                "start_pos": pos,
                "found": match.group(),
                "found_at": match.start(),
            }
        )
    for match in re.finditer(pattern=r"SAM", string=string):
        matches.append(
            {
                "dir": label,
                "string": string,
                "start_pos": pos,
                "found": match.group(),
                "found_at": match.start(),
            }
        )
    return matches


def solve_b(lines):
    matches = []
    line_width = len(lines[0])
    # diagonal right across top row
    for col in range(len(lines[0])):
        dr = get_diagonal(lines, 0, col, right=True)
        matches.extend(find_matches(dr, (0, col), "DR"))

    # diagonal right down left column
    for row in range(1, len(lines)):
        dr = get_diagonal(lines, row, 0, right=True)
        matches.extend(find_matches(dr, (row, 0), "DR"))

    # diagonal left across top row
    for col in range(line_width):
        dl = get_diagonal(lines, 0, col, right=False)
        matches.extend(find_matches(dl, (0, col), "DL"))

    # diagonal left down left column
    for row in range(1, len(lines)):
        dl = get_diagonal(lines, row, line_width - 1, right=False)
        matches.extend(find_matches(dl, (row, line_width - 1), "DL"))

    for i, o in enumerate(matches):
        if o["dir"] == "DR":
            matches[i]["A_at"] = (
                o["start_pos"][0] + o["found_at"] + 1,
                o["start_pos"][1] + o["found_at"] + 1,
            )
        if o["dir"] == "DL":
            matches[i]["A_at"] = (
                o["start_pos"][0] + o["found_at"] + 1,
                o["start_pos"][1] - o["found_at"] - 1,
            )

    matches_count = {}
    for o in matches:
        key = o["A_at"]
        count = 1
        if key in matches_count:
            count = matches_count[key] + 1
        matches_count[key] = count

    overlap = {key: value for key, value in matches_count.items() if value == 2}

    return len(overlap)


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
